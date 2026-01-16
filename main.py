import importlib # Used for importing the modules from the modules folder
import os # Used for listing modules in the modules folder
import time # Used for adding delays


modules_loaded = {} # Hold dictionaries from registered commands
commands = {}

def boot():
    print("Welcome to LumenOS!")
    time.sleep(1)
    for module in os.listdir('./modules'): #  Lists all files in the modules folder
        if module.startswith('LOS_') and module.endswith('.py'):
            module_to_load = module[:-3]  # Removing the .py at the end
            try:
                mod = importlib.import_module('modules.' + module_to_load)
                if hasattr(mod, 'register_command'):  # Checks if python file has module loader
                    mod.register_command(commands)  # Runs register command (adds help prompts and main function to the commands dictionary)
                    print(f'[ OK ]Loaded module: {module_to_load}')
                else:
                    print(f'[FAIL]Module {module_to_load} does not have a register_command function.')
            except Exception as e:
                print(f'[FAIL]Failed to load module: {module_to_load}. {e}')
        time.sleep(0.2)  # Small delay for better readability
    print(f'\n\n[INFO]Total modules loaded: {len(commands)}')
    time.sleep(2)  # Delay for 2 seconds before starting main loop
    main()

def main():
    while True:
        commands_input = input('LumenOS> ').strip().split()  # Gets user input and splits it into a list
        if len(commands_input) == 0:
            pass  # If no input is given, do nothing
        else:
            print(commands_input)

boot()