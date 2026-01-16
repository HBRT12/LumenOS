import json
#This file contains the save/load function, which is used to save configuration and user info.

def register_command(commands):
    commands['save'] = {
        'brief description': 'saves the current configuration to a file',
        'detailed description': '''Saves the current configuration settings to a JSON file named 'config.json'.
 
        Usage
        save''',
        'func': save_main
    }

def save_main(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)
