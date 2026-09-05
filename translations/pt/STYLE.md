# Norma editorial da tradução portuguesa

## Variante e ortografia

- Emprega-se português europeu, sem vocabulário nem construções próprias do
  português brasileiro.
- Segue-se uma ortografia tradicional e etimológica, anterior ao Acordo
  Ortográfico de 1990. A preferência editorial desta tradução prevalece mesmo
  quando a grafia escolhida seja anterior a outras reformas ortográficas.
- Conservam-se, entre outras, as grafias `contracto`, `acção`, `transacção`,
  `projecto`, `óptimo` e `facto`.
- Preserva-se a clareza da prosa técnica; a ortografia tradicional não deve
  tornar obscura a explicação de um conceito.

## Vocabulário de base

| Inglês | Português adoptado |
|---|---|
| address | endereço |
| blockchain | lista de blocos (na primeira ocorrência, `blockchain`) |
| file | ficheiro |
| hash function | função hash |
| input | entrada |
| key image | imagem de chave |
| output | saída |
| range proof | prova de intervalo |
| ring | anel |
| transaction | transacção |
| user | utilizador |
| wallet | carteira |

Os termos ainda controversos serão acrescentados ao glossário somente depois
de revistos no respectivo contexto técnico.

## Termos técnicos e código

- Mantêm-se inalterados os identificadores do código, nomes de tipos, nomes de
  funções e siglas, por exemplo `RCTTypeBulletproofPlus`, `CLSAG` e `FCMP++`.
- Um termo inglês necessário pode acompanhar a primeira tradução entre
  parênteses. Depois disso, usa-se de modo consistente o termo português.
- Distingue-se sempre entre uma funcionalidade presente no código, uma
  funcionalidade activada pelas regras de consenso e uma proposta ainda em
  desenvolvimento.

## Voz e andamento

- Conserva-se a voz colectiva do original português: `veremos`, `podemos` e
  `chamaremos` acompanham o leitor sem lhe falar de cima.
- A intuição e um exemplo concreto precedem, sempre que possível, a definição
  formal. Depois da fórmula, explica-se por que funciona e qual será o seu uso.
- Alice, Bob e os restantes intervenientes são tratados como nomes próprios.
  Exemplos breves e um humor discreto são bem-vindos quando esclarecem, nunca
  quando interrompem o raciocínio.
- Os parágrafos devem avançar sem pressa, mas cada frase deve cumprir uma
  função. Evitam-se traduções literais, fragmentos e sequências artificiais de
  `\\` ou `\newline` usadas apenas para separar prosa.

## Notação e composição

- Um símbolo mantém o mesmo papel ao longo de uma demonstração. Escalares e
  valores simples escrevem-se em minúscula; pontos de curva e objectos
  compostos, em maiúscula, salvo convenção técnica explícita.
- `\bmod` designa a operação que devolve o resto; `\pmod{n}` aparece em
  congruências e no fim de expressões. Em português, fala-se em `módulo`, não
  em `modulus`.
- Usa-se pontuação portuguesa normal em torno de fórmulas, citações e notas de
  rodapé: não há espaço antes de dois pontos, ponto e vírgula, vírgula ou ponto
  final.
- Identidades algébricas não substituem a explicação: uma passagem decisiva é
  anunciada antes da equação ou interpretada logo depois.
- Os rótulos curtos já característicos do livro, como `Funciona porque` e
  `Requisitos`, mantêm-se quando ajudam a orientação.

## Fontes e revisão

- Toda a afirmação sobre a implementação deve indicar a revisão do código
  Monero que foi consultada.
- As expressões `regra de consenso activa`, `comportamento implementado` e
  `trabalho experimental` não são sinónimas. Uma funcionalidade no ramo de
  desenvolvimento só é descrita como activa se a programação de versões da
  rede principal e a validação de blocos o confirmarem.
- Artigos científicos e documentação de protocolo complementam o código-fonte;
  não são colocados dentro do repositório Monero.
- Cada alteração deve abranger uma unidade conceptual pequena e ser revista
  quanto à exactidão técnica, à língua e à compilação de LaTeX.
- Ficheiros gerados, apontamentos e experiências permanecem fora deste
  repositório.
