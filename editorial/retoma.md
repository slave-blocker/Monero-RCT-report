# Fecho da edição em quatro partes — 17 de Novembro de 2026

O PDF `Zero-to-Monero-2-0-0-pt.pdf` tem **309 páginas**, dentro do limite de 376. O sumário apresenta quatro partes e dezassete capítulos de numeração contínua. O pagamento de Alice, 11 = 7 + 3 + 1, abre o livro e é retomado na construção RingCT. As alterações locais de compromissos e relações entre geradores foram integradas na revisão.

| Capítulo | Páginas físicas | Páginas impressas | Excerto |
|---|---|---|---|
| 10 — Funções e divisores em curvas elípticas | 153–180 | 141–168 | `translations/pt/Divisores-pt.pdf` |
| 11 — Generalized Bulletproofs | 181–195 | 169–183 | `translations/pt/Generalized-Bulletproofs-pt.pdf` |
| 12 — FCMP++ | 196–233, póster na 234 | 184–221, póster sem folio | `translations/pt/FCMP-pt.pdf` |

FCMP++ conserva **38 páginas de texto e uma de póster**. A necessidade dos certificados de divisor e os seus custos desenvolvem-se nas páginas físicas **212–214**, sem impor uma página por secção. Divisores ocupa 28 páginas contínuas. Os apêndices foram conservados, e o índice remissivo ocupa as páginas físicas 303–308.

A compilação estabilizou sem referências ou citações por resolver e com zero avisos de caixas; makeindex aceitou 411 chamadas, sem rejeições nem avisos. Foram conferidas as 28 remissões «ver», as 383 referências numéricas do índice, os 1166 destinos do PDF e as ligações dos três excertos. A exportação compara texto e imagem a 100 dpi nas 82 páginas dos excertos e conserva as remissões para outras partes do livro como ligações ao volume integral.

A inspecção visual percorreu as 309 páginas e ampliou 79, além da leitura detalhada dos certificados e do póster. As verificações algébricas e numéricas estão em `checks/`; `worked-examples.py` reúne as contas do pagamento, dos pesos, das funções sobre F17, da árvore e do resíduo de TxTangle. O âmbito e as fontes estão registados em `revision-log.md` e `protocol-version-ledger.md`. A entrega e o commit são locais.

Os registos seguintes conservam os estados anteriores da edição.

# Edição de 17 de Novembro de 2026

O livro português tem 326 páginas. Generalized Bulletproofs é o capítulo 11, entre Dandelion++ e FCMP++. Os três excertos correspondem às seguintes páginas do livro (numeração impressa).

| Capítulo | Páginas | Excerto |
|---|---|---|
| Divisores e certificados de multiplicação escalar | 28–55 | `translations/pt/Divisores-pt.pdf` |
| Generalized Bulletproofs | 179–193 | `translations/pt/Generalized-Bulletproofs-pt.pdf` |
| Pertença e autorização de gasto em FCMP++ | 194–231, poster na 232 | `translations/pt/FCMP-pt.pdf` |

O capítulo 11 usa a relação de *Fixed Protocol* com compromissos escalares e vectoriais. O exemplo dos dois quadrados segue o valor de um compromisso escalar e a sua máscara até à equação de avaliação, e os operandos até à última dobra. O programa `checks/gbp-F3.py` confere o caso geral, incluindo a especialização com a lista de compromissos escalares vazia usada em FCMP++. O ensaio do divisor sobre uma recta e a verificação da prova exterior têm hipóteses e limites distintos.

A composição estabilizou sem avisos de caixas nem remissões por resolver. O índice aceitou 376 entradas sem avisos. A exportação conferiu por texto e imagem todas as páginas dos três excertos.

# Edição de 16 de Novembro de 2026

Revisão concluída e verificada em 16 de Novembro de 2026. O livro português tem **314 páginas**. Não resta trabalho pendente no âmbito autorizado registado nesta sessão. As fontes, os registos de revisão e os três PDFs finais constituem o resultado. Os commits são locais; não foi feito push.

