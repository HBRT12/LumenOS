import json
#This file contains the save/load function, which is essential for LumenOS to run. DO NOT DELETE!!!

def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)