#!/usr/bin/env python3

import argparse
import socket


def scan_port(target, port, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((target, port))
        return result == 0

    except socket.error:
        return False

    finally:
        sock.close()


def scan_range(target, start_port, end_port):

    print(f"\n[+] Target: {target}")
    print(f"[+] Port range: {start_port}-{end_port}")
    print("-" * 45)

    open_ports = []

    for port in range(start_port, end_port + 1):

        if scan_port(target, port):

            try:
                service = socket.getservbyport(port, "tcp")

            except OSError:
                service = "unknown"

            print(f"[OPEN] {port}/tcp - {service}")

            open_ports.append(port)

    print("-" * 45)
    print(f"[+] Open ports found: {len(open_ports)}")

    return open_ports


def main():

    parser = argparse.ArgumentParser(
        description="Simple TCP port scanner for authorized lab environments."
    )

    parser.add_argument(
        "target",
        help="Target hostname or IP address"
    )

    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Starting port (default: 1)"
    )

    parser.add_argument(
        "--end",
        type=int,
        default=1024,
        help="Ending port (default: 1024)"
    )

    args = parser.parse_args()

    if not 1 <= args.start <= 65535:
        parser.error("Starting port must be between 1 and 65535.")

    if not 1 <= args.end <= 65535:
        parser.error("Ending port must be between 1 and 65535.")

    if args.start > args.end:
        parser.error(
            "Starting port cannot be greater than ending port."
        )

    scan_range(
        args.target,
        args.start,
        args.end
    )


if __name__ == "__main__":
    main()