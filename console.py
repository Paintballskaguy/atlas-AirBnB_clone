#!/usr/bin/python3
""" this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

import cmd, models

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

    def do_show(self, args):
        'outputs representation of an instance given the class name and id'
        instance = self.get_instance(args)
        if instance is None:
            return
        else:
            print(instance)

    def do_destroy(self, arg):
        'delete instance given by the class name and id'
        # save change to json file
        # errors:
            # ** class name missing **
            # ** class doesn't exist **
            # ** instance id missing **
            # ** no instance found **
        pass

    def do_all(self, args):
        obj_list = []
        if not args:
            for key, value in models.storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
        elif args not in models.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if key.startswith(args):
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, arg):
        'updates the instance given by class_name and id. usage: update <class> <id> <attr> "<val>"'
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
        args = arg.split()
        if len(args) < 1:
            print("** class name missing**")
            return
        if args[0] not in models.valid_classes:
            print("** class doesn't exist**")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if instance is None:
            return
        if len(args) < 3:
            print("** attribute name missing **")
             return
        if len(args) < 4:
            print("** value missing **")
            return
            
        attr_name = args[2]
        attr_value = args[3].strip("")
        
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            if attr_type is int:
                attr_value = int(attr_value)
            elif attr_type is float:
                attr_value = float(attr_value)
                
        setattr(instance, attr_name, attr_value)
        instance.save()

    def get_instance(self, args):
        args = args.split()
        class_name = args[0] if len(args) > 0 else None
        id_num = args[1] if len(args) > 1 else None

        if class_name is None:
            print('** class name missing **')
            return None
        elif class_name not in models.valid_classes:
            print("** class doesn't exist **")
            return None
        elif id_num is None:
            print('** instance id missing **')
            return None
        else:
            key = class_name + "." + id_num
            instance = models.storage.all().get(key)  
            if instance is None: 
                print('** instance not found **')
                return None
            return instance

    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        quit()
        
    def do_destroy(self, arg):
        """deletes an instance by class name and id"""
        instance = self.get_instance(arg)
        if instance is None:
            return
        key = arg.split()[0] + "." + arg.split()[1]
        del models.storage.all()[key]
        models.storage.save()

    def emptyline(self):
        pass
 
    do_EOF = do_quit 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
