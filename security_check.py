import os

def scan_files():
    issues = []

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)

                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                for i, line in enumerate(lines):
                    # Detect debug mode
                    if "debug=True" in line:
                        issues.append(f"[MEDIUM] Debug mode enabled in {file}:{i+1}")

                    # Detect hardcoded API key pattern
                    if "API_KEY" in line:
                        issues.append(f"[HIGH] Possible hardcoded API key in {file}:{i+1}")

    return issues


def save_results(issues):
    with open("scan_results.txt", "w") as f:
        for issue in issues:
            f.write(issue + "\n")


if __name__ == "__main__":
    results = scan_files()
    save_results(results)

    print("\n🔍 Custom Scan Results:\n")
    for r in results:
        print(r)