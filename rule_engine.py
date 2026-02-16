import json

def load_rules(file_path):
    with open(file_path, 'r') as file:
        rules = json.load(file)
    return rules

def check_failed_logins(df, max_limit):
    violations = []

    failed_logins = df[df['action'] == 'login_failed']
    count_by_user = failed_logins.groupby('user').size()

    for user, count in count_by_user.items():
        if count > max_limit:
            violations.append({
                "user": user,
                "violation": "Too many failed login attempts",
                "count": count
            })

    return violations
