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
