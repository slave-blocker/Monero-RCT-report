# Ponto de retoma

Estado verificado em 11 de Novembro de 2026: divisores D1–D5 concluídos, em 30 páginas; reconstrução de FCMP++ F1–F6 concluída até às condições dos dois circuitos, em 27 das 38 páginas previstas. O livro compilado tem 295 páginas. A revisão integral continua activa.

## Próxima unidade

F7: transcrito e ordem dos desafios, a partir das fontes já conferidas. Desenvolver o contexto, os compromissos das duas curvas, o desafio da raiz, os desafios dos divisores, os seis pesos por entrada e as provas GBP sequenciais. O par de Schnorr da raiz é serializado à parte; a sua resposta não é absorvida pelo transcrito. Na primeira entrada, os desafios de divisores seguem Wei, Helios se L≥3, Selene se L≥2; os dois últimos são reutilizados nas entradas seguintes. A análise dos desafios excepcionais deve conservar a distinção face ao modelo regular de D5.

Depois, concluir a composição de segurança, ajustar FCMP++ a 38 páginas de texto e construir o poster novo. O poster antigo permanece fora da composição; o capítulo antigo é recuperável pelo Git.

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

As contas reproduzíveis estão em `editorial/checks/`. Os cinco programas usam apenas Python 3 e a biblioteca padrão. Os registos de notação, dependências, fontes e revisão descrevem o âmbito e os limites das verificações.

Nesta sessão, `python3 /tmp/ztm-build-pt.py` compila o livro; `python3 /tmp/ztm-export-chapters.py` actualiza e confere os três PDFs. Os auxiliares, os padrões portugueses do TeX e as imagens de inspecção estão em `/tmp/ztm-editorial-build` e `/tmp/ztm-latex-deps`; são recursos temporários. O registo de versões documenta a preparação do ambiente. As fontes definitivas são `translations/pt/main.tex`, os ficheiros de conteúdo e a bibliografia; a composição normal usa pdflatex e bibtex, com as passagens necessárias para estabilizar as remissões.
