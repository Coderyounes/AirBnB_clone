#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
