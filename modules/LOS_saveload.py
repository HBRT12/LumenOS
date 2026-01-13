import json
#This file contains the save/load function, which is essential for LumenOS to run.

def register_command(commands):
    commands['save'] = {
        'brief description': 'saves the current configuration to a file',
        'detailed description': '''Saves the current configuration settings to a JSON file named 'config.json'.
 
        Usage
        save''',
        'func': save_main
    }
    commands['load'] = {
        'brief description': 'loads the configuration from a file',
        'detailed description': '''Loads the configuration settings from a JSON file named 'config.json'.
        
        Usage
        load''',
        'func': load_main
    }

def save_main(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def load_main():
    with open('config.json', 'r') as f:
        return json.load(f)