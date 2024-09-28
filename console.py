#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    # implement EOF
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
