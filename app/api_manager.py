import json
import os

CONFIG_FILE = 'config.json'

def save_config(data):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(data, f)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {}