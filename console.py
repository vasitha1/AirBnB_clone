#!/usr/bin/python3
"""
console.py

This module provides `HBNBCommand` class which used as the entry point of
the command interpreter.

Methods:
- quit() and EOF(): Both exit the program. The `EOF` method exits via ctrl+d.
- emptyline(): Overrides the default `emptyline` method of `cmd.Cmd` by doing
  nothing on empty input. By default pressing `Enter` without a command
  repeates the last command.
- Customised help method: To summarise the use of all commands
- Default: To handle situations where an unknown command is given to the prompt

Usage:
This class is intended to serve as a command interpreter for the AirBnB console.

Design Notes:
- Imports the `cmd` module which allows to write a line-oriented command
  interpreter. It treates methods starting with `do` as commands.
- Defines a custom prompt string `(hbnb)` that will appear when the user
  interacts with the interpreter.
- The cmd module is needed for the creation of an interactive interactively
- line.strip makes sure that the line is empty after spaces and tabs removed.
- HBNBCommand().cmdloop() makes sure that code runs infinitely untill it meets an
  EOF or quit command like the shell does.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the commands as methods"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """to exit the program using "quit" command"""

        return True

    def do_EOF(self, arg):
        """to exit the program using Cntrl+D """

        # Print new line when exiting via EOF
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered."""

        pass

    """
    def default(self, line):
        Is called when the command is not recorgnised
        print("Command not found: {}".format(line))
    """
    def do_create(self, arg):
        """Creates a new instance of the basemode, prints it's id and saves"""

        if not arg:
            print("** class name missing **")
            return

        try:
            if arg == "Basemodel":
                instance = BaseModel()

                # remember to save to file when base method is added
                instacne.save()
                print(instance.id)

            else:
                print("** class doesn't exist **")

        except Exception as e:
            print("Error: {}".format(e))

    def do_show(self, arg):
        """Prints string representation of an instance based on class name and id"""

        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] != "Basemodel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)

        if obj:
            print(obj)

        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and ID"""

        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] != "Basemodel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()

        else:
            print("** no instance found **")

    def all(self, arg):
        """
        Prints all string representations of all instances and
        optionaly filters by class name.
        """

        args = arg.split()
        objects = storage.all()

        if not args:
            print([str(obj) for obj in objects.values()])

        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")

        else:
            filtered_objs = [str(obj) for key, obj in objects.items()
                            if key.startswith("{}.".format(args[0]))]

            print(filtered_objs)

    def update(self, arg):
        """
        Updates an instance based on the class name and ID by adding or
        updating an instance.
        """

        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)

        if not obj:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        # Ensure that the attribute name and value are valid
        attribute_name = args[2]
        value = args[3]

        # Cast value to the appropriate type based on the attribute type
        if isinstance(getattr(obj, attribute_name, None), str):
            setattr(obj, attribute_name, value)

        elif isinstance(getattr(obj, attribute_name, None), int):
            try:
                setattr(obj, attribute_name, int(value))

            except ValueError:
                print("** invalid value type **")
                return

        elif isinstance(getattr(obj, attribute_name, None), float):
            try:
                setattr(obj, attribute_name, float(value))

            except ValueError:
                print("** invalid value type **")
                return
        else:
            print("** attribute type unsupported **")
            return

        # Update the `updated_at` timestamp and save
        obj.updated_at = datetime.now()
        obj.save()

"""
    def do_help(self, arg):
         Doccuments all created methods 
        if arg == "quit":
            print("Quit command to exit the program\n")
        elif arg == "EOF":
            print("Ctrl + D command to exit the program\n")
        else:
            print("\nDocumented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit\n")
"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()

*** Unknown syntax
