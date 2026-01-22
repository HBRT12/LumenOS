import sys
import time

def register_command(commands):
    commands['shutdown'] = {"brief": "Saves config and shuts down",
    "detailed": """Shuts down LumenOS and saves config unless tag is used.
    
    Tags
    -ns: When this tag is used, LumenOS shuts down without saving config to the JSON file.
    
    Formatting
    shutdown <tag>
    
    Usage
    shutdown
    shutdown -ns""",
    "func": shutdown_main
                            }

def shutdown_main(arguments, commands):
    if arguments[0] == "-ns":
        print("Thank you for using LumenOS!\n\nShutting down...")
        time.sleep(2)
        sys.exit()
    else:
        try:
            commands["save"]["func"]
            print("[ OK ] Config saved to JSON file.")
            print("Thank you for using LumenOS!\n\nShutting down...")
        except Exception as e:
            print(f"[FAIL] Failed to save config: {e}")
