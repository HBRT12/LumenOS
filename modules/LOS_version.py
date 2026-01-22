def register_command(commands):
    commands['version'] = {
        'brief': 'Displays the current version of LumenOS',
        'detailed': '''Displays the current version of LumenOS.

        Usage
        version''',
        'func': version_main
    }

def version_main(arguments):
    print("LumenOS v0.5.2 Alpha")