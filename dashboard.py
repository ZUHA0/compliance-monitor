import streamlit as st
from log_analyzer import load_logs
from rule_engine import load_rules, check_failed_logins

st.title("🔍 Automated Compliance Monitoring Dashboard")

logs_df = load_logs("data/logs.json")
rules = load_rules("data/rules.json")

violations = check_failed_logins(
    logs_df,
    rules["max_failed_logins"]
)

st.subheader("System Logs")
st.dataframe(logs_df)

st.subheader("Compliance Status")

if violations:
    st.error("⚠ Violations Detected!")
    st.write(violations)
else:
    st.success("✅ System Compliant")
