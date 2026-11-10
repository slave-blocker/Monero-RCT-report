# Registo de notação

| Símbolo | Significado e domínio | Regra editorial |
|---|---|---|
| \(\mathbb F\), \(\mathbb F_q\) | Corpo das coordenadas da curva em estudo | Nas contas iniciais, \(q\) primo maior que três; exemplo em \(\mathbb F_{17}\). |
| \(\ell\), \(l\) | Ordem prima do subgrupo criptográfico | Distinguir de \(q\); uniformização global pendente. |
| \(\mathbb E\) | Curva elíptica | Weierstrass nos divisores, com transformação de representação explicitada quando necessária. |
| \(a_{\mathbb E},b_{\mathbb E}\) | Coeficientes da equação da curva | Reservar \(a,b\) simples conforme a construção posterior; evitar colisões locais. |
| \(\mathcal O_\infty\) | Identidade na apresentação de Weierstrass | Explicar a representação projectiva antes de calcular ordens nesse ponto. |
| \(x,y\) | Funções coordenadas, ou coordenadas de um ponto quando indexadas | Distinguir \(x(A)\) / \(x_A\) da variável polinomial e da chave secreta usada em FCMP++. |
| \(f_0(x)+yf_1(x)\) | Representante reduzido de uma função polinomial na curva | Derivar pela relação \(y^2=x^3+a_{\mathbb E}x+b_{\mathbb E}\). |
| \(t\) | Parâmetro local | Explicar através de uma coordenada local simples e de exemplos de factorização. |
| \([A]\) | Lugar formal associado ao ponto \(A\) | Aritmética de divisores por coeficientes; soma na curva indicada separadamente. |
| \(\operatorname{ord}_A(f)\) | Ordem inteira de uma função racional não nula | Positiva para zero, negativa para pólo. |
| \(\operatorname{div}(f)\) | Divisor principal da função \(f\) | Distinguir a função testemunha do seu divisor. |
| \(\deg D\), \(\sigma(D)\) | Soma inteira das multiplicidades; soma dos pontos com essas multiplicidades | Manter os três tipos visíveis: divisor formal, inteiro e ponto da curva. |
| \(N_f(x)\) | Norma \(f(x,y)f(x,-y)\) | Polinómio numa variável quando f é polinomial; as raízes contam os zeros sobre cada abscissa. |
| \(D\sim D'\) | Equivalência linear: a diferença é o divisor de uma função racional não nula | Introduzir pela transformação concreta com rectas e verticais. |
| \(\operatorname{Pic}^0(\mathbb E)\) | Grupo das classes de divisores de grau zero por equivalência linear | Nomear depois de construir a redução a \([S]-[\mathcal O_\infty]\). |
| \(F_n\), \(f\) | Testemunha racional da multiplicação; testemunha com os pólos concentrados na identidade | No exemplo, \(F_3=f/(x-10)\) e \(f=x^2+15x+2y\). |
| \(L_A\), \(A_i=2^iA\) | Comprimento da representação do escalar; tabela de duplicações da base A | L_A é uma quantidade de posições; reservar ℓ para a ordem prima de A. |
| \(e_i\), \(m_i\) | Bits da representação inicial; multiplicidades inteiras não negativas da construção com soma fixa | A soma dos m_i é L_A e a soma ponderada por 2^i representa o escalar módulo ℓ. Distinguir a construção da testemunha das variáveis e condições do circuito posterior. |
| \(d\) | Quantidade prescrita de ocorrências afins; limite da ordem do pólo | Para multiplicidade fixa, d = L_A + 1; o espaço da função tem dimensão d para d ≥ 1. |
| \(\widehat f\) | Função testemunha após fixar um coeficiente não nulo em um | A normalização conserva o divisor; a posição escolhida exige coeficiente não nulo na família de testemunhas. |
| \(f(D)\) | Produto dos valores de f elevados às multiplicidades inteiras de D | A definição ordinária exige valores finitos e não nulos no suporte de D. |
| \(\{f,g\}_A\) | Símbolo local, calculado pelas ordens e pelas unidades de f e g em A | Conservar o sinal e a ordem das funções; os produtos globais percorrem pontos geométricos. |
| \(\deg_\infty(f)\), \(\operatorname{lc}(f)\) | Ordem do pólo e coeficiente do monómio de maior peso de uma função polinomial não nula | Usar o parâmetro t = x/y no infinito; uma constante não nula tem peso zero. |
| \(Z\), \(\mathcal L\), \(c_{\rm declive}\), \(c_{\rm corte}\) | Projecção y − c_declive x; função Z − c_corte; parâmetros da recta | Z aplica-se aos pontos afins. Os pontos B₀, B₁, B₂ são encontros com a curva; o terceiro é o inverso da soma dos dois primeiros. |
| \(\mathcal N_f(z)\) | Norma na direcção Z: produto de f nos três encontros com Z = z | Distinguir de N_f(x), a norma quadrática introduzida em D2. Com declive fixo, é um polinómio de grau deg_∞(f) e coeficiente inicial lc(f)³. |
| \(R'\), \(R'/R\) | Derivada formal; derivada logarítmica | Definir pelo termo de primeira ordem em h, incluindo a regra do quociente. Ler os coeficientes inteiros na característica do corpo. |
| \(\Delta_r\) | Derivada do cúbico dos encontros em B_r: 3x² + a_E − 2my | A não nulidade caracteriza um encontro simples; a fórmula combinada admite y = 0 quando Δ_r ≠ 0. |
| \(u_i\), \(\widetilde m_i\) | Variáveis do corpo na relação verificada; levantamento inteiro extraído no intervalo [−1,d] | Distinguir dos m_i não negativos da construção honesta. Exigir d + 1 < p; a coincidência A_i = −W pode produzir −1. |
| \(\gamma_i\), \(o_r\), \(v_W\) | Pesos públicos da tabela; razões auxiliares nos encontros; inversa associada a −W | Os dados da função e do vector precedem o desafio; os auxiliares são calculados depois. |
| \(d_f\) | Ordem efectiva do pólo de f, até ao limite d | A relação aceita funções de peso limitado; a soma fixa pertence à construção da testemunha. |
| \(M\), \(N\), \(s\), \(\varepsilon\) | Quantidade de pares de desafio regulares; quantidade de pontos afins racionais; limite da união dos suportes; erro algébrico | O limite explícito de D5 usa amostragem uniforme condicionada a três encontros distintos. Não atribuir as suas constantes ao amostrador Rust. |
| \(H_p\), \(H\) | Função hash para pontos; gerador fixo dos compromissos | Apresentar cada receita e os seus domínios separadamente. |

## Convenções da nova exposição de FCMP++

Preservar I como imagem de chave, conforme bLSAG e CLSAG. Usar J para a base da imagem. Na tradução das fontes primárias, o I da fonte passa a J no livro, e o L da fonte passa a I. A notação da secção pertinente de `dlogRelations.tex` será reconciliada no exame global; o capítulo antigo de FCMP++ foi substituído, sem conservar os seus esquemas de notação por inércia.

| Símbolo | Significado | Correspondência com as fontes |
|---|---|---|
| \(\mathcal S\), \(\rho\) | Conjunto público admitido; raiz que o fixa | S, TreeRoot; a raiz tem o tipo da curva do respectivo nível, a definir na construção da árvore. |
| \((O,J,C)\) | Chave, base da imagem e compromisso de uma saída | (O,I,C). A escolha do triplo é secreta; os registos do conjunto são públicos. |
| \(I=xJ\) | Imagem de chave pública | L na especificação e na análise de composição. |
| \(r_O,r_J,r_R,r_C\) | Máscaras da chave, base da imagem, compromisso auxiliar e montante | r_o,r_i,r_j,r_c. |
| \((\widetilde O,\widetilde J,R,\widetilde C)\) | Apresentação pública que liga pertença e autorização | (O_tilde,I_tilde,R,C_tilde). |
| \(x,y\), \(z,a\) | Abertura da chave O; máscara e montante na abertura de C | Manter separados os papéis de chave de gasto e máscara de montante. |
| \(n,r,N_{\rm PI}\) | Número de entradas, número de provas de intervalo, número total de argumentos de produto interno | N_PI = 2 + n + r para uma prova de pertença agregada. SAL contribui com um argumento de dimensão um por entrada. |
| \(\bar y,w,\eta\) | Máscara da chave apresentada, produto secreto e máscara da diferença em SAL | ybar = y + r_O; w = x r_J; eta = r_P − ybar − r_R. O w corresponde ao z da fonte; evita confusão com a máscara z de C. |
| \(P,D\) | Compromisso dos factores e produto; diferença pública P − Otilde − R | P = xG + r_J V + wU + r_P T; D = wU + eta T. A máscara r_P é independente. |
| \(\alpha,\beta,\delta,\mu,k_y,k_w,k_\eta\) | Sete máscaras uniformes do protocolo SAL, posteriores à escolha de P | As quatro primeiras conservam os nomes da fonte; k_y, k_w, k_eta correspondem a r_y, r_z, r_r_p. |
| \(A,B,R_O,R_P,R_I\) | Mensagens SAL calculadas antes do desafio, além de P | R_I corresponde ao R_L da fonte, conservando I como imagem. |
| \(s_x,s_J,s_P,s_y,s_w,s_\eta\) | Seis respostas de SAL | Correspondem a s_alpha, s_beta, s_delta, s_y, s_z, s_r_p; s_P é a combinação quadrática das máscaras. |
| \(m_{\rm tx},\tau,\mathcal H_{\rm SAL},e\) | Resumo assinável, sequência codificada, função de hash escalar e desafio de SAL | H_SAL é o nome matemático da função seleccionada; não acrescenta um campo literal SAL ao transcrito. |
| \(x_1,b_1,p_1;\ x_2,y_2,w_2,\eta_2\) | Testemunhas extraídas do argumento de produto e das relações de Schnorr | Conservar os índices até compor com a abertura de R fornecida pela pertença. |

## Prova aritmética generalizada

| Símbolo | Significado e domínio | Correspondência com as fontes |
|---|---|---|
| \(\mathcal G,\mathbb F\) | Grupo de compromisso e respectivo corpo de escalares | Distinguir expressamente do corpo de coordenadas da curva. |
| \(g,h,\boldsymbol g,\boldsymbol h\) | Dois pontos e dois vectores de pontos públicos da prova | G,H,G_bold,H_bold no relatório; são bases do grupo de prova, distintas dos geradores de Monero usados em SAL. |
| \(m,s,q,d\) | Dimensão vectorial, quantidade de compromissos vectoriais, quantidade de condições lineares, grau distinguido d = 2s + 2 | Correspondem a n,n_c,Q,n′ na fonte. O m da fonte, quantidade de compromissos escalares externos, é zero nesta especialização. |
| \(K_k,\boldsymbol c_k,\boldsymbol d_k,\gamma_k\) | Compromisso externo e abertura nas duas famílias de bases, com máscara em h | C_k,c_{k,L},c_{k,R},c′_k na fonte. As condições referem-se a c_k; a testemunha construída usa d_k = 0. |
| \(\boldsymbol a_L,\boldsymbol a_R,\boldsymbol a_O\) | Operandos e resultados dos produtos do circuito | Vectores escalares; posições adicionais recebem zeros. |
| \(W_L,W_R,W_O,W_k,\boldsymbol b\) | Matrizes públicas das condições e vector dos termos constantes | O livro põe b no segundo membro; a constante do Rust tem sinal oposto. |
| \(\lambda,\zeta,\xi,\omega\) | Desafios dos produtos, condições lineares, avaliação e passagem ao IPA | y,z,x,ip_x no Rust. Todos não nulos nesta construção. |
| \(\boldsymbol y,\boldsymbol z,\boldsymbol w_L,\boldsymbol w_R,\boldsymbol w_O,\boldsymbol w_k,b_\zeta,\delta\) | Potências dos desafios e pesos/correcções públicas | y tem comprimento m, z tem comprimento q; y⁻¹ actua depois da multiplicação W_R transposta por z. |
| \(A_I,A_O,S,\alpha,\beta,\rho_S,\boldsymbol s_L,\boldsymbol s_R\) | Compromissos iniciais e respectivas máscaras | A máscara de S recebe o índice S para conservar ρ como raiz da árvore. |
| \(\boldsymbol l(X),\boldsymbol r(X),t(X),T_i\) | Polinómios vectoriais, produto interno polinomial e compromissos dos coeficientes | O coeficiente de grau d é público para uma testemunha válida; os outros recebem T_i. |
| \(\tau_\xi,\mu,\widehat t,P_{\rm ar},u_{\rm PI}\) | Máscaras agregadas, produto avaliado, ponto público reconstruído e base do IPA | u_PI = omega g; a relação entre estes dois pontos é pública. |

## Ciclo, folhas e árvore

| Símbolo | Significado e domínio | Regra de utilização |
|---|---|---|
| \(p_{\rm E},p_{\rm S}\) | Módulos das coordenadas de Edwards/Helios e de Selene | p_E = 2²⁵⁵ − 19; p_S = 2²⁵⁵ − 11686397589588510723982429389243424941. Evitar q, reservado à quantidade de condições em F3. |
| \(b_{\rm H},b_{\rm S}\) | Coeficientes de Helios e Selene, ambas com coeficiente linear −3 | Usar os parâmetros da cópia Rust seleccionada; o relatório Veridise local contém outros parâmetros. |
| \(b_O,O_{\rm reg},C_{\rm reg},\pi\) | Bytes da chave original, pontos registados e projecção para o subgrupo primo | J deriva dos bytes originais; π(P) = [8][8⁻¹ mod ℓ]P. A projecção conserva a componente de ordem ℓ. |
| \(x_{\rm E},y_{\rm E},d_{\rm E};u,v;X,Y\) | Coordenadas Edwards, Montgomery e Wei25519 | Todas em F_pE. Distinguir x_E da chave secreta x de SAL. |
| \(a_{\rm M},\kappa,a_{\rm W},b_{\rm W}\) | Parâmetro de Montgomery, raiz fixa de −486664 e coeficientes de Wei25519 | a_M = 486662; a_W = 1 − a_M²/3; b_W = 2a_M³/27 − a_M/3. |
| \(\boldsymbol g_{\mathcal E},h_{\mathcal E},B_{\mathcal E}\) | Bases vectoriais, base de máscara e inicializador na curva do nível | O inicializador está abrangido pela hipótese de dificuldade de relações com todas as bases GBP. |
| \(\boldsymbol v_j,Q_j,K_j,\widetilde Q_j,\beta_j\) | Vector do ramo, nó, compromisso mascarado, nó mascarado e máscara | Q_j = B + ⟨v_j,g⟩; K_j = ⟨v_j,g⟩ + β_j h; Qtilde_j = B + K_j. Completar v_j com zeros ao comparar a abertura ampliada de F3. |
| \(L,\rho,A_{\rm raiz},\nu,c_{\rm raiz},s_{\rm raiz}\) | Profundidade, raiz pública e mensagens/escalares do fecho de Schnorr | Q_L = ρ. A_raiz = νh, s_raiz = ν + c_raiz β_L. O vector do ramo da raiz tem abertura pública conhecida. |

## Certificados das máscaras e custos

| Símbolo | Significado e domínio | Regra de utilização |
|---|---|---|
| \(D_O,D_U,D_V,D_R,D_C\) | Pontos certificados na primeira camada | −r_OT, −r_JU, −r_JV, r_RT, −r_CG. A letra D conserva W_R,W_O para as matrizes de F3. |
| \(D_j=-\beta_jh_{\mathcal E_j}\) | Ponto que retira a máscara de um nó | Q_j = Qtilde_j + D_j; o escalar certificado tem o sinal da multiplicação efectivamente usada. |
| \(\ell_A,L_A,d_A\) | Ordem da base A, comprimento da representação e limite do pólo de f_A | d_A = L_A + 1; o índice distingue este limite do grau d = 2s + 2 em GBP. L_A = 253 em Edwards e 255 nas curvas do ciclo. |
| \(f_A=f_{A,0}+yf_{A,1}\) | Função do certificado da multiplicação W = s_A A | Os zeros incluem −W; na primeira camada, W representa um dos D acima. A função e as coordenadas são dados secretos comprometidos. |
| \(t,z_j,\Lambda_j(X)\) | Tamanho da grelha local, pontos públicos distintos e polinómios de Lagrange | Notação local da interpolação; Λ_j(z_i) = δ_ij. A grelha prepara a testemunha; os três pontos desafiados pertencem à verificação posterior. |

## Condições dos circuitos

| Símbolo | Significado e domínio | Regra de utilização |
|---|---|---|
| \(P_0,P_1,P_2\), \(\iota_{\rm a},\sigma_{\rm a}\) | Ponto público, operandos secretos, inversa da diferença de abscissas e declive da soma | Todos os pontos afins e válidos; exigir X_1 ≠ X_0. O resultado pode ter X_2 = X_0. |
| \(w,v_i,u,p_i\) | Largura da lista, candidatos, valor escolhido e produtos acumulados | p_0 = v_0 − u; p_i = p_(i−1)(v_i − u); p_(w−1) = 0. |
| \(\boldsymbol t,\boldsymbol t_i,\chi_j,\Phi_{\boldsymbol\chi}\) | Sextuplo escolhido, candidatos, seis pesos e combinação linear | Pesos separados, comuns a todas as linhas de uma entrada; os dados precedem os desafios. |
| \(\varepsilon_{\rm sext}\) | Erro algébrico de colisão para valores fixados | No modelo uniforme em F*, limite min(1,w/(\|F\|−1)); não representa o erro completo de Fiat–Shamir. |
| \(\mathsf{Mult}_A(W;\boldsymbol u,f)\) | Relações do certificado de multiplicação de D5 | Abreviatura das sete multiplicações, condições lineares, normalização e fixação anterior ao desafio. |
| \(N_{\rm S},N_{\rm H},m_{\rm S},m_{\rm H},\operatorname{pot}_2\) | Linhas dos circuitos, dimensões dos IPA e arredondamento à potência de dois seguinte | N_S = n(97+52⌊(L−1)/2⌋); N_H = 32n⌊L/2⌋. m_S = pot₂(max(256,N_S)); m_H = pot₂(max(128,n,N_H)). |

As etiquetas existentes são mantidas durante as unidades locais para preservar as referências a jusante. A estrutura definitiva será reconciliada quando cada capítulo ficar integralmente reescrito.
