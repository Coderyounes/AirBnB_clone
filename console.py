#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """disable the repettion of the last command using emptyline method"""
        pass

    def do_EOF(self, line):
        """exit the program after reach/get the end-of-file\n"""
        return True

    def do_create(self, arg):
        """reate new instance

        Args:
            arg (_type_): _description_
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = globals()[arg]()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        obj = storage.all()
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in globals():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args_list[0], args_list[1])
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        obj = storage.all()
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in globals():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args_list[0], args_list[1])
            if key in obj:
                del (obj[key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        obj = storage.all()
        args_list = args.split()

        if not args_list:
            for key in obj:
                print("{}".format(str(obj[key])))
        elif args_list[0] not in globals():
            print("** class doesn't exist **")
        else:
            class_name = args_list[0]
            for key in obj:
                if key.split('.')[0] == class_name:
                    print(str(obj[key]))

    def do_update(self, args):
        """
        Updates an instance based on the class name and attrbute name
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        obj = storage.all()
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in globals():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            class_name = args_list[0]
            obj_id = args_list[1]
            attr_name = args_list[2]
            attr_value = args_list[3][1:-1]

            key = "{}.{}".format(class_name, obj_id)
            if key in obj:
                instance = obj[key]
                if hasattr(instance, attr_name):
                    setattr(instance, attr_name, attr_value)
                    instance.save()
                else:
                    print("** attribute name invalid **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
