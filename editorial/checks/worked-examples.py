"""Confere os exemplos das contas do pagamento e dos certificados de divisor.

A aritmética é independente dos geradores e dos dados da implementação.
As fórmulas de Bulletproofs+ correspondem às de bulletproofs_plus.cc;
as razões dos divisores, às de ec-gadgets/src/dlog.rs. Estes testes não
demonstram as hipóteses criptográficas nem a solidez do protocolo.
"""

from fractions import Fraction
from math import comb
from random import Random


ELL = 2**252 + 27742317777372353535851937790883648493
rng = Random(17112026)

# Coeficientes formais de G e H: a soma não depende das máscaras escolhidas.
assert 11 == 7 + 3 + 1
assert (12 + (ELL - 2) + 1) % ELL == 11
assert ELL - 2 > 2**64 - 1 and 3 * 2**64 < ELL
for amount in (7, 3):
    bits = [(amount >> i) & 1 for i in range(64)]
    assert sum(bit * 2**i for i, bit in enumerate(bits)) == amount
for _ in range(100):
    x, y_b, y_a = (rng.randrange(ELL) for _ in range(3))
    pseudo = ((y_b + y_a) % ELL, 11)
    outputs_and_fee = ((y_b + y_a) % ELL, 7 + 3 + 1)
    assert pseudo == outputs_and_fee
    assert ((x - pseudo[0]) % ELL, (11 - pseudo[1]) % ELL) == (
        (x - y_b - y_a) % ELL, 0
    )

# Duas saídas de 64 bits: y^(k+1) y^(128-k) = y^129.
for _ in range(40):
    y, z = (rng.randrange(1, ELL) for _ in range(2))
    expanded = 0
    for j, amount in enumerate((7, 3)):
        for i in range(64):
            k = 64 * j + i
            d = pow(z, 2 * (j + 1), ELL) * 2**i % ELL
            expanded += (
                ((amount >> i) & 1)
                * pow(y, k + 1, ELL) * d * pow(y, 128 - k, ELL)
            )
    assert expanded % ELL == (
        pow(y, 129, ELL) * (7 * pow(z, 2, ELL) + 3 * pow(z, 4, ELL))
    ) % ELL


P = 17


def inv(n):
    return pow(n % P, -1, P)


def add(a, b):
    if a is None:
        return b
    if b is None:
        return a
    x, y = a
    u, v = b
    if x == u and (y + v) % P == 0:
        return None
    slope = ((3 * x * x + 2) * inv(2 * y) if a == b
             else (v - y) * inv(u - x)) % P
    rx = (slope * slope - x - u) % P
    return rx, (slope * (x - rx) - y) % P


def mul(n, point):
    result = None
    for _ in range(n):
        result = add(result, point)
    return result


points = [(x, y) for x in range(P) for y in range(P)
          if (y * y - x**3 - 2 * x - 2) % P == 0]
assert len(points) + 1 == 19
a = (5, 1)
assert [mul(k, a) for k in (1, 2, 3, 4, 8, 16, 19)] == [
    (5, 1), (6, 3), (10, 6), (3, 1), (13, 7), (10, 11), None
]


def value(coeffs, point):
    c0, c1, c2, cy = coeffs
    x, y = point
    return (c0 + c1 * x + c2 * x * x + cy * y) % P


def local_order(coeffs, point):
    """Ordem do zero, usando x=x0+t na equação y(t)^2=x(t)^3+2x(t)+2."""
    x, y = point
    y_series = [y]
    rhs = [x**3 + 2*x + 2, 3*x*x + 2, 3*x, 1, 0]
    for k in range(1, 5):
        previous = sum(y_series[i] * y_series[k-i] for i in range(1, k))
        y_series.append((rhs[k] - previous) * inv(2*y) % P)
    c0, c1, c2, cy = coeffs
    f_series = [value(coeffs, point), c1 + 2*c2*x + cy*y_series[1],
                c2 + cy*y_series[2], cy*y_series[3], cy*y_series[4]]
    return next(i for i, c in enumerate(f_series) if c % P)


line = (9, -2, 0, 1)
cubic_sum = (0, 15, 1, 2)
certificate = (2, 1, 14, 5)
divisors = [
    (line, [(1, (5, 1)), (1, (6, 3)), (1, (10, 11))]),
    (cubic_sum, [(3, (5, 1)), (1, (10, 11))]),
    (certificate, [(2, (6, 3)), (1, (3, 1)), (1, (13, 10))]),
]
for coeffs, zeros in divisors:
    assert {point for point in points if value(coeffs, point) == 0} == {
        point for _, point in zeros
    }
    for multiplicity, point in zeros:
        assert local_order(coeffs, point) == multiplicity

# Divisão das rectas, reduzindo y^2 pela equação da curva.
for x, y in points:
    assert ((y-13*x+13)*(y-2*x+9) - (x-6)*(x*x+15*x+2*y)) % P == 0
    assert ((y-7*x-12)*(y-6*x) - (x-3)*(x*x+11*x+5+4*y)) % P == 0
    assert 14 * (x*x+11*x+5+4*y) % P == value(certificate, (x, y))
assert [(2 + x + 14*x*x) % P for x in (0, 1, 2)] == [2, 0, 9]
assert 11 * inv(2) % P == 14


