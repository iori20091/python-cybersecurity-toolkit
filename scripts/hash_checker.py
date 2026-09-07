#!/usr/bin/env python3

import argparse
import hashlib
from pathlib import Path


def calculate_sha256(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()


def main():

    parser = argparse.ArgumentParser(
        description="Calculate and optionally verify a file SHA-256 hash."
    )

    parser.add_argument(
        "file",
        help="File to hash"
    )

    parser.add_argument(
        "--expected",
        help="Expected SHA-256 hash"
    )

    args = parser.parse_args()

    path = Path(args.file)

    if not path.is_file():

        print(f"[ERROR] File not found: {path}")
        return

    result = calculate_sha256(path)

    print(f"[+] File: {path}")
    print(f"[+] SHA-256: {result}")

    if args.expected:

        if result.lower() == args.expected.lower():

            print("[+] Integrity check: MATCH")

        else:

            print("[!] Integrity check: MISMATCH")


if __name__ == "__main__":
    main()