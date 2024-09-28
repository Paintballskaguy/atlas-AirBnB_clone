#!/usr/bin/python3
""" this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """ our reimplementation of cmd.Cmd
    """
    # update help command
    # code should not execute one import
    prompt = '(hbnb) '
    file = None

    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    
    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        self.close()
        quit()

    def emptyline(self):
        pass
    
    do_EOF = do_quit 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
