from log_analyzer import load_logs
from rule_engine import load_rules, check_failed_logins
import pandas as pd

def generate_report(violations):
    df = pd.DataFrame(violations)
    df.to_csv("reports/compliance_report.csv", index=False)
    print("Report generated successfully!")

def main():
    logs_df = load_logs("data/logs.json")
    rules = load_rules("data/rules.json")

    violations = check_failed_logins(
        logs_df,
        rules["max_failed_logins"]
    )

    if violations:
        generate_report(violations)
        print("Violations Found:", violations)
    else:
        print("System is compliant.")

if __name__ == "__main__":
    main()
