# Registo da revisão

## Objectivo activo

Revisão autorizada em 10-11-2026, inicialmente com orçamento de 5 000 000 de tokens. Retomada em 16-11-2026 com novo objectivo de 1 000 000 de tokens, abrangendo todo o âmbito preservado em `retoma.md`. Reescrever divisores e FCMP++ e executar todas as intervenções abaixo. Uma unidade semântica por ciclo, com compilação e inspecção. Preservar a progressão apreciada em SAG e bLSAG.

## Lista de intervenções

- [x] Divisores: reescrita integral e paginação contínua.
- [x] FCMP++: reescrita integral a partir das fontes; mapa da composição antes das equações completas; paginação contínua; 38 páginas de texto.
- [x] FCMP++: IPA, Generalized Bulletproofs, SAL e prova de intervalo; contagem condicionada de argumentos.
- [x] FCMP++: construir e inspeccionar o novo poster.
- [x] Explicar a receita de \(H_p\) e reproduzir a obtenção do gerador fixo \(H\).
- [x] Página impressa 55: desenvolver a falha de validação das imagens de chave e a investigação publicada sobre a ausência de exploração.
- [x] Página 57: retirar o parágrafo «Uma variante permite tornar ligáveis…».
- [x] Página 59: ensinar a pergunta decisional de Diffie–Hellman antes de a nomear.
- [ ] Explicar «canónico» na primeira utilização relevante e incluir o termo no índice.
- [x] Página 62: «Especialização usada por Monero»; acrescentar duas páginas de explicação de CLSAG.
- [x] Página 91: simplificar a apresentação das duas verificações de Bulletproofs; retirar do percurso principal os resíduos e a combinação ponderada, preservando as duas condições matemáticas.
- [x] Página 109: eliminar a página redundante sobre o tamanho da prova de intervalo, conservando a exposição útil na secção de espaço.
- [ ] Página 111: desenvolver a representação uniforme dos membros do anel e a posição secreta por entrada.
- [ ] Acrescentar três páginas sobre índices absolutos, key_offsets, reconstrução dos anéis e estrutura de tx_extra. Explicitar que key_offsets pertence a vin.
- [ ] Índice remissivo alfabético no fim, incluindo símbolos, siglas, sinónimos e páginas de explicação.
- [ ] Uniformizar «de/por/em Monero» e «lista de blocos» na prosa portuguesa.
- [x] Nota de rodapé em FCMP++ sobre «cadeia» e «lista de blocos», no tom pedido.
- [ ] Rever a exposição afirmativa ao longo do livro, conservando condições e hipóteses matemáticas.
- [x] Registar no AGENTS.md as preferências de exposição afirmativa, terminologia e secções de extensão natural.
- [ ] Compilação integral, referências, índice, exame visual e actualização dos PDFs do livro e dos capítulos autónomos.
- [ ] Criar o commit pedido, reunindo o resultado final verificado da revisão.

## Unidade D1 — funções, zeros, multiplicidades e pólos

Estado: concluída e verificada.

Âmbito: substituir a abertura e as cinco primeiras secções de divisores por um percurso contínuo que prepare a definição de divisor. Pré-requisitos: aritmética modular, corpos finitos e grupo elíptico do capítulo 2. Destino: registo formal de lugares e ordens, seguido da ponte para a soma de pontos.

Fontes inspeccionadas: Eagen, introdução e secções 2–3; interfaces e construção de rectas em `crypto/divisors`. Referência de estilo: secções de SAG e bLSAG indicadas pelo leitor. Manter as etiquetas referenciadas pelo restante livro e o exemplo em módulo 17 durante a reescrita incremental.

Resultado: a abertura e as antigas cinco secções deram lugar a uma introdução e três secções contínuas: funções sobre a curva, multiplicidades e pólos. Desenvolveram-se a redução polinomial, a expansão local da tangente e as coordenadas projectivas que dão as ordens de x e y no infinito. As etiquetas antigas foram conservadas. As restantes secções do capítulo aguardam a sua unidade própria.

Validação: as contas em módulo 17 foram reproduzidas por cálculo inteiro independente (regularidade, factorização, duplicação, triplicação e dois primeiros coeficientes da expansão local). Compilaram-se o livro de referência e a versão revista com hifenização portuguesa; as referências estabilizaram sem citações ou etiquetas indefinidas. A unidade não introduziu avisos de caixas tipográficas, e os avisos restantes coincidem com os da referência. Inspeccionaram-se imagens das páginas físicas 40–45 e corrigiram-se as quebras junto de uma equação e da abertura da secção dos pólos.

Artefactos actualizados: `Zero-to-Monero-2-0-0-pt.pdf`, com 297 páginas físicas, e `translations/pt/Divisores-pt.pdf`, com 21 páginas. O excerto foi produzido com `pdfpages`; a extracção de texto confirmou que coincide com as páginas físicas 40–60 do livro. A reescrita integral dos divisores continua nas unidades seguintes.

## Unidade D2 — do registo formal ao certificado

Estado: concluída e verificada.

Reescrever o conjunto que começa na definição de divisor e termina no certificado numérico de Q = 3P. Explicar separadamente a soma formal, o grau e a soma no grupo; construir o divisor de uma recta e da razão recta/vertical; justificar o critério de divisor principal e trabalhar a função testemunha completa. Preservar os pré-requisitos construídos em D1, retirar os blocos de exercícios e dar às secções extensão natural. Conferir a função reduzida por aritmética no corpo antes de compilar e inspeccionar o novo conjunto.

Fontes novamente conferidas: Eagen, secções 2.1–3.1.1; `crypto/divisors/src/divisor.rs`, em particular a representação por dois polinómios, a multiplicação reduzida e a eliminação dos factores verticais.

