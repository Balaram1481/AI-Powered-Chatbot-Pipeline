import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
RESULT_FILE=os.path.join(BASE_DIR,"scan_results.txt")
REPORT_FILE=os.path.join(BASE_DIR,"scan_report.txt")

def get_suggestion(issue):
    if "API key" in issue:
        return "Use environment variables instead of hardcoding secrets", "High risk of credential exposure"

    elif "Debug mode" in issue:
        return "Disable debug mode in production", "Can expose internal application data"

    elif "Flask" in issue:
        return "Upgrade to latest secure version", "Known vulnerabilities may be exploited"

    elif "CSP" in issue:
        return "Add Content-Security-Policy headers", "Helps prevent XSS attacks"

    else:
        return "Follow secure coding practices", "General security risk"


def analyze():
    block = False
    report = "AI SecOps Final Report\n\n"

    with open(RESULT_FILE, "r", encoding="utf-8", errors="ignore") as f:
        issues = f.readlines()

    for issue in issues:
        issue = issue.strip()
        suggestion, impact = get_suggestion(issue)

        report += f"{issue}\n"
        report += f"Suggestion: {suggestion}\n"
        report += f"Impact: {impact}\n\n"

        if "[HIGH]" in issue:
            block = True

    if block:
        report += "FINAL DECISION: BLOCK DEPLOYMENT\n"
    else:
        report += "FINAL DECISION: ALLOW DEPLOYMENT\n"

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(report)

    if block:
        exit(1)


if __name__ == "__main__":
    analyze()
