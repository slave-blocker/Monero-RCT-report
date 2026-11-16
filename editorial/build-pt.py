#!/usr/bin/env python3
"""Compõe a edição portuguesa, mantendo os auxiliares fora das fontes."""

import argparse
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "translations" / "pt"


def run(command, *, cwd, env, log):
    with log.open("w") as stream:
        result = subprocess.run(command, cwd=cwd, env=env, stdout=stream,
                                stderr=subprocess.STDOUT)
    if result.returncode:
        print(log.read_text(errors="replace")[-6000:])
        raise SystemExit(f"Falhou {command[0]}; registo: {log}")


def tex_environment(deps, build):
    env = os.environ.copy()
    found = subprocess.run(["kpsewhich", "portuguese.ldf"],
                           capture_output=True, text=True)
    if not found.stdout.strip():
        tex = deps / "portuguese/usr/share/texlive/texmf-dist/tex"
        if not tex.is_dir():
            raise SystemExit(
                "Falta texlive-lang-portuguese. Instale-o, ou extraia o pacote "
                f"com dpkg-deb -x PACOTE.deb {deps / 'portuguese'}.")
        config = deps / "config"
        config.mkdir(parents=True, exist_ok=True)
        language_file = subprocess.check_output(
            ["kpsewhich", "language.dat"], text=True).strip()
        language = Path(language_file).read_text()
        if not re.search(r"^portuguese\s", language, re.M):
            language += "\nportuguese loadhyph-pt.tex\n=portuges\n"
        (config / "language.dat").write_text(language)
        env["TEXINPUTS"] = f"{config}//:{tex}//:" + env.get("TEXINPUTS", "")
        env["TEXMFVAR"] = str(deps / "texmf-var")
        env["TEXMFCONFIG"] = str(deps / "texmf-config")
        fmt = deps / "texmf-var/web2c/pdftex/pdflatex.fmt"
        if not fmt.is_file():
            run(["fmtutil-user", "--byfmt", "pdflatex"], cwd=SOURCE,
                env=env, log=build / "format.log")
    env["BIBINPUTS"] = f"{SOURCE}//:" + env.get("BIBINPUTS", "")
    env["BSTINPUTS"] = f"{SOURCE}//:" + env.get("BSTINPUTS", "")
    return env


def reference_state(build):
    paths = sorted(build.rglob("*.aux")) + [
        build / "main.toc", build / "main.out", build / "main.idx", build / "main.ind"]
    return [(str(p), hashlib.sha256(p.read_bytes()).hexdigest())
            for p in paths if p.exists()]


def build_index(build, env):
    index = build / "main.idx"
    if not index.exists():
        return
    command = ["makeindex", "-s", str(SOURCE / "back/index.ist"), "main.idx"]
    run(command, cwd=build, env=env, log=build / "makeindex.log")
    transcript = (build / "main.ilg").read_text(errors="replace")
    if re.search(r"!!|\b[1-9][0-9]* (?:entries )?rejected\b|\b[1-9][0-9]* warnings\b", transcript):
        raise SystemExit(f"Índice com entradas rejeitadas ou avisos: {build / 'main.ilg'}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, default=Path("/tmp/ztm-editorial-build"))
    parser.add_argument("--tex-deps", type=Path, default=Path("/tmp/ztm-latex-deps"))
    parser.add_argument("--export", action="store_true", help="Actualiza os três PDFs do repositório.")
    args = parser.parse_args()
    build = args.build_dir.resolve()
    build.mkdir(parents=True, exist_ok=True)
    for part in ("front", "content", "back"):
        (build / part).mkdir(exist_ok=True)
    env = tex_environment(args.tex_deps.resolve(), build)
    poster_source = SOURCE / "posters/fcmp-composition"
    poster_tex, poster_pdf = poster_source / "poster.tex", poster_source / "poster.pdf"
    if poster_tex.exists() and (
            not poster_pdf.exists() or poster_tex.stat().st_mtime > poster_pdf.stat().st_mtime):
        poster_build = build / "fcmp-poster"
        poster_build.mkdir(exist_ok=True)
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
             f"-output-directory={poster_build}", "poster.tex"],
            cwd=poster_source, env=env, log=poster_build / "build.log")
        shutil.copy2(poster_build / "poster.pdf", poster_source / "poster.pdf")
    latex = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
             f"-output-directory={build}", "main.tex"]
    run(latex, cwd=SOURCE, env=env, log=build / "pass-1.log")
    run(["bibtex", "main"], cwd=build, env=env, log=build / "bibtex.log")
    build_index(build, env)
    for number in range(2, 8):
        before = reference_state(build)
        run(latex, cwd=SOURCE, env=env, log=build / f"pass-{number}.log")
        build_index(build, env)
        if before == reference_state(build):
            break
    else:
        raise SystemExit("As remissões ainda variam depois de sete passagens.")
    log = (build / "main.log").read_text(errors="replace")
    unresolved = re.findall(r"LaTeX Warning: (?:Reference|Citation).*?undefined.*", log)
    unresolved += re.findall(r"LaTeX Warning: There were undefined.*", log)
    if unresolved:
        raise SystemExit("\n".join(unresolved))
    info = subprocess.check_output(["pdfinfo", str(build / "main.pdf")], text=True)
    print(re.search(r"^Pages:.*", info, re.M).group())
    print(f"Avisos de caixas: {len(re.findall(r'(?:Over|Under)full', log))}")
    print(f"PDF: {build / 'main.pdf'}")
    if args.export:
        shutil.copy2(build / "main.pdf", ROOT / "Zero-to-Monero-2-0-0-pt.pdf")
        subprocess.run(["python3", str(ROOT / "editorial/export-chapters.py")], check=True)


if __name__ == "__main__":
    main()
