#!/usr/bin/env python3
"""Extrai os capítulos e confere o texto e a imagem de todas as páginas."""

import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def text_pages(pdf, first, last):
    return subprocess.check_output(["pdftotext", "-layout", "-f", str(first),
                                    "-l", str(last), str(pdf), "-"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", type=Path, default=ROOT / "Zero-to-Monero-2-0-0-pt.pdf")
    args = parser.parse_args()
    book = args.book.resolve()
    raw = subprocess.check_output(["pdfinfo", "-dests", str(book)], text=True)
    destinations = {name: int(page) for page, name in
                    re.findall(r'^\s*(\d+)\s+\[.*\]\s+"([^"]+)"', raw, re.M)}
    chapters = [("Divisores-pt.pdf", "chapter.3", "chapter.4"),
                ("FCMP-pt.pdf", "chapter.11", "chapter.12")]
    with tempfile.TemporaryDirectory(prefix="ztm-export-") as temporary:
        work = Path(temporary)
        for name, start, following in chapters:
            first = destinations[start]
            last = destinations[following] - 1
            total = last - first + 1
            output = work / name
            subprocess.run(["mutool", "merge", "-o", str(output), str(book),
                            f"{first}-{last}"], check=True)
            if text_pages(book, first, last) != text_pages(output, 1, total):
                raise SystemExit(f"O texto do excerto {name} diverge do livro.")
            print(f"{name}: páginas {first}–{last}; a conferir {total} imagens.", flush=True)
            for offset in range(total):
                hashes = []
                for pdf, page in ((book, first + offset), (output, offset + 1)):
                    pixels = subprocess.check_output([
                        "pdftoppm", "-r", "100", "-singlefile", "-f", str(page),
                        "-l", str(page), str(pdf)])
                    hashes.append(hashlib.sha256(pixels).digest())
                if hashes[0] != hashes[1]:
                    raise SystemExit(f"Imagem divergente em {name}, página {offset + 1}.")
            destination = ROOT / "translations/pt" / name
            destination.write_bytes(output.read_bytes())
            print(f"{name}: {total} páginas conferidas.", flush=True)


if __name__ == "__main__":
    main()
