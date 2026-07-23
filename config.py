import json
import os

CONFIG_FILE = "config/settings.json"

def load_config():
    try:
        if not os.path.exists(CONFIG_FILE):
            print("⚠️ Config file not found. Using defaults.")
            return {}
        file = open(CONFIG_FILE, "r")
        config = json.load(file)
        file.close()
        return config
    except Exception as e:
        print("⚠️ Error loading config file:", e)
        return {}

        