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
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in models.valid_classes:
            print("** class doesn't exist **")
            return
        else:
            model_class = globals().get(arg[0])
            new_obj = model_class()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        'outputs representation of an instance given the class name and id'
        instance = self.get_instance(args)
        if instance is None:
            return
        else:
            print(str(instance))

    def do_destroy(self, arg):
        'delete instance given by the class name and id'
        instance = self.get_instance(arg)
        if instance is None:
            return
        else:
            key = models.storage.construct_key(instance)
            models.storage.all().pop(key)
            models.storage.save()

    def do_all(self, args):
        'outputs string representations for every existing instance or for all of a class'
        obj_list = []
        if not args:
            for value in models.storage.all().values():
                obj_list.append(str(value))
        elif args in models.valid_classes:
            for key, value in models.storage.all().items():
                if key.startswith(args):
                    obj_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, arg):
        'updates the instance given by class_name and id. usage: update <class> <id> <attr> "<val>"'
        # assume given <attr> is valid
        # typecast <val> accordingly 
        # expect only simple args : string, int, and float
        # only one attribute can be updated at a time
        # ignore additional arguments
        # save changes to json
        instance = self.get_instance(arg)
        if instance is None:
            return

        attr_val = self.parse_attributes(arg)
        if attr_val is None:
            return

        attr = attr_val[0]
        value = attr_val[1]
        # if attr_val[0] in ('id', 'created_at', 'updated_at'):
        #     return

        if hasattr(instance, attr):
            attr_type = type(getattr(instance, attr))
            if attr_type is int:
                value = int(value)
            elif attr_type is float:
                value = float(value)

        setattr(instance, attr, value)
        instance.save()

    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        quit()

    do_EOF = do_quit 

    def emptyline(self):
        pass

    def parse_attributes(self, args):
        'returns an touple with attribute and value'
        args = args.split()
        attr = args[2] if len(args) > 2 else None
        value = args[3] if len(args) > 3 else None
        if attr is None:
            print('** attribute name missing **')
            return None
        elif value is None:
            print('** value missing **')
            return None
        else:
            return (attr, value)

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
                print('** no instance found **')
                return None
            return instance

if __name__ == '__main__':
    HBNBCommand().cmdloop()