def ratio_data(coeffs, point, slope):
    _, c1, c2, cy = coeffs
    x, y = point
    delta = (3*x*x+2-2*slope*y) % P
    numerator = (2*y*(c1+2*c2*x)+(3*x*x+2)*cy) % P
    denominator = value(coeffs, point)*delta % P
    return numerator, denominator, numerator*inv(denominator) % P


assert [ratio_data(line, (x, 6), 0) for x in (0, 7, 10)] == [
    (12, 13, 14), (6, 13, 7), (6, 3, 2)
]
assert [ratio_data(certificate, (x, 16), 0) for x in (3, 5, 9)] == [
    (9, 16, 8), (1, 6, 3), (5, 7, 8)
]
c0, c2, cy = 2, 14, 5
d0 = 12*(c0+3+9*c2+16*cy) % P
n0 = (32*(1+6*c2)+12*cy) % P
assert (d0, n0, n0*inv(d0) % P) == (16, 9, 8)

# Todas as secantes com três encontros simples e razões definidas.
regular_counts = []
for coeffs, zeros in divisors:
    count = 0
    for slope in range(P):
        for intercept in range(P):
            intersections = [(x, y) for x, y in points
                             if (y-slope*x-intercept) % P == 0]
            if len(intersections) != 3:
                continue
            if any(value(coeffs, point) == 0 for point in intersections):
                continue
            lhs = sum(ratio_data(coeffs, point, slope)[2] for point in intersections) % P
            rhs = sum(m*inv(intercept-y+slope*x) for m, (x, y) in zeros) % P
            assert lhs == rhs
            count += 1
    regular_counts.append(count)

# Desafios que distinguem os dois dados falsos explicitamente apresentados.
assert [ratio_data(line, point, 6) for point in ((3, 16), (7, 6), (9, 1))] == [
    (16, 14, 6), (6, 9, 12), (3, 6, 9)
]
assert (12+11+4) % P == 10 and (12+11+13) % P == 2
table = [a, mul(2, a), mul(4, a)]
minus_w = (13, 10)
for slope, intercept, expected in [(0, 16, [8, 4, 8, 3]), (2, 15, [5, 5, 6, 11])]:
    weights = [inv(intercept-y+slope*x) for x, y in table+[minus_w]]
    assert weights == expected
    honest = (2*weights[1]+weights[2]+weights[3]) % P
    false = (weights[0]+2*weights[1]+weights[3]) % P
    assert (honest, false) == ((2, 2) if slope == 0 else (10, 9))

# Capacidades e caminhos, com índices a começar em zero.
for size, expected in ((684, [18, 1]), (685, [19, 2, 1])):
    layers = []
    while size > 1:
        width = (38, 18)[len(layers) % 2]
        size = (size+width-1)//width
        layers.append(size)
    assert layers == expected
for index, expected in [(681, [(17, 35), (0, 17), (0, 0)]),
                        (684, [(18, 0), (1, 0), (0, 1)])]:
    path = []
    for width in (38, 18, 38):
        index, position = divmod(index, width)
        path.append((index, position))
    assert path == expected

# Cotas numéricas: comparação exacta das fracções, sem arredondar por defeito.
p_e = 2**255-19
p_s = 2**255-11686397589588510723982429389243424941
assert [comb(s, 2)+2*s-1 for s in (508, 512)] == [129793, 131839]


def error_bound(field, n_aff, s):
    exceptional = comb(s, 2)+2*s-1
    return Fraction(4*(4*n_aff+6*field*exceptional), (n_aff-2)**2)


wei = error_bound(p_e, 8*ELL-1, 508)
helios = error_bound(p_e, p_s-1, 512)
selene = error_bound(p_s, p_e-1, 512)
assert wei < Fraction(539, 10**73)
assert max(helios, selene) < Fraction(547, 10**73)
rounded_union = 5*Fraction(539, 10**73)+2*Fraction(547, 10**73)+Fraction(38, 2**255-20)
assert rounded_union < Fraction(38, 10**71)

# TxTangle: quatro participantes, S={0,2}; fixam-se todos os termos salvo
# um que atravessa o corte. Ambas as orientações permutam todos os resíduos.
subset = {0, 2}
fixed_terms = {(0, 1): 3, (0, 2): 7, (0, 3): 5,
               (1, 2): 11, (1, 3): 2, (2, 3): 13}
for variable_edge in ((0, 3), (1, 2)):
    histogram = [0] * 19
    for varied_term in range(19):
        terms = dict(fixed_terms)
        terms[variable_edge] = varied_term
        offsets = [0] * 4
        cut = 0
        for (u, v), term in terms.items():
            offsets[u] += term
            offsets[v] -= term
            if u in subset and v not in subset:
                cut += term
            if v in subset and u not in subset:
                cut -= term
        residue = sum(offsets[u] for u in subset) % 19
        assert residue == cut % 19
        assert sum(offsets) == 0
        histogram[residue] += 1
    assert histogram == [1] * 19
    assert Fraction(histogram[0], sum(histogram)) == Fraction(1, 19)

print('Pagamento 11=7+3+1, 100 escolhas de máscaras e 40 combinações de pesos conferidos.')
print('Divisores em F17: zeros e multiplicidades, divisões, tabelas, D0/N0 e interpolação conferidos.')
print('Identidades conferidas em todas as secantes regulares:', regular_counts)
print('Crescimento 684/685, caminhos 681/684 e cotas numéricas conferidos exactamente.')
print('TxTangle: 38 escolhas de um termo do corte, resíduo uniforme e soma global nula.')
