# Auditoria das relações de logaritmo discreto

Data da fotografia: 25 de Agosto de 2026.

Esta nota responde à pergunta: «onde mais aparece uma relação desconhecida,
como \(\gamma=\log_G H\)?»  Não é uma lista de todos os pontos de curva no
código.  É um inventário das famílias de bases cuja relação desconhecida tem
um papel de segurança ou de ocultação no protocolo descrito no relatório e no
FCMP++ em desenvolvimento.

## Primeiro cuidado: três frases diferentes

1. **Relação desconhecida entre bases.** Para pontos públicos \(J,K\) no mesmo
   grupo cíclico existe sempre \(\lambda\) com \(K=\lambda J\). O protocolo
   precisa que ninguém conheça \(\lambda\).
2. **Logaritmo conhecido pelo dono.** Uma chave pública \(P=xG\) foi
   deliberadamente construída com um \(x\) conhecido pelo proprietário. Não é
   um «gerador independente».
3. **Mesmo testemunho em bases diferentes.** Em \(P=xG\) e
   \(I=x\mathcal H_p(P)\), o dono conhece \(x\); a relação entre as bases
   \(G\) e \(\mathcal H_p(P)\) continua desconhecida. A DLEQ/assinatura prova
   que o mesmo \(x\) foi usado.

Confundir as três transforma uma auditoria de parâmetros numa sopa de letras.

## Resultado curto

O \(\gamma=\log_GH\) dos compromissos de montante não está sozinho. A versão
FCMP++ introduz \(T,U,V\) no grupo Ed25519 e famílias inteiras de geradores em
Selene e Helios. A hipótese correcta deixa então de ser «ninguém conhece três
gammas novos» e passa a ser uma hipótese de **logaritmo discreto generalizado**:
é impraticável encontrar uma relação linear não trivial entre os geradores
derivados de forma independente.

Há uma distinção histórica importante. \(\mathcal H_p(P)\), usado nas imagens
de chave, depende da saída e não é um parâmetro estático. Os vectores de bases
dos Bulletproofs são estáticos, determinísticos e indexados, mas não são um
único ponto global nomeado nas equações correntes da transacção. Se «como
\(H=\gamma G\)» quer dizer precisamente uma segunda base fixa, global e com
nome próprio, então \(H\) era de facto o antecedente visível; FCMP++ acrescenta
os três pontos fixos \(T,U,V\).

Em símbolos, para uma família \(J_1,\ldots,J_m\), não se deve conseguir achar
\((a_1,\ldots,a_m)\ne(0,\ldots,0)\) tal que

\[
  a_1J_1+\cdots+a_mJ_m=\mathcal O.
\]

Conhecer qualquer quociente \(\log_{J_i}J_j\) já daria uma relação destas;
com muitas bases, porém, falar apenas de quocientes aos pares esconde a forma
exacta da hipótese.

## Inventário

