import importlib # Used for importing the modules from the modules folder
import os # Used for listing modules in the modules folder
modules_loaded = {}

for module in os.listdir('./modules'):
    if module.startswith('LOS_') and module.endswith('.py'):
        module_to_load = module[:-3] # Removing the .py at the end
        mod = importlib.import_module('modules.' + module_to_load)