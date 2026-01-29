def register_command(commands):
    commands['viewvar'] = {
    'brief': 'View the value of a specified variable',
    'detailed': '''Displays the name of all variables and their type or the value of a specified variable.

    Usage
    viewvar
    viewvar <variable_name>''',
    'func': viewvar_main
    }

def viewvar_main(arguments, varlist):
    if len(arguments) == 0:
        print("Variables:")
        for var_name, var_value in varlist.items():
            print(f"- {var_name}: {type(var_value['func']).__name__}")
    elif len(arguments) == 1:
        var_name = arguments[0]
        if var_name in varlist:
            var_value = varlist[var_name]['func']
            print(f"Variable '{var_name}': {var_value} (Type: {type(var_value).__name__})")
        else:
            print(f"[ERROR]  Variable '{var_name}' not found.")
    else:
        print("[ERROR]  Invalid usage. Use 'viewvar' or 'viewvar <variable_name>'.")