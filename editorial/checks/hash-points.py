"""Receitas de pontos: contas no corpo e comparação facultativa com a fonte C.

A execução simples usa a biblioteca padrão e confere os exemplos do livro.
--source compila as funções originais em directório temporário; requer gcc,
libsodium e cabeçalhos de Boost/libsodium. --include acrescenta uma pasta de
cabeçalhos extraídos localmente. Os repositórios de fontes ficam intactos.
Estas verificações cobrem identidades e exemplos, não hipóteses de segurança.
"""
import argparse
import ctypes
import ctypes.util
import hashlib
from pathlib import Path
import random
import subprocess
import tempfile

WRAPPER = r'''
#include "crypto-ops.h"
#include "hash-ops.h"
#include "blake2b.h"
void ztm_map(const unsigned char *in, unsigned char *out, int clear) {
    ge_p2 p;
    ge_fromfe_frombytes_vartime(&p, in);
    if (clear) {
        ge_p1p1 q;
        ge_p3 r;
        ge_mul8(&q, &p);
        ge_p1p1_to_p3(&r, &q);
        ge_p3_tobytes(out, &r);
    } else ge_tobytes(out, &p);
}
int ztm_decode_mul8(const unsigned char *in, unsigned char *out) {
    ge_p3 p;
    if (ge_frombytes_vartime(&p, in) != 0) return -1;
    ge_p2 p2;
    ge_p1p1 q;
    ge_p3 r;
    ge_p3_to_p2(&p2, &p);
    ge_mul8(&q, &p2);
    ge_p1p1_to_p3(&r, &q);
    ge_p3_tobytes(out, &r);
    return 0;
}
'''

