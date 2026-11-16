"""Contas pedagógicas de CLSAG: agregação, resposta e extracção.

Usa o grupo de ordem 19 da curva y²=x³+2x+2 sobre F_17 e enumera o
limite dos pesos para diferenças fixas. Não demonstra as hipóteses
criptográficas nem a redução para adversários com consultas adaptativas.
"""
from random import Random


Q, ELL = 17, 19
G = (5, 1)


def add(p, q):
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    u, v = q
    if x == u and (y + v) % Q == 0:
        return None
    slope = ((v - y) * pow((u - x) % Q, -1, Q) if x != u
             else (3*x*x + 2) * pow(2*y, -1, Q)) % Q
    new_x = (slope*slope - x - u) % Q
    return new_x, (slope*(x - new_x) - y) % Q


def mul(n, p):
    out = None
    n %= ELL
    while n:
        if n & 1:
            out = add(out, p)
        p = add(p, p)
        n >>= 1
    return out


def aggregate(weights, points):
    out = None
    for weight, point in zip(weights, points):
        out = add(out, mul(weight, point))
    return out


def worked_example():
    J = mul(7, G)
    keys = [mul(5, G), mul(9, G)]
    images = [mul(5, J), mul(9, J)]
    assert images == [mul(16, G), mul(6, G)]
    weights = [3, 4]
    w = (3*5 + 4*9) % ELL
    W = aggregate(weights, keys)
    image = aggregate(weights, images)
    assert w == 13 and W == mul(13, G)
    assert image == mul(15, G) == mul(w, J)
    alpha, challenge = 11, 6
    response = (alpha - challenge*w) % ELL
    assert response == 9
    assert add(mul(response, G), mul(challenge, W)) == mul(11, G)
    assert add(mul(response, J), mul(challenge, image)) == G == mul(11, J)


def reconstructions():
    rng = Random(16112026)
    count = 0
    for _ in range(120):
        secrets = [rng.randrange(1, ELL) for _ in range(rng.randrange(2, 7))]
        weights = [rng.randrange(ELL) for _ in secrets]
        J = mul(rng.randrange(1, ELL), G)
        keys = [mul(k, G) for k in secrets]
        images = [mul(k, J) for k in secrets]
        W = aggregate(weights, keys)
        image = aggregate(weights, images)
        w = sum(u*k for u, k in zip(weights, secrets)) % ELL
        assert W == mul(w, G) and image == mul(w, J)
        alpha = rng.randrange(ELL)
        for c in range(ELL):
            response = (alpha - c*w) % ELL
            assert add(mul(response, G), mul(c, W)) == mul(alpha, G)
            assert add(mul(response, J), mul(c, image)) == mul(alpha, J)
            c2 = (c + 1) % ELL
            r2 = (alpha - c2*w) % ELL
            extracted = (response - r2) * pow((c2-c) % ELL, -1, ELL) % ELL
            assert extracted == w
            count += 1
    return count


def fixed_difference_counts():
    differences = 0
    for e1 in range(ELL):
        for e2 in range(ELL):
            if e1 == e2 == 0:
                continue
            zeroes = sum((u*e1 + v*e2) % ELL == 0
                         for u in range(ELL) for v in range(ELL))
            assert zeroes == ELL
            differences += 1
    return differences


def reduced_coefficients():
    # Z_19 x Z_8 distingue a regra completa da factorização no subgrupo primo.
    def scale(n, p):
        return n*p[0] % 19, n*p[1] % 8
    differences = 0
    for c in range(19):
        for mu in range(19):
            coefficient = c*mu % 19
            assert scale(coefficient, (3, 0)) == scale(c, scale(mu, (3, 0)))
            if scale(coefficient, (3, 1)) != scale(c, scale(mu, (3, 1))):
                differences += 1
    assert scale(7*5 % 19, (0, 1)) == (0, 0)
    assert scale(7, scale(5, (0, 1))) == (0, 3)
    return differences


if __name__ == "__main__":
    assert len({mul(i, G) for i in range(ELL)}) == ELL
    worked_example()
    count = reconstructions()
    differences = fixed_difference_counts()
    coefficient_differences = reduced_coefficients()
    print(f"Exemplo completo; {count} reconstruções e extracções; "
          f"{differences} diferenças com exactamente 19/361 pesos admissíveis.")
    print("361 produtos de coeficientes: factorização válida no subgrupo primo; "
          f"{coefficient_differences} diferenças com componente de torção.")
