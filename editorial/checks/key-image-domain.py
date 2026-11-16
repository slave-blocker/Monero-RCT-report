"""Confere a decomposição, a falha de ligação e as condições dos desafios.

O grupo pequeno Z_19 x Z_8 permite percorrer todas as componentes de torção.
As contas sobre Edwards25519 conferem também os exemplos no grupo efectivo.
As assinaturas pequenas verificam a álgebra, sem pretensão de segurança.
"""
import hashlib
import importlib.util
from math import gcd
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True


spec = importlib.util.spec_from_file_location(
    "hash_points", Path(__file__).with_name("hash-points.py"))
ec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ec)

ELL = 19
ZERO = (0, 0)
G = (1, 0)


def add(p, q):
    return ((p[0] + q[0]) % ELL, (p[1] + q[1]) % 8)


def mul(n, p):
    return (n * p[0] % ELL, n * p[1] % 8)


def encoded(p):
    return bytes(p)


def challenge(prefix, left, right):
    return int.from_bytes(
        hashlib.sha256(prefix + encoded(left) + encoded(right)).digest(),
        "little") % ELL


def small_signatures():
    rng = random.Random(16112026)
    secrets = [3, 5, 11]
    keys = [mul(x, G) for x in secrets]
    bases = [(7, 0), (13, 0), (17, 0)]
    signatures = 0
    attempts = 0
    for pi in range(3):
        honest = mul(secrets[pi], bases[pi])
        images = []
        for torsion in range(8):
            image = add(honest, (0, torsion))
            order = 8 // gcd(8, torsion)
            prefix = b"bLSAG|dominio|" + b"".join(map(encoded, keys)) + encoded(image)
            for attempt in range(1000):
                attempts += 1
                alpha = rng.randrange(ELL)
                responses = [rng.randrange(ELL) for _ in keys]
                challenges = [0] * len(keys)
                i = (pi + 1) % len(keys)
                challenges[i] = challenge(
                    prefix, mul(alpha, G), mul(alpha, bases[pi]))
                while i != pi:
                    left = add(mul(responses[i], G), mul(challenges[i], keys[i]))
                    right = add(mul(responses[i], bases[i]), mul(challenges[i], image))
                    next_i = (i + 1) % len(keys)
                    challenges[next_i] = challenge(prefix, left, right)
                    i = next_i
                responses[pi] = (alpha - challenges[pi] * secrets[pi]) % ELL
                reconstructed = add(
                    mul(responses[pi], bases[pi]), mul(challenges[pi], image))
                residual = add(reconstructed, mul(-alpha, bases[pi]))
                assert residual == mul(challenges[pi], (0, torsion))
                assert (residual == ZERO) == (challenges[pi] % order == 0)
                if residual == ZERO:
                    break
            else:
                raise AssertionError("Não foi encontrado um desafio admissível.")
            # Verificação independente a partir do desafio inicial transmitido.
            c = challenges[0]
            for i in range(len(keys)):
                left = add(mul(responses[i], G), mul(c, keys[i]))
                right = add(mul(responses[i], bases[i]), mul(c, image))
                c = challenge(prefix, left, right)
            assert c == challenges[0]
            assert (mul(ELL, image) == ZERO) == (torsion == 0)
            assert mul(8, image) == mul(8, honest)
            assert mul(8 * pow(8, -1, ELL), image) == honest
            images.append(image)
            signatures += 1
        assert len(set(images)) == 8
    for t in [1, 2, 4, 8]:
        count = sum(c % t == 0 for c in range(ELL))
        assert count == (ELL + t - 1) // t
    for x in range(ELL):
        for t in range(8):
            point = (x, t)
            prime = mul(8 * pow(8, -1, ELL), point)
            torsion = add(point, mul(-1, prime))
            assert prime == (x, 0) and torsion == (0, t)
    print(f"{signatures} assinaturas em {attempts} tentativas; "
          "oito imagens por chave; rejeição das sete variantes; 152 decomposições.")


def actual_curve():
    G = ec.decode(bytes.fromhex("58" + "66" * 31))
    T = ec.decode(bytes.fromhex(
        "c7176a703d4dd84fba3c0b760d10670f2a2053fa2c39ccc64ec7fd7792ac03fa"))
    assert ec.mul(8, T) == ec.identity
    assert ec.mul(4, T) != ec.identity
    order_two = (0, ec.q - 1)
    assert ec.mul(2, order_two) == ec.identity
    J = ec.mul(8, ec.map_integer(bytes(range(32))))
    key = 123456789
    I = ec.mul(key, J)
    variants = []
    for t in range(8):
        torsion = ec.mul(t, T)
        altered = ec.add(I, torsion)
        variants.append(altered)
        assert (ec.mul(ec.ell, altered) == ec.identity) == (t == 0)
        assert ec.mul(8, altered) == ec.mul(8, I)
        assert ec.mul(8 * pow(8, -1, ec.ell), altered) == I
        order = 8 // gcd(8, t)
        for c in [0, 1, 5, 6, 8, 11, ec.ell-1]:
            alpha = 987654321
            response = (alpha - c * key) % ec.ell
            reconstructed = ec.add(ec.mul(response, J), ec.mul(c, altered))
            expected = ec.add(ec.mul(alpha, J), ec.mul(c, torsion))
            assert reconstructed == expected
            assert (reconstructed == ec.mul(alpha, J)) == (c % order == 0)
    assert len(set(variants)) == 8
    x, y = I
    assert ec.add(I, order_two) == ((-x) % ec.q, (-y) % ec.q)
    assert ec.mul(6, ec.add(I, order_two)) == ec.mul(6, I)
    assert ec.mul(5, ec.add(I, order_two)) == ec.add(ec.mul(5, I), order_two)
    print("Edwards25519: oito variantes, projecções e 56 reconstruções conferidas.")


if __name__ == "__main__":
    small_signatures()
    actual_curve()
