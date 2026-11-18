# Verificação das contas

Estes programas reproduzem identidades, dimensões e exemplos da exposição. Usam Python 3. As dependências específicas indicam-se junto de cada programa. As hipóteses criptográficas e as demonstrações gerais conservam o seu âmbito próprio.

Executar cada ficheiro com `python3 editorial/checks/NOME.py`:

- `worked-examples.py`: pagamento de 11 unidades, pesos de Bulletproofs+, zeros e multiplicidades dos exemplos sobre F17, identidades em 75 secantes, razões e porta do certificado, interpolação, árvore de 684/685 saídas, cotas exactas e uniformidade do resíduo de TxTangle num corpo pequeno.
- `sal-F2.py`: completude, extracção e simulação das relações de SAL.
- `gbp-F3.py` verifica o coeficiente reservado, a contribuição dos compromissos escalares e das suas máscaras na avaliação pública, os sinais das correcções vectoriais e as dobras do IPA até à igualdade final. No circuito dos dois quadrados, compara as saídas correctas \((9,16)\) com \((10,15)\) e verifica também o resíduo obtido quando o compromisso escalar guarda \(24\) em lugar de \(25\).
- `tree-F4.py`: parâmetros e transformações de curvas, projecção da torção, árvore e fecho da raiz.
- `divisor-costs-F5.py`: contagens, interpolação de Lagrange e sinais das máscaras.
- `circuits-F6.py`: somas afins, pertença, compressão e dimensões dos circuitos.
- `sampling-F7.py`: distribuição dos pontos, massas dos pares e contagem de secantes regulares e excepcionais.
- `composition-costs-F8.py`: contagens de compromissos e mensagens, limites dos auxiliares, capacidade da árvore, custos dos polinómios e bijecção da apresentação com enunciado fixo. A opção `--rust-source /home/dollner/monero-oxide-fcmp` compara as fórmulas com as funções de contagem da fonte, compiladas isoladamente num directório temporário; requer `rustc` e deixa a fonte intacta.

- `hash-points.py`: mapa algébrico, receitas de pontos, cofactor e derivação do gerador H; a comparação facultativa com a fonte C usa `--source`.
- `key-image-domain.py`: decomposição de torção, variantes da imagem, reconstrução das rondas e teste do subgrupo.
- `clsag-aggregation.py`: reconstrução e extracção da combinação escalar, pesos e redução prévia dos coeficientes.
- `bulletproof-checks.py`: as duas condições de verificação, dobras, pesos finais e perturbações independentes.
- `appendix-hashes.py --source /caminho/para/monero` usa PyCryptodomex para Keccak e lê o exemplar binário de tipo 6. Confere os índices, os compromissos, os resumos da transacção, a árvore de seis folhas e o identificador do bloco contra as tabelas impressas nos apêndices B e E.
- `transaction-indices.py`: índices relativos, varints e comprimentos de extra; `--source` compara o cabeçalho C++ original.
- `generator-relations.py`: relações deliberadas entre bases, igualdades SAL e duas transformações de respostas distribuídas.

Os resultados esperados e os limites de cada verificação estão no registo de versões das fontes e no registo de revisão. O programa F4 pressupõe a primalidade dos módulos estabelecida pelas fontes; a sua verificação das ordens não constitui um certificado autónomo de primalidade.