Resultado: seis secções com quebras de página impostas deram lugar a quatro secções contínuas. A exposição distingue o registo formal, o grau inteiro e a soma dos pontos. A norma permite demonstrar o equilíbrio entre zeros e pólos; a redução por rectas e a prova de que toda a função regular na parte afim admite um representante polinomial completam o critério de divisor principal. O certificado de Q = 3P inclui a construção, a redução da função testemunha, a expansão local que demonstra o zero triplo e a factorização da norma. O conjunto ocupa parte das páginas físicas 45–51. A abertura D1 foi conservada; no material posterior, ajustou-se apenas uma remissão de «página anterior» para «secção anterior», necessária à paginação contínua.

Validação: as contas do exemplo em módulo 17 foram reproduzidas independentemente, incluindo os produtos polinomiais, a norma e o coeficiente do zero triplo. Conferiram-se as duas direcções do critério, os casos da identidade e dos pontos inversos, as hipóteses sobre o corpo e as etiquetas usadas a jusante. A compilação integral estabilizou com referências e citações resolvidas; os avisos tipográficos coincidem com os de D1. Inspeccionaram-se as imagens das páginas 45–51 e corrigiram-se um título demasiado largo e uma equação que atravessava a mudança de página. O diff confirma a conservação do material exterior à unidade, ressalvada a remissão referida.

Artefactos actualizados: livro português com 297 páginas e capítulo autónomo dos divisores com 21 páginas, correspondentes às páginas físicas 40–60 do livro. A comparação do texto do excerto confirmou a correspondência página a página.

## Unidade D3 — representação compacta e limites da função

Estado: concluída e verificada.

Desenvolver as representações do escalar, o divisor de tamanho controlado e os limites dos graus de f₀ e f₁. Partir do certificado já construído e terminar antes da avaliação de funções sobre divisores. Conferir nas fontes as condições sobre dígitos, multiplicidades, identidade, normalização e função não nula. A avaliação e as verificações aritméticas constituirão a unidade seguinte. A reescrita de FCMP++ e as restantes intervenções permanecem na lista activa.

Fontes inspeccionadas nesta unidade: Eagen, secções 3–4.2; `ScalarDecomposition` e `scalar_mul_divisor` em `crypto/divisors/src/lib.rs`; representação, tabela e verificação em `crypto/fcmps/ec-gadgets/src/dlog.rs`; secção de prova de logaritmo discreto da especificação FCMP++. A construção da testemunha usa multiplicidades inteiras com soma fixa; o circuito aceita uma representação consistente sem impor bits. A exposição distinguirá estes níveis. A normalização de um coeficiente requer que ele seja não nulo na família em causa.

Resultado: as duas secções anteriores deram lugar a três secções contínuas, cobrindo parte das páginas físicas 51–57. A primeira constrói a tabela de duplicações e o divisor escolhido pelos bits. A segunda demonstra a existência de multiplicidades não negativas de soma fixa para cada escalar não nulo, incluindo os representantes pequenos, e trabalha o exemplo de ordem 19 sobre o corpo de 17 elementos. A terceira deduz os limites dos graus, a dimensão exacta do espaço da função, a suficiência das condições de multiplicidade e a normalização. A representação da testemunha e a futura verificação no corpo são apresentadas separadamente. As etiquetas anteriores foram preservadas.

Validação: conferiram-se as duplicações, a ordem do ponto, as multiplicidades, a recta testemunha e a sua normalização por aritmética independente. A construção de multiplicidade fixa foi conferida para 6 282 escalares, abrangendo todas as ordens primas ímpares de 3 a 257; os pesos e dimensões foram conferidos de d = 1 a d = 257. A demonstração escrita estabelece o caso geral. O diff preserva todo o texto anterior e posterior à unidade. O preâmbulo recebeu apenas `needspace`, já disponível no ambiente, para conservar espaço suficiente junto de dois títulos e de uma tabela; estas reservas são condicionais à posição na página. A compilação integral estabilizou com referências e citações resolvidas, e os avisos tipográficos coincidem com os de D2. Inspeccionaram-se as páginas 51–57, incluindo as versões finais das quebras ajustadas.

Artefactos actualizados: livro português com 300 páginas e capítulo autónomo dos divisores com 24 páginas, correspondentes às páginas físicas 40–63. A extracção com `pdfpages` foi conferida página a página contra o livro.

## Unidade D4 — avaliações e reciprocidade

Estado: concluída e verificada.

Reescrever a avaliação de funções sobre divisores, a contribuição local dos pólos comuns e a identidade do resultante que permite usar uma recta desafiada. Partir das funções de tamanho limitado de D3 e preparar a derivada logarítmica. Preservar e justificar sinais, coeficientes líderes, hipóteses sobre suportes e escolhas dos pontos de desafio. As condições de solidez e a tradução final para relações aritméticas serão tratadas na unidade seguinte. As restantes intervenções do objectivo continuam pendentes.

Fontes inspeccionadas: Eagen, secção 3.2, e amostragem dos desafios em `ec-gadgets/src/dlog.rs`; para a forma geral do símbolo local, Osipov e Zhu, *Algebra & Number Theory* 5(3), introdução e fórmula (1-1). A referência de Osipov e Zhu foi acrescentada à bibliografia. As condições da distribuição dos desafios e a contagem das tangentes ficaram registadas no inventário de fontes para a análise de solidez em D5.

Resultado: três secções deram lugar a quatro secções contínuas, cobrindo parte das páginas físicas 57–63. A avaliação de funções sobre divisores começa com uma conta completa sobre F₁₇. As unidades locais justificam o símbolo e a contribuição do ponto no infinito; desta resultam o sinal e os coeficientes iniciais do resultante. A identidade específica com uma recta recebe uma demonstração própria, por factorização cúbica, troca de produtos entre rectas e composição multiplicativa das funções construídas em D2. A norma na direcção da recta prepara a derivada logarítmica. O desafio público é apresentado depois dos dados a fixar e inclui a construção dos três encontros a partir de dois pontos, com as hipóteses necessárias.

