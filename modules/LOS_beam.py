# Adds command and relevant info to commands dictionary
def register_command(commands):
    commands['beam'] = {
        'brief': 'prints inputted arguments',
        'detailed': '''Any argument given in the command will be printed to the screen.
        
        Tags
        -rw: The arguments given will be printed in reverse order by word.
        -rc: The arguments given will be printed in reverse order by character.
        -i: Any tags given after this tag will 
        
        Formatting
        beam [tag if used] [arguments]
        
        Example
        beam -rw This is a test
        beam Hello, world!''',
        'func': beam_main
    }

def beam_main(arguments):  # Main function for the beam command
    if arguments[0] not in ['-rw','-rc']:  # Plainly returns the arguments if there is no tag
        result = ' '.join(arguments) # List converted into a string

    elif arguments[0] == '-rw':  # Looks for -rw tag
        arguments.pop(0)  # Removes the tag from the arguments list
        arguments.reverse() # reverses the arguments while they are still a list
        result = ' '.join(arguments) # converts list -> string and saves to result

    elif arguments[0] == '-rc': # checks for -rc tag
        arguments.pop(0) # Removes the tag from the arguments list
        result = ' '.join(arguments)[::-1] # converts list -> string and reverses the characters

    elif arguments[0] == '-i':
        arguments.pop(0) # Removes the -i tag and ignores everything else to allow tags to be saved

    print(result)
