def analyze():
    block = False
    report = "🔐 AI SecOps Final Report\n\n"

    with open("scan_results.txt", "r") as f:
        issues = f.readlines()

    for issue in issues:
        issue = issue.strip()
        report += issue + "\n"

        if "[HIGH]" in issue:
            block = True
            report += "➡ Action: Immediate fix required\n\n"

        elif "[MEDIUM]" in issue:
            report += "➡ Action: Fix soon\n\n"

        else:
            report += "➡ Action: Low priority\n\n"

    if block:
        report += "❌ FINAL DECISION: BLOCK DEPLOYMENT\n"
    else:
        report += "✅ FINAL DECISION: ALLOW DEPLOYMENT\n"

    with open("security_report.txt", "w") as f:
        f.write(report)

    print(report)

    if block:
        exit(1)


if __name__ == "__main__":
    analyze()