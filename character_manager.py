
import json
import os

def create_character(name, occupation, age, str_, dex, int_, pow, app, edu):
    return {
        "name": name,
        "occupation": occupation,
        "age": age,
        "abilities": {
            "STR": str_,
            "DEX": dex,
            "INT": int_,
            "POW": pow,
            "APP": app,
            "EDU": edu
        }
    }

def save_character(character, folder="sample_data"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{character['name']}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(character, f, ensure_ascii=False, indent=4)

def load_character(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
