#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """exit the program after reach/get the end-of-file\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