Validação: conferiram-se independentemente a avaliação de divisores de suportes disjuntos, a contribuição do infinito, a troca entre rectas e verticais e o exemplo final. A enumeração das rectas com três encontros racionais distintos sobre F₁₇ permitiu ainda 252 verificações da identidade, cobrindo duas funções testemunhas, três escalas e as 42 rectas. A demonstração escrita estabelece o caso geral e conserva as multiplicidades. O diff confirma que todo o material anterior e posterior à unidade foi conservado, bem como as etiquetas existentes. A compilação integral estabilizou com referências e citações resolvidas; os avisos tipográficos coincidem com os de D3, descontada a mudança dos números de linha. Inspeccionaram-se as páginas 57–63 e ajustou-se a reserva de espaço antes de uma conta para manter a introdução junto das equações.

Artefactos actualizados: livro português com 303 páginas e capítulo autónomo dos divisores com 27 páginas, correspondentes às páginas físicas 40–66. A extracção com `pdfpages` foi conferida página a página contra o livro.

## Unidade D5 — derivada logarítmica e verificação do certificado

Estado: concluída e verificada. As unidades D1–D5 completam a reescrita do capítulo dos divisores.

Reescrever as quatro secções restantes, partindo da norma na direcção da recta. Ensinar a derivação formal e calcular a derivada ao longo da curva, trabalhar a identidade numérica completa e explicitar as condições aritméticas que ligam a função aos dados prescritos. Conferir nas fontes as hipóteses de solidez, a representação das multiplicidades no corpo, os denominadores e o papel da normalização. Distinguir a testemunha construída da relação efectivamente verificada, e explicar como a prova maior conserva os dados secretos e liga as suas partes. Fechar com os custos pertinentes e a dependência que FCMP++ utilizará. Retirar os exercícios e as quebras de página impostas ainda presentes nesta parte. Compilar, inspeccionar, conferir as contas e actualizar os dois PDFs antes de passar à reescrita de FCMP++.

Fontes inspeccionadas: Eagen, secções 3.2 e 4.1–4.2; especificação FCMP++, secção «Discrete Log Proof»; construção da testemunha e relações do circuito nas fontes de Monero-oxide. Duas revisões independentes conferiram a extracção das multiplicidades, a distribuição dos desafios, os custos e as contas do exemplo. A derivação probabilística usa um modelo uniforme explicitamente definido, distinto da amostragem concreta da implementação; as diferenças e as hipóteses de normalização ficaram registadas no inventário de fontes para FCMP++.

Resultado: quatro secções contínuas, nas páginas físicas 63–69, completam a passagem da norma ao certificado aritmético. A derivada formal é definida antes das regras de produto, quociente e composição; o exemplo em módulo 17 inclui todos os numeradores, denominadores, inversas e razões. A comparação das fracções simples recupera o escalar através de um levantamento inteiro único em [−1,d], incluindo a coincidência entre −W e um ponto da tabela. A contagem dos desafios fornece um limite explícito de erro. A última secção explica os sete produtos secretos da relação, os dez produtos da variante com inversões adicionais e os custos separados da função, dos dados comprometidos e da prova exterior. Foram eliminados os exercícios e as três quebras de página restantes; o capítulo inteiro tem agora paginação contínua.

Validação: a identidade da derivada logarítmica foi reproduzida em 52 casos admissíveis, cobrindo as duas funções do exemplo e as rectas simples da curva sobre F₁₇. A enumeração confirmou as 42 rectas, os 252 pares ordenados regulares e o limite da sua contagem. Conferiram-se também o levantamento com coeficiente −1, a contagem dos coeficientes e os sete/dez produtos. A demonstração geral e o limite probabilístico foram revistos separadamente. O diff conserva todo o prefixo D1–D4 e todas as etiquetas existentes. A compilação integral terminou com referências e citações resolvidas e sem novos avisos tipográficos. Inspeccionaram-se as páginas 63–69 e corrigiu-se uma citação que ficara isolada no início de página.

Artefactos actualizados: livro português com 306 páginas e capítulo autónomo dos divisores com 30 páginas, correspondentes às páginas físicas 40–69. A extracção com `pdfpages` foi conferida página a página contra o livro. A cópia de comparação para a próxima unidade ficou em `/tmp/ztm-D5-preserved`.

## Unidade F1 — mapa da construção e relação de FCMP++

Estado: concluída e verificada. A abertura nova está instalada; o capítulo de FCMP++ permanece em construção até às 38 páginas de texto pedidas.

Iniciar a reconstrução de FCMP++ a partir das fontes primárias, com uma primeira unidade de 3–6 páginas. Estabelecer o problema, a declaração pública, a testemunha secreta e o mapa das propriedades e das subprovas antes das equações completas. Conferir a composição de pertença, autorização, ligação ao gasto, imagem de chave, compromissos e provas de intervalo. Preparar uma estrutura nova para as 38 páginas de texto pedidas, reservando o desenvolvimento dos certificados de divisores e dos seus custos. A prosa, os exemplos, os esquemas e a sequência do capítulo antigo não servem de modelo. Os conceitos já ensinados nos divisores constituem os pré-requisitos; as relações concretas e as hipóteses da construção seleccionada serão estabelecidas pelas fontes.

Fontes inspeccionadas: especificação de Parker, relações e conjunção optimizada na análise Cypher Stack, tipos e transcritos da implementação Rust, provas dos dois circuitos e construção das folhas na cópia C++ fixa. Consultou-se também a apresentação primária de Curve Trees no ePrint. Duas revisões independentes conferiram a relação composta, a ligação dos transcritos, a contagem dos argumentos e a separação entre as regras exteriores e as garantias das provas.

Resultado: uma introdução e quatro secções novas, em seis páginas. A exposição começa pelo conjunto público e pela escolha secreta; define a relação da entrada e a apresentação mascarada; um esquema novo mostra a ligação entre pertença e SAL. O mapa distingue os dois argumentos de pertença, o argumento SAL de dimensão um por entrada e as provas de intervalo, com a fórmula 2 + n + r e os casos de uma e duas entradas. Conservou-se I como imagem de chave e introduziu-se J como base. A nota terminológica pedida foi incluída na abertura. A formação exacta das folhas e os protocolos completos ficam para as unidades seguintes.

