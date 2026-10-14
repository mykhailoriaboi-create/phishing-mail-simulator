def main():
    print("=" * 45)
    print("       PHISHING EMAIL SIMULATOR")
    print("=" * 45)
    print()
    print("Cybersecurity Awareness Training Tool")
    print()

from simulator.emails import EMAIL_SCENARIOS


def main():
    print("=" * 50)
    print("        PHISHING EMAIL SIMULATOR")
    print("=" * 50)
    print()

    print(f"Available scenarios: {len(EMAIL_SCENARIOS)}")
    print()

    for email in EMAIL_SCENARIOS:
        print(f"[{email['id']}] {email['company']}")
        print(f"    From: {email['sender']}")
        print(f"    Subject: {email['subject']}")
        print()

if __name__ == "__main__":
    main()


