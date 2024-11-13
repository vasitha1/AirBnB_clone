#!/usr/bin/python3
"""
console.py

This module contains the entry point of the command interpreter

Methods:
- quit and EOF methods: to exit the program
- Customised help method: 
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return self.do_quit(arg)

    def defaultf(self, line):
        if line.strip() == '':
            pass
        else:
            print("Command not found: {}".format(line))