O capítulo antigo estava inalterado face a HEAD e foi integralmente substituído no ficheiro TeX; a sua recuperação faz-se pelo Git. O poster antigo foi retirado da composição, para receber uma substituição coerente com a nova exposição. Esta opção deixa o capítulo deliberadamente parcial durante a reconstrução, sem intercalar prosa antiga. O objectivo final continua a ser 38 páginas de texto, além do novo poster.

Validação: conferiram-se directamente as quatro relações da apresentação, a conservação do montante e o cancelamento do termo da imagem. A contagem dos argumentos foi confrontada com as chamadas de prova dos dois circuitos, de SAL e da prova agregada de intervalo. O diff conserva as fontes do capítulo dos divisores e as restantes fontes de conteúdo; as remissões exteriores dependem apenas da etiqueta do capítulo, que foi preservada. A compilação integral terminou com referências e citações resolvidas e sem novos avisos tipográficos. Inspeccionaram-se as seis páginas, o esquema e a entrada bibliográfica ajustada; aumentou-se o espaço das setas no esquema e corrigiu-se a composição dos caminhos da fonte citada.

Artefactos actualizados: livro em revisão com 272 páginas; excerto parcial de FCMP++ com seis páginas, correspondentes às páginas físicas 190–195; divisores com as mesmas 30 páginas de texto, agora nas páginas físicas 39–68. Os dois excertos foram conferidos página a página contra o livro. A redução temporária da extensão resulta da substituição integral do capítulo antigo pela primeira unidade nova. O auxiliar `/tmp/ztm-export-chapters.py` actualiza ambos os excertos e o livro.

## Unidade F2 — o produto secreto e a autorização SAL

Estado: concluída e verificada. A autorização está desenvolvida; o capítulo completo permanece em reconstrução.

Partir do produto x r_J e construir a conjunção optimizada do argumento de produto de dimensão um com as relações de Schnorr. Explicar o significado dos pontos enviados e das respostas antes das equações de verificação, trabalhar o desenvolvimento quadrático e a consistência das aberturas, e fixar exactamente o contexto do desafio. Usar I como imagem e J como base em todas as equações, mantendo a correspondência das fontes nas notas. Conservar a distinção entre a relação extraída de SAL e a relação obtida depois de compor com a pertença. Visar até seis páginas contínuas, com as contas necessárias resolvidas, compilação e inspecção do PDF.

Resultado: quatro secções contínuas abrangem as páginas físicas 195–199. O compromisso P reúne factores e produto, a diferença D liga-o à apresentação, e a expansão quadrática conduz às mensagens e às quatro verificações. O transcrito apresenta a sequência completa dos dados públicos. A extracção de Schnorr e a comparação das aberturas estabelecem a ligação à saída de que a pertença fornece testemunha; a simulação e a sua bijecção explicam a ocultação. As secções acompanham o argumento e atravessam páginas naturalmente. O prefixo F1 foi integralmente conservado.

Fontes e revisão: conferiram-se a conjunção optimizada da análise Cypher Stack, a prova e a verificação Rust, o transcrito da entrada e o artigo primário de Bulletproofs+. Duas conferências independentes verificaram sinais, nomes, partilha de respostas, hipóteses e âmbito da extracção e da simulação. Corrigiram-se na exposição três pontos de precisão: amostragem uniforme explícita dos primeiros nonces, acesso do extractor a respostas alternativas e âmbito da igualdade de distribuições para a testemunha comum.

Validação: /tmp/ztm-check-sal-F2.py reproduz as contas sobre a curva do exemplo, de ordem 19 sobre F₁₇. Quarenta conjuntos de dados e todos os dezanove desafios dão 760 verificações de completude, 760 extracções lineares, 760 simulações com recuperação dos nonces e 760 testes da dependência do desafio com imagem não nula. Estas contas conferem a álgebra; as garantias criptográficas conservam as hipóteses e as demonstrações próprias. O diff confirma que os divisores e o preâmbulo não mudaram nesta unidade; a bibliografia recebeu apenas a referência primária de Bulletproofs+. A compilação integral estabilizou com todas as remissões e citações resolvidas e os mesmos 164 avisos tipográficos de F1. Inspeccionaram-se as cinco páginas e a entrada bibliográfica.

Artefactos: livro em revisão com 276 páginas; excerto parcial de FCMP++ com dez páginas, correspondentes às páginas físicas 190–199; divisores com trinta páginas, nas páginas físicas 39–68. Os excertos são conferidos contra o livro pelo auxiliar de exportação. O alvo de FCMP++ continua a ser 38 páginas de texto e um poster novo; a extensão será ajustada pela matéria que falta, conservando paginação contínua.

## Unidade F3 — compromissos vectoriais e Generalized Bulletproofs

Estado: concluída e verificada.

Ensinar a ponte entre compromissos vectoriais públicos e as relações aritméticas sobre as suas aberturas. Partir das operações já conhecidas de Pedersen e produto interno; definir o circuito e a declaração exacta que a extensão prova, incluindo os valores públicos, vectores secretos, bases e máscaras. Conferir a construção nos relatórios matemáticos fixos e na implementação, antes de fixar notação e equações. Desenvolver uma unidade de até seis páginas contínuas, preparando a alternância de curvas e a abertura dos caminhos. Conservar a distinção entre esta maquinaria e o argumento de produto de dimensão um de SAL. Compilar, inspeccionar o PDF e actualizar os registos e excertos antes de passar à árvore.

Resultado: quatro secções contínuas nas páginas físicas 200–204. A primeira liga um circuito pequeno às coordenadas comprometidas e define a declaração geral pertinente. A segunda deduz os pesos, o limite da combinação desafiada e o coeficiente t_d dos polinómios, com uma conta completa para v = u² + 3u. A terceira constrói a avaliação comprometida, o ponto público P_ar e a relação do IPA. A última explica a ordem dos desafios, a ocultação exterior e a interface com os circuitos da árvore. A máscara de S passou a ρ_S para conservar ρ como raiz.

