#!/usr/bin/python3
"""Airbnb console module"""

import cmd
import os


class HBNBCommand(cmd.Cmd):
    """Airbnb console module"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """quit the program"""
        exit()

    def do_EOF(self, line):
        """Exit upon EOF condition"""
        return True

    def do_clear(self, line):
        """Clear terminal"""
        os.system('clear')

    def postloop(self):
        """Action taken after each iteration or each prompt"""
        print()

    def emptyline(self):
        """Action to be taken if an emptyline is passed on the console"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
