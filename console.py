#!/usr/bin/python3
"""
cmd - module is the base of the comand line Interpreter
Other - Models are classes to act like objects or destinations
re - Regex Modules
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
import re


class HBNBCommand(cmd.Cmd):
    """
    HBNB - Command-line Interpreter use a various Cmd
    """
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
        """
        create new instance
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = arg
                if class_name not in globals():
                    raise NameError
                new_instance = globals()[arg]()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation
        of an instance based on the class name and id.
        """
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
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
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
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        obj = storage.all()
        args_list = args.split()

        if not args_list:
            for key in obj:
                print("{}".format(str(obj[key])))
        elif args_list[0] not in globals():
            print("** class doesn't exist **")
        else:
            class_name = args_list[0]
            if hasattr(globals()[class_name], 'all'):
                print(globals()[class_name].all())
            else:
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
                if isinstance(instance, globals()[class_name]):
                    if not hasattr(instance, attr_name):
                        setattr(instance, attr_name, None)
                    setattr(instance, attr_name, attr_value)
                    instance.save()
                else:
                    print("** attribute name invalid **")
            else:
                print("** no instance found **")

    def do_count(self, line):
        """Print the count all class instances"""
        cur_class = globals().get(line, None)
        if cur_class is None:
            print("** class doesn't exist **")
            return
        n = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                n += 1
        print(n)

    def default(self, line):
        if len(line) == 0:
            return

        pattern = r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        m = re.match(pattern, line)

        mName, method, params = m.groups()

        if len(params) == 0:
            params = []

        cmd = " ".join([mName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