Fontes: inspeccionaram-se os três relatórios matemáticos locais, o protocolo fixo de Janeiro de 2026, a implementação Rust e a proposta de referência de Curve Trees. Duas revisões independentes conferiram a relação ampliada, as dimensões, os graus, o exemplo, as duas verificações e a ordem do transcrito. Acrescentou-se uma entrada bibliográfica precisa para o protocolo fixo e actualizou-se a remissão correspondente na abertura F1. O título liga directamente à cópia fixa; o historial das versões e os lapsos tipográficos das fontes ficaram nas notas.

Validação: /tmp/ztm-check-gbp-F3.py verifica 240 coeficientes distinguidos, 720 reconstruções do ponto público, 720 verificações polinomiais e 720 relações de entrada do IPA, sobre F₁₀₁ e F₆₅₅₃₇, com zero a quatro compromissos, várias dimensões e componentes direitas arbitrárias. O exemplo recebeu 600 verificações algébricas. Conferiu-se ainda o limite da combinação em 180 polinómios não nulos sobre todos os cem pares de desafios não nulos de F₁₁. As demonstrações e hipóteses criptográficas permanecem distintas destes testes de contas.

A compilação integral estabilizou com remissões e citações resolvidas e os mesmos 164 avisos tipográficos de F2. Inspeccionaram-se as cinco páginas, a transição anterior e a nova referência. Uma reserva de espaço mantém a introdução da primeira secção junto do título; as restantes quebras acompanham o texto. Afinou-se o fecho para evitar uma página quase vazia. O preâmbulo, os divisores e o texto de F1–F2 foram conservados, salvo a remissão bibliográfica já referida.

Artefactos: livro em revisão com 281 páginas; FCMP++ parcial com quinze páginas, correspondentes às páginas físicas 190–204; divisores com trinta páginas, correspondentes às páginas físicas 39–68. Os dois excertos foram conferidos contra o livro. A reconstrução prossegue para as 38 páginas de texto e o poster novo.

## Unidade F4 — ciclo de curvas, folhas e caminhos

Estado: concluída em 10 de Novembro de 2026.

Construir a representação pública do conjunto a partir da interface de compromissos de F3. Fixar os corpos de coordenadas e de escalares de Edwards25519, Selene e Helios; explicar a alternância e conferir as equações e ordens pertinentes. Desenvolver a formação exacta das folhas, incluindo o hash da chave original e a projecção das componentes com torção, e os compromissos que resumem os ramos. Mostrar como um caminho secreto selecciona um elemento e liga níveis até à raiz pública, com um esquema novo se clarificar os tipos e o fluxo. Conferir os formatos nas fontes fixas; reservar o desenvolvimento dos certificados de máscaras e dos circuitos completos para as unidades seguintes. Visar até seis páginas contínuas, compilar e inspeccionar antes de prosseguir.

Resultado: quatro secções novas em cinco páginas, com os tipos do ciclo, a dedução completa da mudança de coordenadas, a preparação dos sextuplos e a construção dos ramos. Um exemplo novo de 700 saídas calcula os 19 nós de Selene, os dois de Helios e a raiz de Selene; o caminho da saída 699 dá as posições 15, 0 e 1. A comparação das aberturas justifica a utilização de abscissas e fixa as coordenadas adicionais a zero. O fecho de Schnorr foi explicitado com as suas mensagens e verificação, preparando a indução descendente desde a raiz. As secções seguem o fluxo do argumento, sem quebras de página explícitas.

Duas revisões independentes conferiram as relações e os tipos contra as fontes. Precisaram-se a representação afim dos nós abaixo da raiz, a publicidade da raiz e o âmbito da coincidência dos corpos para aritmética directa. A discrepância entre os parâmetros Helios–Selene da cópia seleccionada e os do relatório Veridise local ficou registada nas notas; o capítulo usa as constantes conferidas no Rust e na fonte primária de tevador. O script de contas de F4 verificou as transformações, a projecção com todas as componentes de torção e o fecho da raiz.

A compilação integral estabilizou com remissões e citações resolvidas e os mesmos 164 avisos tipográficos de F3, além do aviso preexistente de opção obsoleta de xcolor. Inspeccionaram-se as cinco páginas, a transição de F3 e a entrada bibliográfica nova. O código TeX anterior de F1–F3, os divisores e o preâmbulo foram conservados. O crescimento do sumário deslocou as páginas físicas subsequentes em uma posição, sem alterar a numeração impressa dos capítulos anteriores.

Artefactos: livro em revisão com 288 páginas; FCMP++ parcial com vinte páginas, correspondentes às páginas físicas 191–210; divisores com trinta páginas, correspondentes às páginas físicas 40–69. A reconstrução de FCMP++ prossegue para as 38 páginas de texto e o poster novo.

## Unidade F5 — necessidade e custos dos certificados de divisores

Estado: concluída e verificada em 10 de Novembro de 2026.

Aplicar cumulativamente o capítulo dos divisores às multiplicações das máscaras agora identificadas na folha e entre níveis. Desenvolver as três páginas reservadas à razão de usar estes certificados e aos seus custos: representação do escalar entre corpos, construção da função, dados comprometidos, produtos secretos e trabalho de avaliação. Distinguir as cinco multiplicações da primeira camada, a reutilização do escalar com U e V e a multiplicação de cada camada adicional; conferir as dimensões concretas nas fontes. Conservar a hipótese de normalização e as condições de denominadores, remetendo a ordem completa dos desafios e as excepções dos dispositivos para os circuitos completos. Compilar e inspeccionar esta unidade antes de prosseguir.

Resultado: duas secções contínuas acrescentam três páginas ao capítulo. A primeira aplica a representação entre corpos às cinco multiplicações da folha e às máscaras dos ramos, trabalhando os sinais e a partilha entre U,V. A segunda calcula os dados comprometidos, as relações multiplicativas, a preparação das tabelas e a recuperação dos coeficientes. A fórmula de Lagrange recebe uma justificação completa por unicidade; o texto explica por que a interpolação directa efectua 33 282/34 322 produtos no corpo enquanto o certificado usa sete relações multiplicativas secretas. Estas contagens têm objectos e fases explicitamente distintos.

