# Sequência de actualização da edição portuguesa

## Referência técnica

A auditoria inicial foi feita sobre uma fotografia do código Monero datada de
14 de Agosto de 2026. A
programação da rede principal termina na versão 16 do protocolo, activada no
bloco 2 689 608. A presença de código num ramo de desenvolvimento não basta
para o tratar como regra activa.

O texto inglês da segunda edição não recebeu capítulos técnicos novos depois
da tradução portuguesa. Por isso, a revisão parte do texto português e só
recorrerá ao inglês se surgir material posterior identificável.

## Ordem de trabalho

1. **Preliminares, introdução e conceitos básicos.** Fixar a voz, a
   terminologia, a notação e o âmbito técnico da edição. Corrigir a aritmética
   modular, a introdução às curvas elípticas, Schnorr, Ed25519/EdDSA e XOR sem
   pressupor formação especializada.
2. **Assinaturas de Schnorr e assinaturas em anel.** Rever as hipóteses de
   subgrupo e o prefixo de chave; conservar MLSAG como história do formato e
   apresentar CLSAG como a assinatura usada pelas transacções activas.
3. **Endereços e detecção de saídas.** Rever endereços principais,
   subendereços e endereços integrados; acrescentar as etiquetas de vista de
   um byte e separar optimização de leitura da carteira de propriedade de
   privacidade.
4. **Compromissos e provas de intervalo.** Reorganizar os compromissos de
   Pedersen e marcar as provas Borromean e Bulletproof como formatos
   históricos. Conservar e corrigir a exposição portuguesa da Bulletproof
   clássica — incluindo a voz, o traslado, as setas e a derivação recursiva —
   e acrescentar depois uma secção distinta sobre Bulletproof+, com as
   diferenças de protocolo, a agregação e os limites de saídas.
5. **Transacções RingCT.** Substituir `RCTTypeBulletproof2` pelo formato activo
   `RCTTypeBulletproofPlus`; actualizar CLSAG, anéis fixos de 16 membros, duas
   ou mais saídas, etiquetas de vista, limite de `tx_extra` e regras de
   maturação. Manter formatos antigos apenas onde explicam dados históricos.
6. **Lista de blocos, peso e taxas.** Rever a estrutura e validação de blocos,
   a dificuldade, a emissão, o peso dinâmico e as taxas segundo a versão 16.
   As regras de consenso serão distinguidas das escolhas da carteira e do nó.
7. **Novo capítulo: FCMP++.** Produzir cerca de 33 páginas compiladas, como o
   último capítulo da Parte I, ``Essenciais''. Começar na relação de Schnorr
   `R+cX=sH`; construir visualmente as árvores de curvas; introduzir apenas a
   maquinaria de divisores necessária; e chegar à composição de pertença,
   autorização de gasto e ligação de Luke ``KayabaNerve'' Parker. Reservar no
   total uma ou duas páginas finais para código, migração, hipóteses de
   segurança e estado de implantação. Apresentar sempre FCMP++ como protocolo
   futuro ainda em desenvolvimento, não como consenso activo da v16.
8. **Novo capítulo: mineração e RandomX.** Explicar a máquina virtual, o
   programa aleatório, os modos leve e completo, a cache e o conjunto de
   dados, bem como a semente por épocas de 2 048 blocos com atraso de 64.
   Relacionar cada pormenor de consenso com a implementação consultada e
   colocar este capítulo antes de FCMP++, que fecha os ``Essenciais''.
9. **Novo capítulo: difusão de transacções e Dandelion++.** Explicar as fases
   `stem` e `fluff`, épocas, encaminhamento, temporizadores e embargo, além do
   comportamento distinto nas zonas públicas e nas ligações I2P/Tor. Este é
   comportamento de rede implementado, não uma regra de consenso; o capítulo
   ficará também antes de FCMP++.
10. **Provas sobre transacções.** Confrontar as provas de pagamento, chaves de
   transacção e auditoria com as interfaces actuais da carteira e indicar os
   limites de cada afirmação.
11. **Multi-assinaturas.** Rever o capítulo à luz da implementação actual da
    carteira, que continua deliberadamente desactivada por omissão e marcada
    como experimental. Não a apresentar como mecanismo de consenso.
12. **Mercados com garantia e TxTangle.** Conservar o valor conceptual, mas
    rotular com clareza os pressupostos, dependências e natureza experimental;
    retirar qualquer sugestão de que sejam funções correntes do Monero.
13. **Apêndices e referências.** Trocar os exemplos de transacção e bloco por
    exemplos da versão 16, ou marcá-los inequivocamente como históricos;
    reparar referências, índices, rótulos e notas de implementação.

## Assuntos observados, mas não activados

O ramo consultado contém componentes iniciais de FCMP++ e tipos associados a
Carrot. Não existe, nessa revisão, uma versão posterior à v16 programada para a
rede principal, nem validação de transacções FCMP++ nas regras activas. Esse
material entra num capítulo próprio pelo seu valor pedagógico, mas fica
historicamente e tecnicamente separado da descrição da v16. O capítulo fixa a
revisão das fontes e do código que explica, identifica matéria provisória e não
antecipa como definitivas regras cuja activação ainda não tenha sido definida.

## Disciplina de validação

Cada unidade conceptual será compilada antes de se avançar. No fecho de cada
etapa executam-se a compilação integral, a verificação de referências e
`git diff --check`; os ficheiros gerados ficam fora dos repositórios e o clone
Monero permanece estritamente só de leitura.