| Família | Como nasce | Relação que se supõe desconhecida | Papel | Se houver armadilha |
|---|---|---|---|---|
| \(G,H\) (Ed25519) | \(G\) canónico; \(H=8\,\mathrm{decode}(\mathrm{Keccak}(G))\) para este parâmetro histórico | \(H=\gamma G\) | Vinculação dos compromissos \(C=yG+bH\) | Duas aberturas, inflação com moedas próprias; ver `Transactions.tex`, secção `gamma` |
| \(G,T\) | \(T\) por `unbiased_hash_to_ec(Keccak("Monero Generator T"))` | \(T=\tau G\), \(\tau\) desconhecido | Compatibilidade de chaves: \(O=xG+yT\); ocultação/re-randomização FCMP++ | Uma relação conhecida mistura ou reabre as duas coordenadas \(x,y\) |
| \(G,T,U,V\) | \(U,V\) por hash para curva com rótulos FCMP++ separados | Nenhuma relação linear não trivial conhecida entre as quatro bases | Tupla re-randomizada e SAL: \(\widetilde I=I+r_iU\), \(R_{\rm fcmp}=r_iV+r_jT\) | Pode destruir a vinculação entre os cegamentos e abrir testemunhos alternativos para a SAL |
| \(G,\mathcal H_p(P)\) | hash para ponto dependente de cada saída \(P\) | \(\log_G\mathcal H_p(P)\) desconhecido | Imagem de chave CLSAG e DLEQ entre \(P=xG\) e \(I=x\mathcal H_p(P)\) | Relações escolhidas/armadilhadas podem comprometer a prova de igualdade e a ligação |
| \(G_i,H_i,H\) das Bulletproofs+ | cadeia determinística de hash para ponto, separada por índice | Relações lineares entre toda a base vectorial desconhecidas | Vinculação dos compromissos vectoriais e do argumento de produto interno | Uma relação curta permite alterar vectores comprometidos ou satisfazer equações sem testemunha válida |
| \(g,h,\mathbf g,\mathbf h\) de Selene | rejeição com rótulos `Monero Selene ...` | DLOG generalizado na curva Selene | Generalized Bulletproof que agrega as camadas ímpares/pares da árvore | Uma relação linear quebra a vinculação das aberturas e a solidez do circuito |
| \(g,h,\mathbf g,\mathbf h\) de Helios | rejeição com rótulos `Monero Helios ...` | DLOG generalizado na curva Helios | Segundo Generalized Bulletproof da árvore | Mesmo tipo de quebra na outra metade das camadas |
| Inicializadores de hash Selene/Helios e bases vectoriais | hash para curva com `Monero ... Hash Initializer` | O inicializador não deve ter uma abertura conhecida na base vectorial relevante | Separar árvore vazia/prefixo e compromisso dos filhos | Uma abertura conhecida pode permitir colisões estruturais entre listas de filhos |
| Tabelas \(J,2J,4J,\ldots\) do dispositivo por divisores | múltiplos públicos de uma base já fixada | Aqui as relações **são conhecidas por desenho** | Provar que dígitos/escalars recompõem \(kJ\) dentro do circuito | Não é uma cerimónia de geradores; a solidez vem do dispositivo e do PLD da curva exterior |

## O caso histórico \(H\)

O código Monero actual conserva cinco pontos globais em
`src/crypto/generators.cpp`. O comentário e a função de reprodução fixam:

```text
G = gerador Ed25519 canónico
H = 8 * decode(Keccak256(G))
T = unbiased_hash_to_ec(Keccak256("Monero Generator T"))
U = unbiased_hash_to_ec(Keccak256("Monero FCMP++ Generator U"))
V = unbiased_hash_to_ec(Keccak256("Monero FCMP++ Generator V"))
```

Esta é uma fotografia do ramo principal C++ na revisão
3646f648db57f60cca86430e25a635d19fa9b92a. Os bytes de \(U,V\) nessa
integração parcial ainda diferem dos bytes no ramo FCMP++ de monero-oxide
citado abaixo. Não se deve montar um conjunto de parâmetros híbrido com
pontos das duas revisões. A função de segurança de \(U,V\) é a mesma no
inventário; a instanciação exacta pertence a uma única fotografia coerente
do protocolo.

Para \(H\), «hash para ponto» é a construção histórica concreta acima; não se
deve reescrevê-la como se utilizasse exactamente a rotina moderna usada para
\(T,U,V\). O efeito desejado é o mesmo: o valor é reproduzível por qualquer
pessoa, mas não há uma pessoa que tenha escolhido primeiro o escalar e depois
publicado o ponto.

O relatório já deriva o ataque completo e a extracção

\[
 \gamma=(y'-y)(b-b')^{-1}\pmod l
\]

a partir de duas aberturas de \(C=yG+bH\). Esse é o modelo pedagógico para as
restantes famílias, embora as consequências concretas não sejam sempre
«fabricar montante».

## \(T\): a porta de compatibilidade

FCMP++ representa a chave de saída como

\[
  O=xG+yT.
\]

Uma saída histórica tem \(y=0\), portanto continua a ser \(O=xG\). Protocolos
futuros podem usar a segunda coordenada sem mudar o formato conceptual da
tupla. Esta flexibilidade só é vinculante se a relação entre \(G\) e \(T\)
não for conhecida. Se \(T=\tau G\) com \(\tau\) conhecido, então

