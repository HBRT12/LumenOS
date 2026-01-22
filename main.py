import importlib  # Used for importing the modules from the modules folder
import os  # Used for listing modules in the modules folder
import time  # Used for adding delays
import getpass  # Used for hiding password input

modules_loaded = {}  # Hold dictionaries from registered commands
commands = {}

def loginscreen():
    print("Welcome to LumenOS Secure Login\n")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    # For demonstration purposes, we accept any username/password
    print(f"\n[INFRM]  Login successful. Welcome, {username}!\n")
    time.sleep(1)

def boot():
    print("Welcome to LumenOS!\n\n[INFRM]  Loading modules...")
    time.sleep(1)
    for module in os.listdir("./modules"):  # Lists all files in the modules folder
        if module.startswith("LOS") and module.endswith(".py"):
            module_to_load = module[:-3]  # Removing the .py at the end
            try:
                mod = importlib.import_module("modules." + module_to_load)
                if hasattr(mod, "register_command"):  # Checks if python file has module loader
                    mod.register_command(commands)  # Runs register command (adds help prompts and main function to the commands dictionary)
                    print(f"[ OK! ]  Loaded module: {module_to_load}")
                else:
                    print(f"[ERROR]  Module {module_to_load} does not have a register_command function.")
            except Exception as e:
                print(f"[ERROR]  ERRORed to load module: {module_to_load}. {e}")
        time.sleep(0.05)  # Small delay for better readability
    print(f"[INFRM]  Total modules loaded: {len(commands)}\n\n")

    try:
        print("[INFRM]  Attempting to load config...")
        time.sleep(0.5)
        config = commands["load"]["func"]
        print("[ OK! ]  Config loaded successfully!")
    except Exception as e:
        print(f"[ERROR]  ERRORed to load config: {e}")
    time.sleep(2)  # Delay for 2 seconds before starting main loop
    main()

def main():
    while True:
        commands_input = input("\nLumenOS> ").strip().split()  # Gets user input and splits it into a list
        if len(commands_input) == 0:
            pass  # If no input is given, do nothing
        else:
            command_to_run = commands_input[0]  # First item in list is the command
            arguments = commands_input[1:]  # The rest are arguments
            if command_to_run in commands:  # Checks if command exists in commands dictionary
                try:
                    commands[command_to_run]["func"](arguments, commands)  # Runs the main function of the command
                except TypeError:
                    commands[command_to_run]["func"](arguments)  # Runs the main function of the command
                except Exception as e:
                    print(f"[ERROR]  An error occurred while executing the command: {e}")
            else:
                print(f"[ERROR]  Command '{command_to_run}' not found. Type 'help' to see available commands.")

boot()
