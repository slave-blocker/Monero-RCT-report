# Brief da sessão: capítulo FCMP++

## Prompt para retomar

Continua o objectivo activo de três milhões de tokens e escreve o novo capítulo
português de FCMP++ para *Zero a Monero*. A entrega deve ter cerca de 33 páginas
compiladas e tornar o protocolo compreensível numa primeira leitura, mantendo
a voz, o humor, o ritmo, as metáforas, as setas, os traslados, as notas de
margem e a matemática visual do autor. O capítulo é o último de ``Essenciais'',
imediatamente antes de ``Extensões''.

Começa na relação familiar de Schnorr \(R+cX=sH\). Distingue desde o princípio
três objectos que fontes diferentes chamam \(R\): a raiz pública da árvore, o
compromisso de ocasião da prova de Schnorr e o compromisso de consistência
\(R_{\mathrm{fcmp}}=r_iV+r_jT\). Constrói então, devagar e com um exemplo
numérico ou uma curva de brinquedo, o acumulador e as árvores de curvas de
Matteo Campanelli, Mathias Hall-Andersen e Simon Holmgaard Kamp: compromissos
vectoriais, selecção oculta, re-aleatorização, caminho escondido, alternância
das curvas e verificação da raiz. Descomprime a curta prova de segurança em
intuição verificável, sem reproduzir formalismo que não ajude o leitor.

Introduz apenas a parte do método de divisores principais e reciprocidade de
Weil de Liam Eagen que a implementação FCMP++ usa para provar eficientemente
operações de curva. Mostra primeiro a geometria de rectas, intersecções e somas
de pontos; só depois dá os polinómios e as avaliações necessárias.

Segue a evolução até à composição de Luke ``KayabaNerve'' Parker. Explica por
que a chave de saída histórica \(O=xG\) não oferece o grau de liberdade
necessário, a extensão \(O=xG+yT\) com \(y=0\) para saídas antigas, a folha
\((O,I,C)\), e a re-aleatorização

\[
\widetilde O=O+r_oT,\qquad
\widetilde I=I+r_iU,\qquad
R_{\mathrm{fcmp}}=r_iV+r_jT,\qquad
\widetilde C=C+r_cG.
\]

Separa visualmente a prova de pertença da prova de autorização e ligação.
Deriva as equações da prova SAL a partir do código actual, expandindo os termos
até os factores aleatórios se cancelarem e restar \(L=xI\). Atribui com
precisão o acumulador a Campanelli--Hall-Andersen--Kamp, a maquinaria por
divisores a Eagen, a adaptação e composição FCMP++ a KayabaNerve e as
análises aos respectivos revisores; não atribuas todo o protocolo a uma só
pessoa.

Reserva no total apenas uma ou duas páginas finais para caminhos de código,
migração de saídas antigas, hipóteses de segurança, custos e estado de
implantação. FCMP++ deve ser sempre descrito como próximo protocolo ainda em
desenvolvimento, nunca como consenso activo da v16. Fixa por referências os
commits e revisões realmente explicados. Não alteres os repositórios externos
nem as experiências não confirmadas que já lá estão.

Compila por unidades conceptuais. Mede as páginas reais do capítulo, verifica
as referências e executa `git diff --check`. Entrega o `.tex` e o PDF completo;
não cries um commit sem um pedido separado.

## Fontes locais principais

- `~/curve-trees/` — implementação de referência das Curve Trees; contém uma
  alteração local do utilizador em `relations/tests/curve_tree.rs`.
- `~/Documents/fcmp_ai/2022-596.pdf` — Liam Eagen, divisores principais e
  reciprocidade de Weil.
- `~/Documents/fcmp_ai/2022-510.pdf` — *Bulletproofs++*, apesar do nome opaco
  do ficheiro.
- `~/Downloads/gbp.pdf` — nota da Cypher Stack sobre Generalized Bulletproofs.
- `/tmp/monero-oxide-fcmp/` — ramo `fcmp++` de `monero-oxide`, revisão
  `31c26d96eaadbba910ffe3613ad8b4cf9c598a93`, usado como referência corrente
  da prova de pertença, geradores e SAL. Se a cópia temporária já não existir,
  recria-a a partir do mesmo ramo e fixa a revisão antes de comparar.
- `~/fcmp-plus-plus/` — repositório arquivado, útil apenas para a história;
  não o tratar como autoridade sobre a implementação corrente.
- `~/monero/src/fcmp_pp/` — tipos e preparação das folhas no código Monero.
- `~/Documents/Wolfram/curve trees/` — caderno e rotinas de curva elíptica.

Os repositórios `~/curve-trees` e `~/fcmp-plus-plus` têm alterações locais do
utilizador. São fontes só de leitura: preserva-as e trabalha com cópias limpas
em `/tmp` quando for necessário executar experiências reproduzíveis.