\[
  xG+yT=(x+y\tau)G.
\]

e cada abertura \((x,y)\) ganha imediatamente muitas descrições alternativas.
Isto não significa que \(T\) seja um segundo «gerador do grupo» no sentido de
gerar outro subgrupo: o grupo é cíclico, portanto \(T\) é algum múltiplo de
\(G\). «Independente» significa somente que esse múltiplo é
computacionalmente desconhecido.

## \(U,V\): dois cegamentos que têm de conversar sem se denunciarem

A re-randomização FCMP++ usa

\[
\begin{aligned}
 \widetilde I &= I+r_iU,\\
 R_{\rm fcmp} &= r_iV+r_jT.
\end{aligned}
\]

O mesmo \(r_i\) aparece nas duas linhas. A prova de pertença confirma que a
tupla escondida foi obtida de uma saída real com essa consistência; a SAL usa
\(R_{\rm fcmp}\) sem revelar \(r_i\). O papel de \(U\) e \(V\) não é apenas
«mais entropia». Eles colocam o mesmo segredo em bases separadas para que uma
prova consiga ligá-lo algebricamente sem abrir a saída.

Por isso a hipótese útil é conjunta para \(G,T,U,V\). Escrever três símbolos

\[
 T=\tau G,\qquad U=\upsilon G,\qquad V=\nu G
\]

é legítimo matematicamente, mas induz em erro se parecer que a segurança se
resume a esconder três números independentes. Uma combinação conhecida, por
exemplo \(aG+bT+cU+dV=\mathcal O\), já pode criar uma segunda abertura dos
compromissos multibase mesmo sem entregar isoladamente \(\tau,\upsilon,\nu\).

## Hash para ponto por saída: \(\mathcal H_p(P)\)

Na CLSAG e nos seus antepassados, a imagem de chave tem a forma

\[
 I=x\mathcal H_p(P),
 \qquad P=xG.
\]

O \(x\) é conhecido pelo dono e é precisamente o testemunho cuja igualdade se
prova nas duas bases. O desconhecido é a relação entre as bases. Como
\(\mathcal H_p(P)\) depende de \(P\), existe uma família potencialmente enorme
de relações

\[
  \eta_P=\log_G\mathcal H_p(P).
\]

Não se armazenam «milhões de gammas». O modelo de oráculo/hash para grupo diz
que cada ponto válido derivado de uma entrada nova se comporta como uma base
sem relação conhecida. A validação de subgrupo e identidade continua
essencial; uma codificação mal validada pode quebrar a frase antes de o PLD
entrar em cena.

## Geradores vectoriais das Bulletproofs e Generalized Bulletproofs

Uma prova de produto interno não trabalha apenas com \(G\) e \(H\). Compromete
vectores completos:

\[
 C=rh+\langle\mathbf a,\mathbf g\rangle
       +\langle\mathbf b,\mathbf h\rangle.
\]

Se alguém conhece coeficientes não todos nulos que somem os geradores a zero,
consegue alterar uma abertura ao longo dessa relação sem mudar \(C\). É a
versão multidimensional do truque de \(\gamma\). Por isso a frase de segurança
é «DLOG generalizado» para a família inteira, não apenas
\(\log_g h\) desconhecido.

No código FCMP++ de 18 de Agosto de 2026, cada uma das curvas Selene e Helios
recebe:

```text
g       <- hash("Monero <Curva> G")
h       <- hash("Monero <Curva> H")
g[i]    <- hash("Monero <Curva> G <i>")
h[i]    <- hash("Monero <Curva> H <i>")
hashInit<- hash("Monero <Curva> Hash Initializer")
```

O «hash» acima é amostragem por rejeição para uma codificação canónica,
não-identidade e válida na curva. Os rótulos são separadores de domínio. Não
há configuração confiada e não existe uma «toxic waste» que uma cerimónia
deva destruir; a verificabilidade dos parâmetros é precisamente a propriedade
transparente herdada de Curve Trees.

## Inicializador de hash não é mero enfeite

Os nós actuais são construídos como

