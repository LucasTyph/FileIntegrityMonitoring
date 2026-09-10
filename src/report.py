def print_report(diff: dict[str, list]):
    separator_a = "=========================="
    separator_b = "--------------------------"

    sections = [
        ("created", "CREATED", "+"),
        ("modified", "MODIFIED", "~"),
        ("deleted", "DELETED", "-"),
    ]

    print(separator_a)
    for key, label, sign in sections:
        entries = diff[key]
        if not entries:
            print(f"[{sign}] {label} (0 files)")
        else:
            print(f"[{sign}] {label} ({len(entries)} file{'s' if len(entries) != 1 else ''})")
            print()
    
            for entry in entries:
                print(f"  {sign} {entry}")
        print(separator_b)
    print(separator_a)

        