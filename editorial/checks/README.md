# Verificação das contas

Estes programas reproduzem identidades, dimensões e exemplos da exposição. Usam Python 3 e a biblioteca padrão. As hipóteses criptográficas e as demonstrações gerais conservam o seu âmbito próprio.

Executar cada ficheiro com `python3 editorial/checks/NOME.py`:

- `sal-F2.py`: completude, extracção e simulação das relações de SAL.
- `gbp-F3.py`: coeficientes distinguidos, avaliação polinomial e relação de entrada do IPA.
- `tree-F4.py`: parâmetros e transformações de curvas, projecção da torção, árvore e fecho da raiz.
- `divisor-costs-F5.py`: contagens, interpolação de Lagrange e sinais das máscaras.
- `circuits-F6.py`: somas afins, pertença, compressão e dimensões dos circuitos.
- `sampling-F7.py`: distribuição dos pontos, massas dos pares e contagem de secantes regulares e excepcionais.

Os resultados esperados e os limites de cada verificação estão no registo de versões das fontes e no registo de revisão. O programa F4 pressupõe a primalidade dos módulos estabelecida pelas fontes; a sua verificação das ordens não constitui um certificado autónomo de primalidade.