## Artefactos e extensão

| Artefacto | Estado verificado |
|---|---|
| `Zero-to-Monero-2-0-0-pt.pdf` | Livro completo, 314 páginas. |
| `translations/pt/Divisores-pt.pdf` | 30 páginas, iguais às páginas físicas 41–70 do livro. |
| `translations/pt/FCMP-pt.pdf` | 38 páginas de texto, físicas 194–231, mais o poster A3 na 232. |
| `translations/pt/posters/fcmp-composition/` | Poster novo, com fonte TeX e PDF vectorial. |
| Índice remissivo | 371 entradas aceites; seis páginas, físicas 308–313; remissões verificadas. |

## Âmbito concluído

- Divisores D1–D5 e reconstrução de FCMP++ F1–F8 a partir das fontes primárias, incluindo os certificados, os seus custos e o poster novo.
- Representações canónicas, receitas de hash para pontos, gerador H, domínio das imagens de chave e pergunta DDH.
- Desenvolvimento adicional de CLSAG; verificação de Bulletproofs por duas condições; retirada da repetição localizada na antiga página impressa 109.
- Índices locais, globais e relativos dos anéis, varints, leitura de extra e exemplos completos.
- Notação cumulativa das relações entre geradores, tabelas legíveis, autorização distribuída e mercados com garantia.
- Revisão global de terminologia, exposição afirmativa e separação entre matemática, fontes e pormenores incidentais de implementação.
- Inspecção integral, recompilação, verificação de sumário/índice, exportação dos excertos e fecho em Git.

## Evidência de verificação

A compilação estabiliza com zero avisos de caixas, sem referências ou citações por resolver. Makeindex aceita as 371 entradas sem rejeições nem avisos. Foram conferidos os destinos, páginas e títulos das 293 entradas do sumário, as 296 âncoras de títulos, as 342 referências numéricas do índice e os alvos das 29 remissões «ver». Os excertos foram comparados com o livro por texto e imagem em todas as páginas.

O desenvolvimento matemático e os resultados das verificações reproduzíveis estão em `revision-log.md`, `protocol-version-ledger.md` e `checks/README.md`. Os programas em `checks/` conservam o âmbito das identidades e exemplos verificados; não substituem as hipóteses criptográficas nem constituem uma auditoria da rede em funcionamento.

F7 conserva o modelo de dados fixados antes de desafios ideais, distinguindo a redução de hashes e as tentativas adaptativas de Fiat–Shamir. F8 conserva a hipótese de simulação da distribuição condicionada e o domínio de admissibilidade dos certificados. Estes limites fazem parte da exposição concluída, não são tarefas pendentes.

As notas de fontes retiradas do corpo estão em `source-margin-inventory.md`; o estado das interfaces de multi-assinatura está em `multisig-interface-snapshot.md`. As notas de preparação de F8 são históricas. Os capítulos e figuras substituídos permanecem recuperáveis pelo historial Git.

## Reprodução

`python3 editorial/build-pt.py` compila o livro; `--export` actualiza o PDF principal e chama `editorial/export-chapters.py`, que confere texto e imagem de todas as páginas dos excertos antes de os substituir. O ambiente e as dependências estão descritos em `building.md` e no registo de versões. Os auxiliares e as imagens de inspecção em `/tmp` são temporários; as fontes definitivas e os programas de compilação/exportação estão no repositório.

Os principais marcos anteriores ao fecho foram `f4858c0` (F8), `8d85712` (poster), `ce00840` (receitas de pontos), `0e9b26c` (imagens/DDH), `d5c4060` (CLSAG), `d85fff7` (Bulletproofs), `268e951` (índices das transacções), `951f766` (índice remissivo), `bc897ab` (notação SAL), `6c5a91a` (autorização partilhada) e `c5b236a` (tabelas e destinos). O commit que contém este estado final fecha a revisão transversal e os PDFs definitivos.
