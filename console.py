#!/usr/bin/python3
""" this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """ our reimplementation of cmd.Cmd
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        quit()

    def do_create(self, arg):
        'creates a new instance of BaseModel'
        # save to json_file
        # print id
        # if class name is missing print: ** class name missing **
        # if class name doesnt exist print: ** class doesn't exist **
        pass

    def do_show(self, arg):
        'prints string representation of given object'
        pass

    def emptyline(self):
        pass
    
    do_EOF = do_quit 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
