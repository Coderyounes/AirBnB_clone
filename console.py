#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """exit the program after reach/get the end-of-file\n"""
        return True

    def do_create(self, arg):
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