\[
 C_{\rm nó}=J_{\rm init}+\sum_i v_iJ_i.
\]

O ponto inicial separa a função que compromete uma lista de filhos de uma soma
vectorial crua e evita que o vector todo zero codifique simplesmente a
identidade. Ele também pertence à constelação de pontos derivados sem
armadilha. A hipótese exacta necessária depende da redução de segurança da
construção completa; operacionalmente, deve ser tratado como mais uma base
sem abertura conhecida na família usada por esse hash.

## Relações deliberadamente conhecidas

Nem toda igualdade entre pontos é suspeita. O dispositivo de logaritmo
discreto prepara uma tabela

\[
 J,\;2J,\;4J,\ldots,2^{n-1}J.
\]

Estas relações são públicas e necessárias: os dígitos do escalar escolhem uma
combinação que resulta no ponto alegado. A novidade de Eagen não consiste em
fingir que \(2J\) é independente de \(J\); consiste em comprimir, com divisores
e desafios aleatórios, a verificação de que os pontos/dígitos escolhidos somam
correctamente.

O mesmo vale para uma chave pública \(P=xG\), para \(xP\), ou para um nonce
\(R=rH\): são relações construídas por quem conhece o escalar e usadas como
declarações/testemunhos. A auditoria de «relações desconhecidas» não deve
marcá-las como falhas.

## Locais de código verificados

### Monero

- Repositório local: `~/monero`
- revisão: `3646f648db57f60cca86430e25a635d19fa9b92a`
- `src/crypto/generators.cpp`: bytes, reprodução e acesso a \(G,H,T,U,V\)
- `src/crypto/generators.h`: interface pública dos cinco pontos
- `src/fcmp_pp/curve_trees.cpp`: transformação de saídas em tuplas e construção
  incremental dos nós

### monero-oxide / FCMP++

- cópia temporária: `/tmp/monero-oxide-fcmp`
- ramo: `fcmp++`
- revisão: `31c26d96eaadbba910ffe3613ad8b4cf9c598a93`
- `monero-oxide/ringct/fcmp++/generators/src/lib.rs`: \(U,V\), famílias
  Selene/Helios e inicializadores
- `monero-oxide/ringct/fcmp++/src/lib.rs`: ligação dos parâmetros Ed25519,
  Selene e Helios
- `monero-oxide/ringct/fcmp++/src/sal/mod.rs`: uso conjunto de \(G,T,U,V\)
- `crypto/fcmps/ec-gadgets/src/dlog.rs`: tabelas de múltiplos e verificação por
  divisores
- `crypto/fcmps/src/tree.rs`: crescimento e poda dos compromissos vectoriais

## O que deve entrar no capítulo

O corpo pedagógico deve mostrar:

1. \(\gamma=\log_GH\) como caso unidimensional já conhecido;
2. a passagem para «nenhuma relação linear» em \(G,T,U,V\);
3. a razão específica de cada uma das bases em
   \(\widetilde O,\widetilde I,R_{\rm fcmp},\widetilde C\);
4. a família \(g,h,\mathbf g,\mathbf h\) das duas curvas como hipótese da
   prova vectorial;
5. uma caixa curta distinguindo relações desconhecidas de relações
   deliberadamente conhecidas.

Os pormenores de bytes, revisões e caminhos ficam na nota final de código, não
no percurso principal.

## Questões que esta auditoria não resolve sozinha

- Derivar pontos por hash elimina uma pessoa obviamente detentora de uma
  armadilha, mas a segurança final ainda depende da função de hash, do mapa
  para curva, dos separadores de domínio e da validação de pontos.
- Uma hipótese de DLOG não substitui a prova de conhecimento nem a solidez do
  circuito. Um circuito pode usar parâmetros honestos e ainda esquecer uma
  restrição.
- «Não conhecemos uma relação» não é prova de que nenhuma relação curta
  exista; os modelos e reduções formalizam como os pontos derivados são
  tratados.
- A segurança pós-quântica não está incluída: um computador quântico grande
  que execute Shor calcula estas relações. A composição FCMP++ procura
  forward secrecy em sentido específico, mas continua baseada em curvas
  elípticas para segurança clássica.
