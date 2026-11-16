# Ponto de retoma

Estado verificado em 16 de Novembro de 2026: divisores D1–D5 concluídos, em 30 páginas; reconstrução de FCMP++ F1–F8 concluída, em 38 páginas de texto, seguida de um poster novo em A3. O livro compilado tem 310 páginas. O trabalho foi retomado com autorização para todo o âmbito e orçamento de 1 000 000 de tokens. O objectivo está activo. O checkpoint D1–D5/F1–F6 ficou guardado em `e0e6b12`; F7 foi concluída em `0ab541c`; a preparação de F8 ficou em `af5f0f0`; F8 e os PDFs verificados ficaram em `f4858c0`; o poster ficou em `8d85712`.

## Próxima unidade

Desenvolver a vulnerabilidade histórica das imagens de chave, com a componente de torção, a falha de ligação e o alcance da investigação publicada. As receitas de H_p e H estão redigidas e conferidas contra a fonte C; «canónico» está explicado na primeira utilização relevante. Prosseguir depois para DDH, MLSAG/CLSAG, Bulletproofs, a estrutura das entradas e o índice, conservando todo o âmbito abaixo.

A preparação de F8 permanece em `editorial/fcmp-F8-preparation.md` como registo das fontes. O texto TeX já inclui a extracção descendente, a estabilidade da imagem, a simulação com enunciado fixo, as fórmulas exactas do tamanho e os custos. `editorial/checks/composition-costs-F8.py` verifica as contas e pode compará-las directamente com as funções Rust, compiladas isoladamente em /tmp.

F7 fixa a sequência completa e demonstra um limite incondicional para dados fixados antes de desafios ideais. A redução efectiva dos resumos e as tentativas adaptativas de Fiat–Shamir conservam a sua análise própria. A normalização e os domínios das testemunhas honestas continuam condicionados; não apresentar uma garantia incondicional de completude nem inventar um procedimento de repetição. F8 conserva expressamente a hipótese de simulação da distribuição condicionada para a realização concreta. O poster novo está em `translations/pt/posters/fcmp-composition/`; os dois conjuntos de figuras antigos foram retirados e permanecem recuperáveis pelo Git.

## Restante âmbito autorizado

- Índice remissivo no fim, incluindo símbolos, siglas e remissões entre termos.
- Explicação aprofundada da vulnerabilidade histórica das imagens de chave e da verificação de subgrupo.
- Remover a frase da variante ligável indicada na antiga página 57; explicar DDH e representações canónicas.
- Rever a expressão da especialização de MLSAG; acrescentar duas páginas pedagógicas a CLSAG.
- Simplificar a verificação de Bulletproofs, conservando as duas igualdades: retirar E_0/E_IP e a combinação opcional por pesos.
- Remover o conteúdo indicado da antiga página 109, após localização na edição de referência.
- Corrigir a explicação dos anéis/índices e acrescentar três páginas sobre índices absolutos e relativos, reconstrução dos anéis e estrutura de tx_extra. Os key_offsets pertencem às entradas, não a tx_extra.
- Revisão global de «de/por/em Monero», «lista de blocos» e exposição afirmativa; reconciliar a notação do capítulo das relações de logaritmo discreto com I como imagem e J como base.
- Compilar e inspeccionar o livro completo, os excertos e o índice; fechar as alterações restantes em commits verificados. Não foi pedido push.

Os números de página dos pedidos referem-se ao exemplar impresso anterior; as localizações actuais devem ser identificadas pelo conteúdo. A nota terminológica solicitada já está em FCMP++, e as directivas de estilo estão em AGENTS.md.

## Verificação e composição

As contas reproduzíveis estão em `editorial/checks/`. Os programas usam Python 3 e a biblioteca padrão; a comparação opcional de F8 com a fonte exige rustc, e a comparação dos mapas com a fonte C exige gcc, libsodium e os cabeçalhos indicados no registo de versões. Os registos de notação, dependências, fontes e revisão descrevem o âmbito e os limites das verificações.

`python3 editorial/build-pt.py` compila o livro; acrescentar `--export` actualiza o PDF principal e chama `editorial/export-chapters.py`, que confere texto e imagem de todas as páginas dos excertos antes de os substituir. Os auxiliares, os padrões portugueses do TeX e as imagens de inspecção estão em `/tmp/ztm-editorial-build` e `/tmp/ztm-latex-deps`; são recursos temporários. Os programas de compilação e exportação ficam agora no repositório. O registo de versões documenta a preparação do ambiente. As fontes definitivas são `translations/pt/main.tex`, os ficheiros de conteúdo e a bibliografia; a composição normal usa pdflatex e bibtex, com as passagens necessárias para estabilizar as remissões.
