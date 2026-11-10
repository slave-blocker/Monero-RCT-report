"""Contas exactas da amostragem e das secantes em curvas pequenas.

Verifica a massa dos pontos e pares, a contagem de pares excepcionais
e as seis representações ordenadas de cada secante regular. A prova
geral de solidez e a passagem a Fiat--Shamir pertencem ao texto.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

curves = pairs = zero_ordinate_curves = 0
for q, (a, b) in product((7, 11, 17, 19, 23), ((1, 1), (2, 2), (-3, 5))):
    if (4 * a**3 + 27 * b**2) % q == 0:
        continue
    points = [(x, y) for x, y in product(range(q), repeat=2)
              if (y*y - x*x*x - a*x - b) % q == 0]
    n = len(points)
    assert n > 2
    admissible = {x for x, y in points if x}
    nx = len(admissible)
    assert nx >= Fraction(n - 2, 2)
    # Distribuição condicionada a uma abscissa admissível não nula.
    mass = {p: (Fraction(0) if p[0] == 0 else
                Fraction(1, nx if p[1] == 0 else 2 * nx)) for p in points}
    assert sum(mass.values()) == 1
    assert max(mass.values()) <= Fraction(2, n - 2)
    # Aborto em x=0: sucesso R/(R+1), por soma geométrica.
    success = Fraction(nx, nx + 1)
    actual = {p: m * success for p, m in mass.items()}
    assert sum(actual.values()) == success
    assert all(actual[p] <= mass[p] for p in points)
    exceptional = 0
    regular_lines = Counter()
    for p, r in product(points, repeat=2):
        pairs += 1
        assert mass[p] * mass[r] <= Fraction(4, (n - 2)**2)
        if p[0] == r[0]:
            exceptional += 1
            continue
        slope = (r[1] - p[1]) * pow((r[0] - p[0]) % q, -1, q) % q
        intercept = (p[1] - slope * p[0]) % q
        x3 = (slope*slope - p[0] - r[0]) % q
        y3 = (slope*x3 + intercept) % q
        assert (x3, y3) in points
        repeated = (x3, y3) in (p, r)
        deltas = [(3*x*x + a - 2*slope*y) % q
                  for x, y in (p, r, (x3, y3))]
        assert repeated == (0 in deltas)
        if repeated:
            exceptional += 1
        else:
            regular_lines[slope, intercept] += 1
    assert exceptional <= 4 * n
    assert all(count == 6 for count in regular_lines.values())
    assert 6 * len(regular_lines) == n*n - exceptional
    curves += 1
    zero_ordinate_curves += any(y == 0 and x != 0 for x, y in points)

assert zero_ordinate_curves
print(f'{curves} curvas; {pairs} pares; massas e secantes conferidas; '
      f'{zero_ordinate_curves} curvas com ordenada zero admissível.')
