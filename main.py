import importlib # Used for importing the modules from the modules folder
import os # Used for listing modules in the modules folder
modules_loaded = {} # Hold dictionaries from registered commands
commands = {}

for module in os.listdir('./modules'):
    if module.startswith('LOS_') and module.endswith('.py'):
        module_to_load = module[:-3]  # Removing the .py at the end
        try:
            mod = importlib.import_module('modules.' + module_to_load)

            if hasattr(mod, 'main'):
                mod.register_commands(commands)
                print(f'[  OK  ]Loaded module: {module_to_load}')
        except Exception as e:
            print(f'[ FAIL ]Failed to load module: {module_to_load}. {e}')