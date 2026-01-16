import json
#This file contains the load function, which is needed to load user info.

def register_command(commands):
    commands['load'] = {
        'brief description': 'loads the configuration from a file',
        'detailed description': '''Loads the configuration settings from a JSON file named 'config.json'.
        
        Usage
        load''',
        'func': load_main
    }

def load_main():
    with open('config.json', 'r') as f:
        return json.load(f)