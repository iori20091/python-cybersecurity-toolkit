#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def run_script(script, arguments=None):

    command = [
        sys.executable,
        str(BASE_DIR / script)
    ]

    if arguments:
        command.extend(arguments)

    subprocess.run(command)


def main():

    while True:

        print("\n" + "=" * 45)
        print(" CYBERSECURITY AUTOMATION TOOLKIT")
        print("=" * 45)

        print("1. TCP Port Scanner")
        print("2. SHA-256 Hash Checker")
        print("3. Password Security Checker")
        print("4. Log Analyzer")
        print("5. Exit")

        choice = input(
            "\nSelect an option: "
        ).strip()

        if choice == "1":

            target = input(
                "Target: "
            ).strip()

            start = (
                input("Start port [1]: ").strip()
                or "1"
            )

            end = (
                input("End port [1024]: ").strip()
                or "1024"
            )

            run_script(
                "port_scanner.py",
                [
                    target,
                    "--start",
                    start,
                    "--end",
                    end
                ]
            )

        elif choice == "2":

            file_path = input(
                "File path: "
            ).strip()

            run_script(
                "hash_checker.py",
                [file_path]
            )

        elif choice == "3":

            run_script(
                "password_checker.py"
            )

        elif choice == "4":

            file_path = input(
                "Log file path: "
            ).strip()

            run_script(
                "log_analyzer.py",
                [file_path]
            )

        elif choice == "5":

            print("Exiting toolkit.")
            break

        else:

            print("[!] Invalid option.")


if __name__ == "__main__":
    main()