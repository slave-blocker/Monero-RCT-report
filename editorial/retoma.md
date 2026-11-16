# Ponto de retoma

Estado verificado em 16 de Novembro de 2026: divisores D1–D5 concluídos, em 30 páginas; reconstrução de FCMP++ F1–F8 concluída, em 38 páginas de texto, seguida de um poster novo em A3. O livro compilado tem 315 páginas. O trabalho foi retomado com autorização para todo o âmbito e orçamento de 1 000 000 de tokens. O objectivo está activo. O checkpoint D1–D5/F1–F6 ficou guardado em `e0e6b12`; F7 foi concluída em `0ab541c`; a preparação de F8 ficou em `af5f0f0`; F8 e os PDFs verificados ficaram em `f4858c0`; o poster ficou em `8d85712`; as receitas de pontos e o gerador H ficaram em `ce00840`; as imagens de chave e DDH ficaram em `0e9b26c`; CLSAG ficou em `d5c4060`; Bulletproofs ficou em `d85fff7`.

## Próxima unidade

Criar o índice remissivo no fim, com símbolos, siglas, sinónimos e remissões, e prosseguir a revisão global de terminologia, exposição afirmativa e composição. A unidade das transacções acrescentou três páginas: representação uniforme dos membros, posição secreta por entrada, índices globais e relativos, varints, reconstrução dos anéis e leitura de tx_extra. Falta ainda reconciliar I/J no capítulo das relações entre geradores.

A preparação de F8 permanece em `editorial/fcmp-F8-preparation.md` como registo das fontes. O texto TeX já inclui a extracção descendente, a estabilidade da imagem, a simulação com enunciado fixo, as fórmulas exactas do tamanho e os custos. `editorial/checks/composition-costs-F8.py` verifica as contas e pode compará-las directamente com as funções Rust, compiladas isoladamente em /tmp.

F7 fixa a sequência completa e demonstra um limite incondicional para dados fixados antes de desafios ideais. A redução efectiva dos resumos e as tentativas adaptativas de Fiat–Shamir conservam a sua análise própria. A normalização e os domínios das testemunhas honestas continuam condicionados; não apresentar uma garantia incondicional de completude nem inventar um procedimento de repetição. F8 conserva expressamente a hipótese de simulação da distribuição condicionada para a realização concreta. O poster novo está em `translations/pt/posters/fcmp-composition/`; os dois conjuntos de figuras antigos foram retirados e permanecem recuperáveis pelo Git.

## Restante âmbito autorizado

- Índice remissivo no fim, incluindo símbolos, siglas e remissões entre termos.
- Revisão global de «de/por/em Monero», «lista de blocos» e exposição afirmativa; reconciliar a notação do capítulo das relações de logaritmo discreto com I como imagem e J como base.
- Compilar e inspeccionar o livro completo, os excertos e o índice; fechar as alterações restantes em commits verificados. Não foi pedido push.

Os números de página dos pedidos referem-se ao exemplar impresso anterior; as localizações actuais devem ser identificadas pelo conteúdo. A nota terminológica solicitada já está em FCMP++, e as directivas de estilo estão em AGENTS.md.

## Verificação e composição

As contas reproduzíveis estão em `editorial/checks/`. Os programas usam Python 3 e a biblioteca padrão; a comparação opcional de F8 com a fonte exige rustc, e a comparação dos mapas com a fonte C exige gcc, libsodium e os cabeçalhos indicados no registo de versões. Os registos de notação, dependências, fontes e revisão descrevem o âmbito e os limites das verificações.

`python3 editorial/build-pt.py` compila o livro; acrescentar `--export` actualiza o PDF principal e chama `editorial/export-chapters.py`, que confere texto e imagem de todas as páginas dos excertos antes de os substituir. Os auxiliares, os padrões portugueses do TeX e as imagens de inspecção estão em `/tmp/ztm-editorial-build` e `/tmp/ztm-latex-deps`; são recursos temporários. Os programas de compilação e exportação ficam agora no repositório. O registo de versões documenta a preparação do ambiente. As fontes definitivas são `translations/pt/main.tex`, os ficheiros de conteúdo e a bibliografia; a composição normal usa pdflatex e bibtex, com as passagens necessárias para estabilizar as remissões.
