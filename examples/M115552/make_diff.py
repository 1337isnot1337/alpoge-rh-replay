"""Regenerate the M115552 diff from the original archive and the revised module."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
MODULE = "Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.MemOfClosed"
SOURCE = Path("src") / Path(*MODULE.split(".")).with_suffix(".lean")


def check_hash(data, expected, label):
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError(f"{label}: SHA-256 mismatch")
    return data


def inputs(project, receipt):
    hashes = receipt["sha256"]
    original = check_hash((project / SOURCE).read_bytes(), hashes["published"], "published source")
    revised = check_hash((HERE / "MemOfClosed.lean").read_bytes().replace(b"\r\n", b"\n"), hashes["revised"], "revised source")
    return original, revised


def regenerate(project, receipt):
    original, revised = inputs(project, receipt)
    path = SOURCE.as_posix().encode()
    patch = difflib.diff_bytes(difflib.unified_diff, original.splitlines(True), revised.splitlines(True),
                               fromfile=b"a/" + path, tofile=b"b/" + path)
    return check_hash(b"".join(patch), receipt["sha256"]["diff"], "diff")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="lean/ directory of the original archive")
    output = parser.add_mutually_exclusive_group()
    output.add_argument("-o", "--output", type=Path)
    output.add_argument("--check", action="store_true", help="only check the source and diff digests")
    args = parser.parse_args()
    diff = regenerate(args.project, json.loads((HERE / "receipt.json").read_text()))
    if args.output:
        args.output.write_bytes(diff)
    elif not args.check:
        sys.stdout.buffer.write(diff)
