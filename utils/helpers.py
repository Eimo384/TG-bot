import json
import os

STAT_FILE = "data/stats.json"

def ensure_stat_file():
    if not os.path.exists(STAT_FILE):
        with open(STAT_FILE, "w") as f:
            json.dump({}, f)

def update_stat(command_name):
    ensure_stat_file()
    with open(STAT_FILE, "r") as f:
        stats = json.load(f)
    stats[command_name] = stats.get(command_name, 0) + 1
    with open(STAT_FILE, "w") as f:
        json.dump(stats, f, indent=2)

def get_stat():
    ensure_stat_file()
    with open(STAT_FILE, "r") as f:
        return json.load(f)
