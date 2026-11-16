"""Contas de F8: mensagens, polinómios e distribuição da apresentação.

Usa apenas a biblioteca padrão de Python. Com --rust-source, compila em /tmp
uma cópia das duas funções de contagem da fonte, sem alterar o repositório.
Os testes algébricos não estabelecem hipóteses criptográficas.
"""
import argparse
from itertools import product
from pathlib import Path
from random import Random
import re
import subprocess
import tempfile


def pow2(value):
    return 1 << (value - 1).bit_length()


def dimensions(n, depth):
    return (pow2(max(256, n * (97 + 52 * ((depth - 1) // 2)))),
            pow2(max(128, n, 32 * n * (depth // 2))))


def formula(n, depth):
    ms, mh = dimensions(n, depth)
    a, b, odd = (depth - 1) // 2, depth // 2, depth % 2
    ss = n * b + odd + (n * (2304 + 512 * a) + ms - 1) // ms
    sh = n * (b - 1 + odd) + 1 - odd + (512 * n * b + mh - 1) // mh
    assert ss - (n * b + odd) <= 24
    assert sh - (n * (b - 1 + odd) + 1 - odd) <= 16
    assert n * b + odd + n * (b - 1 + odd) + 1 - odd == n * (depth - 1) + 1
    membership = 32 * (4 * (ss + sh) + 28
                       + 2 * (ms.bit_length() - 1 + mh.bit_length() - 1))
    return ms, mh, ss, sh, membership, membership + 480 * n


def enumerate_messages(n, depth):
    rows = dimensions(n, depth)
    branches = [set(), set()]
    words = [0, 0]
    capacity = 1
    certificates = [0, 0, 0]  # Wei25519, Helios, Selene
    for level in range(1, depth + 1):
        curve = (level - 1) % 2
        capacity *= 38 if curve == 0 else 18
        for input_number in range(n):
            branches[curve].add((level, 0 if level == depth else input_number))
            words[curve] += 18 if level == 1 else 4
            certificates[0 if level == 1 else (1 if curve == 0 else 2)] += (
                5 if level == 1 else 1)
    commitments = []
    element_count = 2  # Um ponto e um escalar no fecho da raiz.
    for curve, m in enumerate(rows):
        # Acomodação por blocos de 128 posições, depois dos ramos separados.
        occupied = {index // (m // 128) for index in range(words[curve])}
        s = len(branches[curve]) + len(occupied)
        commitments.append(s)
        d = 2 * s + 2
        messages = ["K"] * s + ["AI", "AO", "S"]
        messages += [f"T{i}" for i in range(s + 1, 2 * d + 3) if i != d]
        messages += ["tau", "mu", "t"]
        while m > 1:
            messages += ["L", "R"]
            m //= 2
        messages += ["a", "b"]
        element_count += len(messages)
    a, b = (depth - 1) // 2, depth // 2
    assert certificates == [5 * n, n * a, n * b]
    assert sum(certificates) == n * (depth + 4)
    assert capacity == 38 ** (a + 1) * 18 ** b
    return *rows, *commitments, 32 * element_count, 32 * (element_count + 15 * n)


def polynomial_checks():
    rng = Random(82026)
    prime = 65537
    cases = 0
    for s in range(7):
        d = 2 * s + 2
        left_support = {s + 1, d, d + 1} | {d - k for k in range(1, s + 1)}
        right_support = {0, s + 1, d + 1} | set(range(1, s + 1))
        assert len(left_support) == len(right_support) == s + 3
        for m in range(1, 7):
            left = {i: [rng.randrange(prime) for _ in range(m)] for i in left_support}
            right = {i: [rng.randrange(prime) for _ in range(m)] for i in right_support}
            coefficients = [0] * (2 * d + 3)
            multiplications = 0
            for i, lv in left.items():
                for j, rv in right.items():
                    for x, y in zip(lv, rv):
                        coefficients[i + j] = (coefficients[i + j] + x * y) % prime
                        multiplications += 1
            assert multiplications == m * (s + 3) ** 2
            for challenge in [0, 1, 2, 17, prime - 1, rng.randrange(prime)]:
                evaluate = lambda values: [
                    sum(v[k] * pow(challenge, i, prime) for i, v in values.items()) % prime
                    for k in range(m)]
                l_eval, r_eval = evaluate(left), evaluate(right)
                actual = sum(x * y for x, y in zip(l_eval, r_eval)) % prime
                expected = sum(t * pow(challenge, i, prime)
                               for i, t in enumerate(coefficients)) % prime
                assert actual == expected
                cases += 1
    assert 256 * 16 ** 2 + 128 * 8 ** 2 == 73728
    assert 5 * 33282 + 2 * 34322 == 235054
    return cases


def presentation_checks():
    # O grupo aditivo Z_19 basta para conferir a bijecção, sem hipótese de DLOG.
    q = 19
    G, T, U, V = 1, 2, 3, 4
    image, pseudo = 9, 12
    count = 0
    for x, y, commitment in [(3, 7, 8), (5, 2, 11)]:
        O = (x * G + y * T) % q
        J = image * pow(x, -1, q) % q
        rC = (pseudo - commitment) * pow(G, -1, q) % q
        assert x * J % q == image
        assert (commitment + rC * G) % q == pseudo
        presentations = set()
        for rO, rJ, rR, rP in product(range(q), repeat=4):
            Ot = (O + rO * T) % q
            Jt = (J + rJ * U) % q
            R = (rJ * V + rR * T) % q
            P = (x * G + rJ * V + x * rJ * U + rP * T) % q
            presentations.add(Ot + q * (Jt + q * (R + q * P)))
            count += 1
        assert len(presentations) == q ** 4
    return count


def rust_function(source, name):
    match = re.search(r"pub (?:const )?fn " + name + r"\(", source)
    assert match is not None
    start = match.start()
    opening = source.index("{", match.end())
    depth = 1
    end = opening + 1
    while depth:
        depth += (source[end] == "{") - (source[end] == "}")
        end += 1
    return source[start:end]


def compare_rust(repository):
    source = (repository / "crypto/fcmps/src/lib.rs").read_text()
    tape = (repository / "crypto/fcmps/src/tape.rs").read_text()
    constants = re.findall(r"^const C[12]_\w+: usize = \d+;", source, re.M)
    assert len(constants) == 5
    word = re.search(r"const COMMITMENT_WORD_LEN: usize = \d+;", tape).group()
    code = "\n".join(constants + [word, "struct Fcmp;", "impl Fcmp {",
        rust_function(source, "ipa_rows"), rust_function(source, "proof_size"), "}"])
    code += """
fn main() {
    for n in 1..=64 {
        for layers in 1..=32 {
            let (ms, mh) = Fcmp::ipa_rows(n, layers);
            println!("{} {} {} {} {}", n, layers, ms, mh, Fcmp::proof_size(n, layers));
        }
    }
}
"""
    with tempfile.TemporaryDirectory(prefix="ztm-F8-rust-") as tmp:
        work = Path(tmp)
        (work / "counts.rs").write_text(code)
        subprocess.run(["rustc", "--edition=2021", "-O", str(work / "counts.rs"),
                        "-o", str(work / "counts")], check=True)
        lines = subprocess.check_output([str(work / "counts")], text=True).splitlines()
    for line in lines:
        n, depth, ms, mh, size = map(int, line.split())
        result = formula(n, depth)
        assert (ms, mh, size) == (result[0], result[1], result[4])
    return len(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rust-source", type=Path)
    args = parser.parse_args()
    for n in range(1, 65):
        for depth in range(1, 33):
            assert formula(n, depth) == enumerate_messages(n, depth)
    expected = {
        (1, 3): (256, 128, 13, 5, 4160, 4640),
        (2, 3): (512, 128, 14, 10, 4992, 5952),
        (1, 8): (256, 128, 19, 20, 6848, 7328),
        (1, 9): (512, 128, 14, 20, 6272, 6752),
        (1, 10): (512, 256, 14, 15, 5696, 6176),
    }
    for configuration, values in expected.items():
        assert formula(*configuration) == values
    assert formula(1, 8)[-1] - formula(1, 9)[-1] == 576
    print("2048 configurações: compromissos, mensagens, certificados e capacidade conferidos.")
    print(f"{polynomial_checks()} avaliações de polinómios e respectivos custos conferidos.")
    print(f"{presentation_checks()} apresentações: bijecção e enunciado fixo conferidos.")
    if args.rust_source:
        print(f"{compare_rust(args.rust_source)} contagens comparadas com as funções Rust da fonte.")


if __name__ == "__main__":
    main()
