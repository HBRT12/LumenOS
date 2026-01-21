import os

def register_command(commands):
    commands['clear'] = {"brief": "Clears the screen",
                            "detailed": """Clears terminal output, making space on the screen
                            
                            Usage
                            clear
                            """,
                            "func": clear_main
                            }
def clear_main(arguments):
    os.system('cls' if os.name == 'nt' else 'clear')