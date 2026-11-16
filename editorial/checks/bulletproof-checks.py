"""Verifica separadamente as identidades de valor e de produto interno.

As contas usam vectores de coeficientes em bases formais independentes.
Assim, um sinal incorrecto não se pode esconder numa relação entre bases
escolhidas para um pequeno exemplo. O teste não estabelece segurança.
"""
from random import Random


def check_field(p):
    rng = Random(p + 16112026)
    count, rounds = 0, 0
    for n in [2, 4, 8, 16, 64]:
        size = 2*n + 2
        zero = (0,) * size

        def plus(*points):
            return tuple(sum(words) % p for words in zip(*points))

        def scale(a, point):
            return tuple(a*v % p for v in point)

        def msm(values, points):
            return tuple(sum(a*point[j] for a, point in zip(values, points)) % p
                         for j in range(size))

        def dot(a, b):
            return sum(x*y for x, y in zip(a, b)) % p

        basis = [tuple(int(i == j) for i in range(size)) for j in range(size)]
        G, H = basis[:2]
        gs, hs = basis[2:2+n], basis[2+n:]
        for _ in range(12):
            bits = [rng.randrange(2) for _ in range(n)]
            rights = [(b-1) % p for b in bits]
            sL, sR = [[rng.randrange(p) for _ in range(n)] for _ in range(2)]
            alpha, rho, gamma, tau1, tau2 = [rng.randrange(p) for _ in range(5)]
            x, y, z, xip = [rng.randrange(1, p) for _ in range(4)]
            powers_y = [pow(y, i, p) for i in range(n)]
            inv_y = [pow(v, -1, p) for v in powers_y]
            powers_2 = [pow(2, i, p) for i in range(n)]
            value = dot(bits, powers_2)
            V = plus(scale(gamma, G), scale(value, H))
            A = plus(scale(alpha, G), msm(bits, gs), msm(rights, hs))
            S = plus(scale(rho, G), msm(sL, gs), msm(sR, hs))
            l0 = [(b-z) % p for b in bits]
            r0 = [(yy*(b+z) + z*z*two) % p
                  for yy, b, two in zip(powers_y, rights, powers_2)]
            r1 = [yy*s % p for yy, s in zip(powers_y, sR)]
            delta = ((z-z*z)*sum(powers_y) - z**3*sum(powers_2)) % p
            t0, t1, t2 = dot(l0, r0), (dot(sL, r0)+dot(l0, r1)) % p, dot(sL, r1)
            assert t0 == (z*z*value + delta) % p
            T1 = plus(scale(tau1, G), scale(t1, H))
            T2 = plus(scale(tau2, G), scale(t2, H))
            ell = [(a+x*b) % p for a, b in zip(l0, sL)]
            rr = [(a+x*b) % p for a, b in zip(r0, r1)]
            t = dot(ell, rr)
            assert t == (t0+x*t1+x*x*t2) % p
            tau = (x*tau1+x*x*tau2+z*z*gamma) % p
            mu = (alpha+x*rho) % p
            left_value = plus(scale(t, H), scale(tau, G))
            right_value = plus(scale(z*z, V), scale(delta, H),
                               scale(x, T1), scale(x*x, T2))
            assert left_value == right_value
            hp = [scale(a, b) for a, b in zip(inv_y, hs)]
            U = scale(xip, H)
            correction = [(z*yy+z*z*two) % p for yy, two in zip(powers_y, powers_2)]
            public_P = plus(A, scale(x, S), scale(-mu, G), scale(t, U),
                            msm([-z]*n, gs), msm(correction, hp))
            witness_P = plus(msm(ell, gs), msm(rr, hp), scale(t, U))
            assert public_P == witness_P
            current_P, sigma = public_P, zero
            gf, hf = gs[:], hp[:]
            k = n.bit_length()-1
            challenges = {}
            while len(ell) > 1:
                half = len(ell)//2
                la, lb = ell[:half], ell[half:]
                ra, rb = rr[:half], rr[half:]
                ga, gb, ha, hb = gf[:half], gf[half:], hf[:half], hf[half:]
                L = plus(msm(la, gb), msm(rb, ha), scale(dot(la, rb), U))
                R = plus(msm(lb, ga), msm(ra, hb), scale(dot(lb, ra), U))
                u = rng.randrange(1, p)
                ui = pow(u, -1, p)
                challenges[len(ell).bit_length()-1] = u
                term = plus(scale(u*u, L), scale(ui*ui, R))
                sigma = plus(sigma, term)
                current_P = plus(current_P, term)
                ell = [(u*a+ui*b) % p for a, b in zip(la, lb)]
                rr = [(ui*a+u*b) % p for a, b in zip(ra, rb)]
                gf = [plus(scale(ui, a), scale(u, b)) for a, b in zip(ga, gb)]
                hf = [plus(scale(u, a), scale(ui, b)) for a, b in zip(ha, hb)]
                assert current_P == plus(msm(ell, gf), msm(rr, hf), scale(dot(ell, rr), U))
                rounds += 1
            a, b = ell[0], rr[0]
            phi = []
            for i in range(n):
                coefficient = 1
                for j in range(1, k+1):
                    power = 1 if i & (1 << (j-1)) else -1
                    coefficient = coefficient * pow(challenges[j], power, p) % p
                phi.append(coefficient)
            varphi = [pow(v, -1, p) for v in phi]
            assert gf[0] == msm(phi, gs)
            assert hf[0] == msm(varphi, hp)
            final_P = plus(scale(a, gf[0]), scale(b, hf[0]), scale(a*b, U))
            assert plus(public_P, sigma) == final_P
            g_coefficients = [(-z-a*f) % p for f in phi]
            h_coefficients = [(z+yy*(z*z*two-b*f)) % p
                              for yy, two, f in zip(inv_y, powers_2, varphi)]
            final_sum = plus(A, scale(x, S), scale(-mu, G), sigma,
                             scale((t-a*b)*xip, H),
                             msm(g_coefficients, gs), msm(h_coefficients, hs))
            assert final_sum == zero
            # Cada condição depende de dados que a outra não elimina.
            assert plus(left_value, G) != right_value
            assert plus(final_sum, G) != zero
            bad_final = plus(scale(a+1, gf[0]), scale(b, hf[0]), scale((a+1)*b, U))
            assert plus(public_P, sigma) != bad_final
            count += 1
    return count, rounds


if __name__ == "__main__":
    counts = [check_field(p) for p in [101, 65537]]
    print(f"{sum(c for c, _ in counts)} provas algébricas; "
          f"{sum(r for _, r in counts)} dobras; duas condições, "
          "pesos binários e mudanças de bases conferidos.")
