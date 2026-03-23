import requests
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
RESULT_FILE=os.path.join(BASE_DIR,"scan_results.txt")
def run_dast():
    issues = []
    url = "http://localhost:5000"

    try:
        r = requests.get(url)
        headers = r.headers

        print("\nDAST Scan Results:\n")

        if "Content-Security-Policy" not in headers:
            issues.append("[MEDIUM] Missing Content-Security-Policy header")

        if "X-Frame-Options" not in headers:
            issues.append("[LOW] Missing X-Frame-Options header")

    except Exception as e:
        issues.append(f"[HIGH] App not reachable: {e}")

    return issues


if __name__ == "__main__":
    results = run_dast()

    with open(RESULT_FILE, "a") as f:
        for issue in results:
            f.write(issue + "\n")

    for r in results:
        print(r)
