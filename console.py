#!/usr/bin/python3
""" this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """ our reimplementation of cmd.Cmd
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        'creates a new instance of BaseModel'
        # save to json_file
        # print id
        # if class name is missing print: ** class name missing **
        # if class name doesnt exist print: ** class doesn't exist **
        pass

    def do_show(self, arg):
        'outputs representation of an instance given the class name and id'
        # errors:
            # ** class name missing **
            # ** class doesn't exist **
            # ** instance id missing **
            # ** no instance found **
        pass

    def do_destroy(self, arg):
        'delete instance given by the class name and id'
        # save change to json file
        # errors:
            # ** class name missing **
            # ** class doesn't exist **
            # ** instance id missing **
            # ** no instance found **
        pass

    def do_all(self, arg):
        'outputs string representations for every existing instance or for all of a class'
        # error: ** class doesn't exist **
        # example: (hbnb) all BaseModel
        #   ["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]`
        pass

    def do_update(self, arg):
        'updates the instance given by class_name and id
        usage: update <class> <id> <attr> "<val>"'
        # only one attribute can be updated at a time
        # save changes to json
        # assume given <attr> is valid
        # typecast <val> accordingly 
        # errors: 
            # ** class name missing **
            # ** class doesn't exist **
            # ** instance id missing **
            # ** no instance found **
            # ** attribute name missing **
            # ** value missing **
        # ignore additional arguments
        # id, created_at, and updated_at cannot be updated and wont be passed
        # expect only simple args : string, int, and float
        pass

    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        quit()

    def emptyline(self):
        pass
    
    do_EOF = do_quit 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
