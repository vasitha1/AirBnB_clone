#!/usr/bin/python3
"""
console.py

This module contains the entry point of the command interpreter

Methods:
- quit and EOF methods: to exit the program
- Customised help method: To summarise the use of all commands
- Default: To handle situations where an unknown command is given to the prompt

Usage:
This class is intended to serve as a command interprete

Design Notes:
- The cmd module isneeded for the creation of an interactive interactively
- line.strip makes sure that the line is empty after spaces and tabs removed
- HBNBCommand().cmdloop() makes sure that code runs infinitely untill it meetan
EOF or quit command like the shell does.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """ Defines the commands as methods """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """to exit the program using "quit" command"""
        return True

    def do_EOF(self, arg):
        """to exit the program using Cntrl+D """
        return self.do_quit(arg)

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def default(self, line):
        """Is called when the command is not recorgnised """
        print("Command not found: {}".format(line))

    def do_create(self, arg):
        """Creates a new instance of the basemode, prints it's id and saves"""
        if not arg:
            print("** class name missing **")
            return
        if arg != "Basemodel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        #remember to save to file when base method is added
        print(new_instance.id)

    def do_show(self, class_name, id):
        """Prints string representation of instance based class name and id"""
        if not class_name:
            print("** class name missing **")
            return
        if class_name != "Basemodel":
            print("** class doesn't exist **")
            return
        if not id:
            print("** instance id missing **")
            return
        instance = basemodel.get(class_name, id)#Need to implement in the basemodel

        if not instance:
            print("** no instance found **")
            return
        print("{}".format(instance = storage.get(class_name, id)))#Need to implement in Basemodel

    def do_help(self, arg):
        """ Doccuments all created methods """
        if arg == "quit":
            print("Quit command to exit the program\n")
        elif arg == "EOF":
            print("Ctrl + D command to exit the program\n")
        else:
            print("\nDocumented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
