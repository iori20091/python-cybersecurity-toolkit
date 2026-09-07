#!/usr/bin/env python3

import argparse
import getpass
import re


def analyze_password(password):

    score = 0
    recommendations = []

    if len(password) >= 12:
        score += 1
    else:
        recommendations.append(
            "Use at least 12 characters."
        )

    if re.search(r"[a-z]", password):
        score += 1
    else:
        recommendations.append(
            "Add lowercase letters."
        )

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        recommendations.append(
            "Add uppercase letters."
        )

    if re.search(r"\d", password):
        score += 1
    else:
        recommendations.append(
            "Add numbers."
        )

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        recommendations.append(
            "Add special characters."
        )

    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Moderate"

    else:
        strength = "Strong"

    return strength, score, recommendations


def main():

    parser = argparse.ArgumentParser(
        description="Basic password strength checker."
    )

    parser.add_argument(
        "--password",
        help="Password to analyze. If omitted, input is hidden."
    )

    args = parser.parse_args()

    password = (
        args.password
        if args.password
        else getpass.getpass("Enter password: ")
    )

    strength, score, recommendations = analyze_password(
        password
    )

    print("\nPassword Security Assessment")
    print("-" * 35)

    print(f"Score: {score}/5")
    print(f"Strength: {strength}")

    if recommendations:

        print("\nRecommendations:")

        for item in recommendations:
            print(f"- {item}")

    else:

        print(
            "\nNo basic complexity recommendations."
        )


if __name__ == "__main__":
    main()