q=2**255-19
A=486662
d=-121665*pow(121666,-1,q)%q
ell=2**252+27742317777372353535851937790883648493
ii=pow(2,(q-1)//4,q)
identity=(0,1)
def sqrt(value):
    root=pow(value,(q+3)//8,q)
    if root*root%q != value:
        root=root*ii%q
    assert root*root%q == value
    return root
def add(P,Q):
    x,y=P; u,v=Q
    product=d*x*u*y*v%q
    return ((x*v+y*u)*pow(1+product,-1,q)%q,
            (y*v+x*u)*pow(1-product,-1,q)%q)
def mul(n,P):
    out=identity
    while n:
        if n&1: out=add(out,P)
        P=add(P,P)
        n>>=1
    return out
def encode(P):
    x,y=P
    return (y|((x&1)<<255)).to_bytes(32,"little")
def decode(blob):
    raw=int.from_bytes(blob,"little")
    y=raw&((1<<255)-1);sign=raw>>255
    assert y<q
    square=(y*y-1)*pow(d*y*y+1,-1,q)%q
    x=sqrt(square)
    if x&1 != sign:x=(-x)%q
    assert not (x==0 and sign)
    return x,y
def map_integer(blob):
    u=int.from_bytes(blob,"little")%q
    v=2*u*u%q
    w=(v+1)%q
    t=(w*w-A*A*v)%q
    r=w*pow(t,-1,q)%q
    square=pow(r,(q-1)//2,q)==1
    if square:
        z=-A*v%q
        rad=A*(A+2)*v*r%q
        parity=0
    else:
        z=-A%q
        rad=A*(A+2)*r%q
        parity=1
    x=sqrt(rad)
    if x&1 != parity:x=(-x)%q
    y=(z-w)*pow(z+w,-1,q)%q
    assert (-x*x+y*y-1-d*x*x*y*y)%q==0
    return x,y


class Native:
    def __init__(self, source, work, include):
        (work / "wrapper.c").write_text(WRAPPER)
        command = ["gcc", "-O2", "-fPIC", "-shared"]
        paths = [*include, source / "src/crypto", source / "contrib/epee/include",
                 source / "src/crypto/crypto_ops_builder/include"]
        command += ["-I" + str(path) for path in paths]
        command += [str(work / "wrapper.c")]
        command += [str(source / "src/crypto" / name) for name in
                    ["crypto-ops.c", "crypto-ops-data.c", "hash.c",
                     "keccak.c", "blake2b.c"]]
        sodium = ctypes.util.find_library("sodium")
        if not sodium:
            raise RuntimeError("A comparação C requer a biblioteca libsodium.")
        command += [str(source / "contrib/epee/src/memwipe.c"),
                    "-l:" + sodium, "-o", str(work / "checks.so")]
        subprocess.run(command, check=True)
        self.lib = ctypes.CDLL(str(work / "checks.so"))
        self.buf = ctypes.c_ubyte * 32

    def map(self, blob, clear):
        out = self.buf()
        self.lib.ztm_map(self.buf.from_buffer_copy(blob), out, clear)
        return bytes(out)

    def keccak(self, blob):
        out = self.buf()
        self.lib.cn_fast_hash(ctypes.c_char_p(blob), ctypes.c_size_t(len(blob)), out)
        return bytes(out)

    def blake(self, blob):
        out = (ctypes.c_ubyte * 64)()
        assert self.lib.blake2b_monero(
            out, ctypes.c_size_t(64), ctypes.c_char_p(blob),
            ctypes.c_size_t(len(blob)), None, ctypes.c_size_t(0)) == 0
        return bytes(out)

    def decode_mul8(self, blob):
        out = self.buf()
        assert self.lib.ztm_decode_mul8(self.buf.from_buffer_copy(blob), out) == 0
        return bytes(out)


def check(native=None):
    for value, residue in [(2, -1), (A * (A + 2), -1),
                           (2 * A * (A + 2), 1), (A - 1, 1)]:
        assert pow(value, (q - 1) // 2, q) == residue % q
    assert map_integer(bytes(32)) == (0, q - 1)
    assert mul(8, map_integer(bytes(32))) == identity
    rng = random.Random(16112026)
    values = [0, 1, 2, q-1, q, q+1, 2*q-1, 2*q, 2**255, 2**256-1]
    values += [rng.randrange(2**256) for _ in range(512)]
    branches = set()
    for value in values:
        blob = value.to_bytes(32, "little")
        point = map_integer(blob)
        branches.add(point[0] & 1)
        assert map_integer(((-value) % q).to_bytes(32, "little")) == point
        assert decode(encode(point)) == point
        if native:
            assert encode(point) == native.map(blob, 0), value
            assert encode(mul(8, point)) == native.map(blob, 1), value
            assert native.blake(blob) == hashlib.blake2b(
                blob, digest_size=64, person=b"Monero").digest()
    assert branches == {0, 1}
    G = decode(bytes.fromhex("58" + "66" * 31))
    digest = bytes.fromhex(
        "1e609dc09abbd7bca35029ffbf164d05496b441a97d9f13020d869762acd0ee1")
    Q = decode(digest)
    doublings = [
        "5e80078173851a4aeb1563aa6e0da45729dc453e7ca922bab939d011e57af412",
        "1cdf7620c9ba31e2f191f689d1bfbec2ee5d111c126a289d8ded73da456f82a6",
        "8b655970153799af2aeadc9ff1add0ea6c7251d54154cfa92c173a0dd39c1f94",
    ]
    for n, expected in zip([2, 4, 8], doublings):
        assert encode(mul(n, Q)).hex() == expected
    H = mul(8, Q)
    hp1 = mul(8, map_integer(digest))
    blake = hashlib.blake2b(encode(G), digest_size=64, person=b"Monero").digest()
    hp2 = mul(8, add(map_integer(blake[:32]), map_integer(blake[32:])))
    assert encode(hp1).hex() == (
        "d6329b5b1f7c0805b5c345f4957554002a2f557845f64d7645dae0e051a6498a")
    assert encode(hp2).hex() == (
        "aa542c6b29f67c68c8f747f808dd81b09f3265fdcb2595868a151d85c8dfe418")
    for point in [G, H, hp1, hp2]:
        assert point != identity and mul(ell, point) == identity
    if native:
        assert native.keccak(encode(G)) == digest
        assert native.keccak(b"").hex() == (
            "c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470")
        assert native.decode_mul8(digest) == encode(H)
        assert native.blake(encode(G)) == blake
    print(f"{len(values)} argumentos; dois ramos; redução dos 256 bits; "
          "simetria; resíduos; descompressão; exemplos de H e H_p conferidos.")
    if native:
        print("As imagens, hashes e duplicações coincidem com as funções C da fonte.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--include", type=Path, action="append", default=[])
    args = parser.parse_args()
    if args.source:
        with tempfile.TemporaryDirectory(prefix="ztm-hash-points-") as work:
            check(Native(args.source, Path(work), args.include))
    else:
        check()


if __name__ == "__main__":
    main()
