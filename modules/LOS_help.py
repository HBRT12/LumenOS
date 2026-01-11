def register_command(commands):
    commands['help'] = {
        'brief': 'Displays all commands or information about a specific command',
        'detailed': '''The help command displays all commands unless a command is specified as an argument.
        
        Tags:
        -d: Gives the detailed description of the specified command.
        
        Usage:
        help
        help <command>
        help <tag> <command>''',
        'func': help_main
    }

def help_main(arguments, commands):
    if len(arguments) == 0:
        for each in commands:
            print(f'{each}: {commands[each]["brief"]}')
    elif arguments[0] == '-d':
        arguments.pop(0)
        print(commands[arguments[0]]["detailed"])
    else:
        arguments.pop(0)
        print(commands[arguments[0]]["brief"])