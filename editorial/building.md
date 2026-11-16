# Composição da edição portuguesa

Executar `python3 editorial/build-pt.py` a partir do repositório. O programa usa pdflatex e bibtex, estabiliza as remissões e termina se encontrar referências ou citações por resolver. Se existir um índice remissivo, executa também makeindex. O resultado fica em `/tmp/ztm-editorial-build/main.pdf`.

Acrescentar `--export` actualiza `Zero-to-Monero-2-0-0-pt.pdf` e os excertos de divisores e FCMP++. O programa de exportação usa os destinos dos capítulos no PDF, compara o texto e a rasterização a 100 dpi de todas as páginas, e só depois substitui cada excerto. Também pode executar-se separadamente com `python3 editorial/export-chapters.py`.

Os directórios temporários são configuráveis com `--build-dir` e `--tex-deps`. A exportação requer os utilitários pdfinfo, pdftotext, pdftoppm e mutool.

## Hifenização portuguesa sem instalação no sistema

Se o TeX instalado já inclui `portuguese.ldf`, o programa usa a configuração existente. Caso contrário, pode usar-se uma extracção local do pacote oficial da distribuição. No ambiente Ubuntu Noble usado nesta revisão:

```bash
mkdir -p /tmp/ztm-latex-deps
cd /tmp/ztm-latex-deps
apt-get download texlive-lang-portuguese
dpkg-deb -x texlive-lang-portuguese_2023.20240207-1_all.deb portuguese
```

O programa prepara depois um formato pdflatex com os padrões portugueses em `/tmp/ztm-latex-deps`, usando fmtutil-user e variáveis TEXMF dirigidas a esse directório. Mantém a instalação geral intacta. Se a distribuição fornecer outra versão do pacote, ajustar o nome do ficheiro `.deb` ao descarregado.

Os registos de cada passagem ficam no directório de compilação. Os ficheiros de conteúdo, a bibliografia e os programas em `editorial/` são os elementos duradouros; os directórios de `/tmp` podem ser reconstruídos.
