"""Reconstitui as tabelas hexadecimais dos apêndices do bloco e do pagamento."""

import argparse
import json
from itertools import accumulate
from pathlib import Path
import re
from runpy import run_path

from Cryptodome.Hash import keccak


CHECKS = Path(__file__).resolve().parent
CONTENT = CHECKS.parents[1] / "translations/pt/content"
encoding = run_path(str(CHECKS / "transaction-indices.py"))
varint = encoding["varint"]
curve = run_path(str(CHECKS / "hash-points.py"))


def digest(data):
    return keccak.new(digest_bits=256, data=data).digest()


def printed_hashes(filename):
    text = (CONTENT / filename).read_text()
    halves = re.findall(r"\\texttt\{([0-9a-f]{32})\}", text)
    assert len(halves) % 2 == 0
    return [bytes.fromhex(a + b) for a, b in zip(halves[::2], halves[1::2])]


def check_payment(source):
    data = (source / "tests/data/txs/bpp_tx_e89415.bin").read_bytes()
    assert len(data) == 1539 and data[:6] == bytes.fromhex("02 00 01 02 00 10")
    cursor = 6
    distances = []
    for _ in range(16):
        distance, cursor = encoding["read_varint"](data, cursor)
        distances.append(distance)
    assert cursor == 54
    text = (CONTENT / "pagamentoTipoSeis.tex").read_text()
    printed_rows = re.findall(
        r"^(\d+) & \\texttt\{([0-9a-f ]+)\} & (\d+(?:\\,\d+)*) & (\d+(?:\\,\d+)*)",
        text, re.MULTILINE)
    offsets = [(int(i), bytes.fromhex(raw), int(d.replace(r"\,", "")),
                int(total.replace(r"\,", ""))) for i, raw, d, total in printed_rows]
    assert offsets == [(i, varint(d), d, total) for i, (d, total) in
                       enumerate(zip(distances, accumulate(distances)))]

    fee, cursor = encoding["read_varint"](data, 203)
    assert (data[202], fee, cursor) == (6, 6156000000, 208)
    assert (data[288], data[481], data[706]) == (1, 7, 7)
    left, right = data[224:256], data[256:288]
    generator = curve["decode"](bytes.fromhex(
        "8b655970153799af2aeadc9ff1add0ea6c7251d54154cfa92c173a0dd39c1f94"))
    fee_point = curve["mul"](fee, generator)
    outputs = curve["add"](curve["decode"](left), curve["decode"](right))
    pseudo = curve["encode"](curve["add"](outputs, fee_point))
    assert pseudo == data[1507:]
    prefix, base, prunable = map(digest, [data[:202], data[202:288], data[288:]])
    proof = digest(data[289:481] + data[482:706] + data[707:931])
    message = digest(prefix + base + proof)
    txid = digest(prefix + base + prunable)
    assert txid.hex() == "e89415b95564aa7e3587c91422756ba5303e727996e19c677630309a0d52a7ca"
    assert printed_hashes("pagamentoTipoSeis.tex") == [
        txid, left, right, curve["encode"](outputs), curve["encode"](fee_point),
        pseudo, prefix, base, prunable, proof, message]


def check_block():
    text = (CONTENT / "appendix.tex").read_text()
    record = text.split("print_block 1582196\n", 1)[1].split(r"\end{Verbatim}", 1)[0]
    block = json.loads(record[record.index(r"\{"):].replace(r"\{", "{").replace(r"\}", "}"))
    miner = block["miner_tx"]
    output = miner["vout"][0]
    extra = bytes(miner["extra"])
    prefix = (varint(miner["version"]) + varint(miner["unlock_time"]) + b"\x01\xff"
              + varint(miner["vin"][0]["gen"]["height"]) + b"\x01"
              + varint(output["amount"]) + b"\x02" + bytes.fromhex(output["target"]["key"])
              + varint(len(extra)) + extra)
    assert len(prefix) == 94 and miner["rct_signatures"]["type"] == 0
    miner_id = digest(digest(prefix) + digest(b"\0") + bytes(32))
    leaves = [miner_id, *map(bytes.fromhex, block["tx_hashes"])]
    assert len(leaves) == 6
    u = digest(leaves[2] + leaves[3])
    v = digest(leaves[4] + leaves[5])
    a = digest(leaves[0] + leaves[1])
    b = digest(u + v)
    root = digest(a + b)
    header = (varint(block["major_version"]) + varint(block["minor_version"])
              + varint(block["timestamp"]) + bytes.fromhex(block["prev_id"])
              + block["nonce"].to_bytes(4, "little"))
    blob = header + root + varint(len(leaves))
    assert len(blob) == 76
    block_id = digest(varint(len(blob)) + blob)
    assert block_id == bytes.fromhex(re.search(r"^hash: (\w+)$", record, re.MULTILINE)[1])
    assert printed_hashes("caminhoMerkle.tex") == [u, v, a, b, root, block_id]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Repositório C++ de Monero")
    args = parser.parse_args()
    check_payment(args.source)
    check_block()
    print("Apêndices B e E: 16 índices, balanço e 17 valores hexadecimais conferidos.")