Duas revisões independentes confirmaram as fontes e a álgebra. Usaram-se D_O,D_U,D_V,D_R,D_C para os pontos de máscara, conservando W_R,W_O como matrizes de GBP; d_A distingue o limite do pólo do grau distinguido de F3. A condição de normalização permaneceu explícita, e os custos da interpolação foram atribuídos ao algoritmo apresentado. As contagens de 2293 elementos da folha, 35 produtos dos cinco certificados e 49 no caminho de três níveis foram conferidas directamente.

Validação: o script F5 verificou as duas bases de Lagrange nos respectivos nós, recuperou dezasseis pares de polinómios, contou os produtos da interpolação densa e conferiu duzentos conjuntos das quatro relações de máscaras. A compilação integral estabilizou com remissões e citações resolvidas e os mesmos 164 avisos tipográficos, além do aviso preexistente de xcolor. O prefixo F1–F4, as fontes dos divisores, o preâmbulo e a bibliografia foram preservados. Inspeccionaram-se as quatro páginas físicas atravessadas por F5, incluindo a transição de F4, a tabela e as equações.

Artefactos: livro em revisão com 291 páginas; FCMP++ parcial com vinte e três páginas, correspondentes às páginas físicas 191–213; divisores com trinta páginas, correspondentes às páginas físicas 40–69. A reconstrução prossegue para 38 páginas de texto e um poster novo; os certificados e os seus custos ocupam as três páginas adicionais reservadas.

## Unidade F6 — condições dos circuitos de pertença

Estado: concluída e verificada em 11 de Novembro de 2026.

Desenvolver uma unidade de até seis páginas, partindo dos certificados e dos dados já definidos. Ensinar as relações aritméticas para as somas com um ponto público, a pertença a uma lista e a selecção de um sextuplo através da combinação desafiada. Explicitar os denominadores e a necessidade de vincular a lista e a escolha antes do desafio. Reunir estas relações nos dois circuitos, deduzir as contagens de 97/52/32 linhas e explicar as dimensões dos IPA e o papel dos compromissos adicionais. Reservar a ordem integral do transcrito e as garantias da composição para unidades próprias, sem exceder as quinze páginas de texto restantes no total. Compilar, inspeccionar e conferir as condições algébricas antes de prosseguir.

Resultado: quatro secções contínuas acrescentam quatro páginas. A soma é deduzida através da secante, com a inversa e o domínio explícitos; a pertença escalar usa o produto de diferenças. A compressão das seis coordenadas tem um exemplo completo e um limite de colisão demonstrado. As relações da folha e dos níveis seguintes são reunidas, contadas e distribuídas pelos dois circuitos; os exemplos de uma e duas entradas calculam as dimensões e as rondas dos IPA.

Duas revisões independentes conferiram a matemática, os domínios e a fonte seleccionada. A redacção distingue a escolha existencial de uma posição da sua codificação como variável; distingue também a compressão probabilística da igualdade exacta dos sextuplos. Corrigiu-se uma vírgula acidental em dois expoentes antes da compilação final. Os testes aritméticos estão conservados em `editorial/checks/`, juntamente com os de F2–F5.

A compilação integral estabilizou sem remissões ou citações por resolver e sem novos avisos tipográficos. O prefixo F1–F5, os divisores, o preâmbulo e a bibliografia foram preservados. As páginas físicas 213–217 foram inspeccionadas, incluindo a transição e as equações. O livro tem 295 páginas; FCMP++ tem 27 páginas, nas páginas físicas 191–217; divisores mantém 30, nas páginas 40–69. O capítulo de FCMP++ permanece em construção até às 38 páginas e ao poster novo.

## Unidade F7 — transcrito e desafios

Estado: concluída e verificada em 11 de Novembro de 2026.

Fixar a sequência integral do transcrito, distinguindo os dados comprometidos antes dos desafios dos auxiliares calculados depois. Desenvolver o contexto, o fecho da raiz, os desafios de divisores e os seis pesos de cada entrada, e as duas provas GBP em sequência. Explicar a amostragem dos pontos e o domínio das avaliações, com as excepções pertinentes. Conferir o modelo probabilístico efectivo face ao modelo regular de D5; conservar as condições das garantias. Visar cinco a seis páginas contínuas, compilar e inspeccionar antes de prosseguir para a composição final e o poster.

Resultado: três secções contínuas acrescentam cinco páginas. A primeira fixa o contexto, a codificação dos tipos e contagens, o desafio da raiz, os desafios partilhados dos dispositivos e as duas provas GBP sequenciais. A segunda deriva o domínio das avaliações e distingue a construção das razões honestas da verificação por multiplicação cruzada. A terceira transporta a contagem de D5 para o amostrador de abscissas e sinais, contando explicitamente os pares excepcionais e conservando a probabilidade incondicional.

Duas revisões independentes conferiram o contexto, a ordem dos desafios, os domínios e a demonstração do limite. Precisaram-se a raiz quadrada zero, os dados fixados na experiência probabilística e as remissões para o capítulo dos divisores. A fonte usa os escalares finais do IPA de Selene antes de iniciar a prova de Helios; a resposta de Schnorr da raiz acompanha a verificação separada. A hipótese de normalização permanece expressa. Os desvios da redução de hashes e as consultas adaptativas de Fiat–Shamir são identificados como componentes da redução de segurança completa.

Validação: `editorial/checks/sampling-F7.py` enumera 4152 pares em treze curvas pequenas; confere as massas, a dominação dos abortos, os encontros repetidos, a contagem de no máximo 4N pares excepcionais e as seis representações de cada secante regular. Oito curvas incluem pontos admissíveis de ordenada zero. Estes testes verificam as contas geométricas e probabilísticas; o limite geral é demonstrado no texto.

