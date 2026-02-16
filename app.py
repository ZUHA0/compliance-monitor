from flask import Flask, jsonify
from log_analyzer import load_logs
from rule_engine import load_rules, check_failed_logins

app = Flask(__name__)

@app.route("/")
def home():
    return "Compliance Monitoring API Running 🚀"

@app.route("/check-compliance")
def check_compliance():
    logs_df = load_logs("data/logs.json")
    rules = load_rules("data/rules.json")

    violations = check_failed_logins(
        logs_df,
        rules["max_failed_logins"]
    )

    if violations:
        return jsonify({
            "status": "Violation Found",
            "violations": violations
        })
    else:
        return jsonify({
            "status": "System Compliant"
        })

if __name__ == "__main__":
    app.run(debug=True)
