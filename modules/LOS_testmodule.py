def register_command(commands):
    commands['test'] = {
        'command': 'viewvar',
        'brief description': 'displays saved variables',
        'detailed description': """""",
    }
def test():
    print('If you can read this and you are running main.py,you have successfully ran a function from one of the module files and the module importer is working!')