A compilação integral estabilizou com remissões e citações resolvidas e os mesmos 164 avisos tipográficos preexistentes. Inspeccionaram-se as páginas físicas 217–222. O prefixo F1–F6, os divisores, o preâmbulo e a bibliografia foram preservados. Os excertos foram conferidos contra o livro: 300 páginas no total, trinta em divisores e 32 em FCMP++. Restam a composição final, os custos completos e o poster, além das restantes alterações do livro registadas em `retoma.md`.

## Unidade F8 — composição final e custos completos

Estado: concluída e verificada em 16 de Novembro de 2026. FCMP++ atinge 38 páginas de texto; o poster novo será a unidade seguinte.

Resultado: cinco secções contínuas reúnem a extracção descendente desde a raiz, a ligação a SAL, a estabilidade da imagem e as condições de ocultação. A simulação conserva o enunciado público fixo, incluindo imagens e pseudo-compromissos; a realização condicionada à admissibilidade conserva a hipótese de simulação da mesma distribuição. A completude é enunciada no domínio dos certificados e das somas. A resistência a colisões dirigidas entre imagens de saídas diferentes fica identificada como propriedade adicional, sem lhe atribuir a demonstração da estabilidade para uma mesma saída.

As contagens partem das aberturas e da capacidade dos compromissos, deduzem as mensagens das duas GBP e o fecho de Schnorr, e acrescentam SAL e os três pontos da apresentação. O exemplo de uma entrada e três níveis dá 4160 bytes para pertença e 4640 para o objecto FCMP++. O trabalho do provador distingue a interpolação densa dos divisores, os polinómios da prova exterior e as operações de grupo. A última página deduz a capacidade da árvore e o limite de quarenta compromissos auxiliares, conservando a contagem exacta dos ramos.

Fontes: releram-se as relações e a composição no TeX de Cypher Stack, as funções de contagem e de leitura/escrita Rust, a acomodação dos dados em tape.rs, os circuitos e o cálculo dos polinómios de Generalized Bulletproofs. A consulta à página primária de Curve Trees confirmou a referência bibliográfica; a construção seleccionada e as contagens seguem as cópias locais fixas. O historial e as diferenças de âmbito ficam no registo de versões.

Validação: composition-costs-F8.py confere 2048 configurações por enumeração dos ramos, blocos e mensagens; 252 avaliações de produtos de polinómios e respectivos custos; 260642 apresentações sobre um grupo pequeno, com enunciado fixo e bijecção completa. As duas funções de contagem Rust foram copiadas directamente para um programa isolado, compilado em /tmp; os seus resultados coincidem com as fórmulas nas mesmas 2048 configurações. O teste verifica contas e distribuições finitas, conservando o âmbito próprio das hipóteses criptográficas.

A compilação integral produz 306 páginas, com remissões e citações resolvidas e os mesmos 164 avisos de caixas. O prefixo F1–F7 foi conservado integralmente. Inspeccionaram-se as sete páginas físicas atravessadas por F8, incluindo a transição de F7, e ajustou-se a última página para desenvolver os limites dos compromissos auxiliares. FCMP++ ocupa as páginas físicas 191–228; divisores conserva 40–69.

Os auxiliares temporários da sessão anterior tinham desaparecido. A compilação e a exportação foram reconstituídas em editorial/build-pt.py e editorial/export-chapters.py; a configuração e os produtos intermédios continuam em /tmp. O pacote oficial de hifenização portuguesa foi descarregado e extraído nesse directório, sem instalação no sistema.

## Poster de FCMP++ — vista conjunta

Estado: concluído em 16 de Novembro de 2026, depois das 38 páginas de texto. Uma página A3 reúne quatro percursos: conjunto e caminho, prova de pertença, apresentação e SAL, validação do gasto. O esquema novo mostra o caminho de três níveis com alternância Selene–Helios–Selene; as relações de máscaras, divisor, selecção, autorização e equilíbrio acompanham o percurso. O rodapé conserva as hipóteses da composição e os limites da simulação condicionada, além das fórmulas do tamanho.

O poster foi criado de raiz em `translations/pt/posters/fcmp-composition/poster.tex`, com desenhos e texto vectoriais. Os dois conjuntos de figuras antigos deixaram o directório de trabalho e conservam-se no Git. O programa de compilação produz o poster antes de compor o livro. Inspeccionou-se a página e corrigiram-se sobreposições, uma acentuação em modo matemático e substituições de tamanho de fonte; o poster final não produz avisos de composição.

O livro tem 307 páginas. FCMP++ ocupa 38 páginas de texto, físicas 191–228, e o poster ocupa a página física 229. O excerto contém estas 39 páginas. As páginas dos excertos de divisores e FCMP++ são conferidas por texto e imagem contra o livro antes de serem actualizadas.

## Receitas de pontos e representações canónicas

Estado: concluídas em 16 de Novembro de 2026. A explicação de «canónico» começa na aritmética modular e distingue a escolha de representantes das regras completas de codificação. O índice remissivo continua pendente e acolherá estes termos.

A nova secção dos conceitos básicos define a leitura dos 256 bits, a redução no corpo, os dois ramos do mapa e a escolha do sinal. Demonstra a ausência de denominadores nulos e a equação da curva. Define as receitas por Keccak e por BLAKE2b personalizado, preserva a possibilidade matemática da identidade e relaciona a escolha com as classes de saídas da construção fixa. A passagem de bLSAG passa a usar esta definição cumulativamente.

A secção dos compromissos deriva separadamente o gerador fixo H: descompressão do resumo de G e três duplicações, com todas as codificações intermédias. Explica a hipótese de dificuldade da relação entre geradores e a distinção entre descodificar bytes e aplicar o mapa algébrico. O texto contém as codificações de H, H_p^(1)(G) e H_p^(2)(G).

Validação: hash-points.py verifica 522 argumentos, incluindo fronteiras da redução dos 256 bits, ambos os ramos, a simetria, os resíduos, a pertença à curva e os exemplos. A comparação facultativa compila directamente as funções C da fonte fixa em pasta temporária; as imagens antes e depois do cofactor, o BLAKE2b personalizado, o Keccak e H coincidem com as contas independentes. Nenhuma fonte externa foi modificada. A compilação produz 310 páginas, conserva os 164 avisos anteriores e resolve remissões e citações. Inspeccionaram-se as páginas físicas 22–23, 35–39, 79 e 100–102. FCMP++ mantém as 38 páginas de texto e o poster; divisores mantém trinta páginas.

