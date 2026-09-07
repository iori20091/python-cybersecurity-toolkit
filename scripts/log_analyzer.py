#!/usr/bin/env python3

import argparse
import re
from collections import Counter


FAILED_PATTERNS = [
    r"Failed password",
    r"authentication failure",
    r"Invalid user",
    r"Failed login",
]


def analyze_log(file_path):

    failed_attempts = 0
    source_ips = Counter()

    with open(
        file_path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as file:

        for line in file:

            if any(
                re.search(
                    pattern,
                    line,
                    re.IGNORECASE
                )
                for pattern in FAILED_PATTERNS
            ):

                failed_attempts += 1

                ip_match = re.search(
                    r"(?:from|rhost=)\s*"
                    r"(\d{1,3}(?:\.\d{1,3}){3})",
                    line,
                    re.IGNORECASE
                )

                if ip_match:

                    source_ips[
                        ip_match.group(1)
                    ] += 1

    return failed_attempts, source_ips


def main():

    parser = argparse.ArgumentParser(
        description="Analyze authentication logs for failed attempts."
    )

    parser.add_argument(
        "logfile",
        help="Path to log file"
    )

    args = parser.parse_args()

    try:

        failed_attempts, source_ips = analyze_log(
            args.logfile
        )

    except FileNotFoundError:

        print(
            f"[ERROR] File not found: {args.logfile}"
        )

        return

    print("\nLog Security Analysis")
    print("-" * 40)

    print(
        f"Failed authentication attempts: "
        f"{failed_attempts}"
    )

    if source_ips:

        print("\nTop source IPs:")

        for ip, count in source_ips.most_common(10):

            print(
                f"- {ip}: {count} attempts"
            )

    else:

        print("\nNo source IPs identified.")


if __name__ == "__main__":
    main()