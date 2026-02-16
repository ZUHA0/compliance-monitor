import json
import pandas as pd

def load_logs(file_path):
    with open(file_path, 'r') as file:
        logs = json.load(file)

    df = pd.DataFrame(logs)
    return df