## Domínio das imagens de chave e pergunta decisional

Estado: concluído em 16 de Novembro de 2026. O percurso de bLSAG demonstra a decomposição entre a componente de ordem prima e a de pequena ordem, trabalha o ponto (0,−1) e deriva o termo residual cT na ronda verdadeira. O texto conta os desafios admissíveis no modelo ideal, explica as oito variantes e demonstra por que o teste [l]I=O rejeita todas as componentes de torção não nulas. Distingue a validação da imagem da multiplicação pelo cofactor e atribui expressamente o resultado do exame histórico à divulgação primária de 2017.

A pergunta DDH é apresentada através de quatro pontos e das duas distribuições, antes de ser nomeada; as dificuldades decisional, computacional e do logaritmo discreto conservam hipóteses próprias. Retirou-se o parágrafo solicitado sobre a variante parcialmente ligável de MLSAG.

Validação: key-image-domain.py constrói 24 assinaturas válidas no grupo Z_19 x Z_8, três posições de signatário com oito imagens cada, em 93 tentativas; confere todas as 152 decomposições e a contagem dos múltiplos dos desafios. Sobre Edwards25519, verifica as oito variantes, as projecções e 56 reconstruções, incluindo representantes próximos da ordem do subgrupo. O teste de domínio rejeita exactamente as sete variantes alteradas. As contas não substituem as hipóteses criptográficas nem constituem uma auditoria do histórico da rede.

A compilação conserva 312 páginas, 164 avisos anteriores e todas as remissões resolvidas. Inspeccionaram-se as páginas físicas 80–86, incluindo a transição para MLSAG. Uma reserva condicional de espaço mantém o início da discussão de torção junto do título. FCMP++ conserva 38 páginas de texto e o poster, nas páginas físicas 196–234; divisores conserva as páginas 42–71. Os excertos foram novamente conferidos por texto e imagem.

## CLSAG — duas páginas adicionais

Estado: concluído em 16 de Novembro de 2026. A secção aumenta de cinco para sete páginas físicas atravessadas, conservando o início na página 86 e passando o capítulo seguinte de 91 para 93. Duas novas subseções desenvolvem as testemunhas partilhadas, um exemplo completo em ordem 19 e o papel dos pesos. O exemplo calcula p=5, z=9, pesos 3 e 4, testemunha agregada 13 e resposta 9, e verifica ambos os pontos reconstruídos.

O texto distingue a extracção da combinação escalar das hipóteses sobre as suas componentes. A segurança remete para a variante one-more de logaritmos de combinações, a resistência da agregação e RO-DDH, no modelo e nos jogos primários. A base da imagem passa a J_i, conservando I para imagens. Corrigiu-se o título «Especialização usada por Monero», precisaram-se as etiquetas de 32 bytes e desenvolveu-se a contagem de 576 bytes, ou 608 incluindo a imagem que acompanha a entrada.

A conferência da fonte revelou a importância da redução de c_i mu_P e c_i mu_C antes de multiplicar os pontos. A especialização explicita essa regra para o grupo completo e conserva a factorização compacta no domínio primo da análise abstracta. Apenas a coluna verdadeira é apresentada com testemunhas conhecidas P_pi=pG e C_pi=zG; os membros registados podem incluir componente de torção. A validação da imagem primária mantém o seu teste próprio.

Validação: clsag-aggregation.py confere o exemplo, 2280 reconstruções e extracções sobre a curva de ordem 19, todas as 360 diferenças não nulas e a proporção exacta 19/361 de pesos que as anulam. Compara ainda 361 produtos de coeficientes no grupo Z_19 x Z_8; 247 casos distinguem a redução prévia da factorização na componente de torção, enquanto todos coincidem no subgrupo primo. Conferiram-se a serialização e os domínios directamente no C++.

A compilação produz 314 páginas, conserva os 164 avisos anteriores e resolve referências e citações. Inspeccionaram-se as páginas físicas 86–92. FCMP++ mantém 38 páginas de texto e o poster, em 198–236; divisores mantém trinta páginas, em 42–71. Os excertos foram conferidos por texto e imagem antes de serem actualizados. O teste das imagens de chave passou também a evitar a criação de bytecode no directório de trabalho.

## Bulletproofs — duas condições de verificação

Estado: concluída e verificada em 16 de Novembro de 2026. O compromisso ao valor conserva a sua igualdade própria. A condição vectorial define directamente o ponto público do argumento de produto interno; as dobras conduzem à segunda igualdade final. Foram retirados a soma inicial das condições, os resíduos e a combinação ponderada. A expansão nos geradores originais conserva cada sinal, peso e mudança de base. Eliminou-se também uma nota sobre uma versão anterior e uma quebra de página que deixava quase toda a página vazia.

A antiga página impressa 109 foi localizada no PDF de referência 24b7ee6, página física 122. A subsecção de tamanho repetia apenas a fórmula da prova agregada; foi retirada de Transactions.tex. A fórmula e a explicação útil permanecem nos requisitos de espaço.

Validação: bulletproof-checks.py verifica 120 provas algébricas sobre dois corpos, com dimensões de 2 a 64, e 384 dobras. Confere separadamente as duas igualdades, os geradores reconstruídos, os pesos inversos, a passagem de H' a H e perturbações independentes das condições. Os testes usam bases formais independentes e verificam identidades; não constituem uma análise da segurança criptográfica. As condições foram também confrontadas com os termos de verificação da fonte C++.

A compilação produz 312 páginas, resolve referências e citações e conserva os 164 avisos de caixas. Inspeccionaram-se as páginas alteradas e as transições. FCMP++ mantém 38 páginas de texto e o poster, nas páginas físicas 196–234; divisores mantém trinta páginas, em 42–71. Os excertos foram conferidos por texto e imagem.
