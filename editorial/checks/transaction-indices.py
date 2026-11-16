"""Confere índices, varints e comprimentos dos exemplos de transacções.

A opção --source compila apenas o cabeçalho original de varints em /tmp.
As contas não verificam uma transacção criptográfica nem o estado da rede.
"""
import argparse
from pathlib import Path
from random import Random
import subprocess
from tempfile import TemporaryDirectory


def varint(n):
    assert 0 <= n < 2**64
    groups = []
    while n >= 128:
        groups.append((n % 128) + 128)
        n //= 128
    return bytes(groups + [n])


def read_varint(data, position=0):
    value, shift = 0, 0
    while position < len(data):
        byte = data[position]
        position += 1
        value += (byte & 127) << shift
        if byte < 128:
            if shift and byte == 0:
                raise ValueError('representação não canónica')
            if value >= 2**64:
                raise ValueError('fora de 64 bits')
            return value, position
        shift += 7
    raise ValueError('varint incompleto')


def relative(indices):
    assert indices and 0 <= indices[0] < 2**64
    assert all(a < b < 2**64 for a, b in zip(indices, indices[1:]))
    return [indices[0]] + [b-a for a, b in zip(indices, indices[1:])]


def absolute(offsets):
    result, acc = [], 0
    for delta in offsets:
        acc += delta
        assert acc < 2**64
        result.append(acc)
    return result


def encode_vector(values):
    return varint(len(values)) + b''.join(varint(n) for n in values)


def read_vector(data):
    count, cursor = read_varint(data)
    result = []
    for _ in range(count):
        value, cursor = read_varint(data, cursor)
        result.append(value)
    assert cursor == len(data)
    return result


def extra_examples():
    # Etiquetas, contagens e bytes de pontos; a validade dos pontos é exterior.
    R, R0, R1 = (bytes([tag])*32 for tag in [3, 5, 7])
    encrypted = bytes(range(8))
    body = (b'\x01' + R + b'\x04' + varint(2) + R0 + R1
            + b'\x02' + varint(9) + b'\x01' + encrypted)
    assert len(body) == 110 and varint(len(body)) == b'\x6e'
    assert len(varint(len(body)) + body) == 111
    assert len(b'\x01' + R) == 33 and varint(33) == b'\x21'
    assert body[0] == 1 and body[33] == 4 and body[99] == 2
    count, pos = read_varint(body, 34)
    assert count == 2 and body[pos:pos+32] == R0
    assert body[pos+32:pos+64] == R1
    count, pos = read_varint(body, 100)
    assert count == 9 and body[pos:pos+count] == b'\x01' + encrypted


def native_check(source, numbers):
    header = source.resolve() / 'src/common/varint.h'
    assert header.is_file()
    code = r'''
#include <cstdint>
#include <iostream>
#include <iomanip>
#include <iterator>
#include "varint.h"
int main() {
    uint64_t n;
    while (std::cin >> n) {
        const auto bytes = tools::get_varint_data(n);
        for (unsigned char b: bytes)
            std::cout << std::hex << std::setw(2) << std::setfill('0') << unsigned(b);
        auto first = bytes.begin();
        auto last = bytes.end();
        uint64_t recovered = 0;
        const int count = tools::read_varint(first, last, recovered);
        if (count != int(bytes.size()) || recovered != n || first != bytes.end()) return 2;
        std::cout << std::endl;
    }
}
'''
    with TemporaryDirectory(prefix='ztm-varint-') as temp:
        temp = Path(temp)
        (temp / 'check.cpp').write_text(code)
        subprocess.run(['g++', '-std=c++17', '-O2', '-I', str(header.parent),
                        str(temp / 'check.cpp'), '-o', str(temp / 'check')], check=True)
        result = subprocess.run([str(temp / 'check')],
                                input='\n'.join(map(str, numbers))+'\n',
                                text=True, capture_output=True, check=True)
        assert result.stdout.splitlines() == [varint(n).hex() for n in numbers]
    print(f'{len(numbers)} varints coincidem com a escrita e leitura C++ originais.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path)
    args = parser.parse_args()
    rng = Random(20261116)
    numbers = sorted({0, 1, 127, 128, 250, 2**64-1}
                     | {n for k in range(1, 10) for n in (2**(7*k)-1, 2**(7*k), 2**(7*k)+1)}
                     | {rng.randrange(2**64) for _ in range(1024)})
    for n in numbers:
        encoded = varint(n)
        assert read_varint(encoded) == (n, len(encoded))
        assert len(encoded) == max(1, (n.bit_length()+6)//7)
    for _ in range(512):
        indices = sorted(rng.sample(range(2**48), 16))
        offsets = relative(indices)
        assert absolute(offsets) == indices
        assert absolute(read_vector(encode_vector(offsets))) == indices
        # A entrada contém tipo, classe, vector e imagem; a soma reinicia aqui.
        image = bytes(rng.randrange(256) for _ in range(32))
        entry = b'\x02\x00' + encode_vector(offsets) + image
        assert absolute(read_vector(entry[2:-32])) == indices
    assert relative([7, 130, 150, 400]) == [7, 123, 20, 250]
    assert encode_vector([7, 123, 20, 250]).hex() == '04077b14fa01'
    assert len(encode_vector([7, 130, 150, 400])) == 8
    assert relative([0, 1, 7]) == [0, 1, 6]
    assert varint(16).hex() == '10'
    extra_examples()
    print(f'512 anéis; {len(numbers)} varints; exemplos de índices e extra conferidos.')
    if args.source:
        native_check(args.source, numbers)


if __name__ == '__main__':
    main()
