# Ponto de retoma

Estado verificado em 11 de Novembro de 2026: divisores D1–D5 concluídos, em 30 páginas; reconstrução de FCMP++ F1–F7 concluída até ao transcrito e à análise da amostragem, em 32 das 38 páginas previstas. O livro compilado tem 300 páginas. A revisão integral continua activa. O checkpoint D1–D5/F1–F6 ficou guardado em `e0e6b12`; F7 constitui uma unidade própria.

## Próxima unidade

F8: composição final de segurança e custos completos. Reunir as garantias de pertença, autorização, vinculação ao gasto, imagem de chave e ocultação, com as hipóteses exactas das fontes primárias. Desenvolver a extracção descendente desde a raiz e a ligação a SAL sem repetir os cálculos já demonstrados. Deduzir o tamanho da prova a partir dos compromissos e dimensões de F6; as contagens preparatórias estão no registo de versões. O capítulo tem seis páginas de margem até às 38 previstas; a última página de F7 pode receber a continuação natural.

F7 fixa a sequência completa e demonstra um limite incondicional para dados fixados antes de desafios ideais. A redução efectiva dos resumos e as tentativas adaptativas de Fiat–Shamir conservam a sua análise própria. A normalização e os domínios das testemunhas honestas continuam condicionados; não apresentar uma garantia incondicional de completude nem inventar um procedimento de repetição. Depois de F8, ajustar FCMP++ a 38 páginas de texto e construir o poster novo. O poster antigo permanece fora da composição; o capítulo antigo é recuperável pelo Git.

## Restante âmbito autorizado

- Índice remissivo no fim, incluindo símbolos, siglas e remissões entre termos.
- Receitas exactas de H_p e do gerador H, com as distinções pertinentes.
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

As contas reproduzíveis estão em `editorial/checks/`. Os seis programas usam apenas Python 3 e a biblioteca padrão. Os registos de notação, dependências, fontes e revisão descrevem o âmbito e os limites das verificações.

Nesta sessão, `python3 /tmp/ztm-build-pt.py` compila o livro; `python3 /tmp/ztm-export-chapters.py` actualiza e confere os três PDFs. Os auxiliares, os padrões portugueses do TeX e as imagens de inspecção estão em `/tmp/ztm-editorial-build` e `/tmp/ztm-latex-deps`; são recursos temporários. O registo de versões documenta a preparação do ambiente. As fontes definitivas são `translations/pt/main.tex`, os ficheiros de conteúdo e a bibliografia; a composição normal usa pdflatex e bibtex, com as passagens necessárias para estabilizar as remissões.
