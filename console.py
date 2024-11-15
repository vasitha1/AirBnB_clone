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
- Default: To handle situations where an unknown command is given to the
  prompt

Usage:
This class is intended to serve as a command interpreter for the AirBnB
console.

Design Notes:
- Imports the `cmd` module which allows to write a line-oriented command
  interpreter. It treates methods starting with `do` as commands.
- Defines a custom prompt string `(hbnb)` that will appear when the user
  interacts with the interpreter.
- The cmd module is needed for the creation of an interactive interactively
- line.strip makes sure that the line is empty after spaces and tabs removed.
- HBNBCommand().cmdloop() makes sure that code runs infinitely untill it meets
  an EOF or quit command like the shell does.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the commands as methods"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exits the program using `quit` command"""

        return True

    def do_EOF(self, arg):
        """Exits the program using Ctrl+D """

        # Print new line when exiting via EOF
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered."""

        pass


    def default(self, line):
        """Handles commands in the <ClassName>.<command>() format"""

        if '.' not in line:
            print("Command not found: {}".format(line))
            return

        cls_name, mtd_call = line.split('.', 1)
        mtd_name, _, args = mtd_call.partition('(')
        args = args.rstrip(')').strip(' "')

        if cls_name not in globals() or not issubclass(globals()[cls_name], BaseModel):
            print("** class doesn't exist **")
            return

        # Map method name to actual command methods
        cmd_map = {
            "all": "do_all",
            "count": "do_count",
            "show": "do_show",
            "destroy": "do_destroy",
            "update": "do_update",
            "create": "do_create"
        }

        if mtd_name in cmd_map:
            cmd_mtd = cmd_map[mtd_name]

            if args:
                full_args = f"{cls_name} {args}"

            else:
                full_args = cls_name

            getattr(self, cmd_mtd)(full_args)

        else:
            print("Command not found: {}".format(line))

    def do_create(self, arg):
        """
        Creates a new instance of the BaseModel, saves and prints
        it's id.
        """

        if not arg:
            print("** class name missing **")
            return

        # Fetch the class from the argument dynamically using `globals()`
        cls = globals().get(arg)
        if cls and issubclass(cls, BaseModel):
            instance = cls()
            instance.save()
            print(instance.id)

        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints string representation of an instance based on class name
        and id
        """

        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        cls = globals().get(args[0])
        if not cls or not issubclass(cls, BaseModel):
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

        cls = globals().get(args[0])
        if not cls or not isinstance(cls, BaseModel):
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

    def do_all(self, arg):
        """
        Prints all string representations of all instances and
        optionaly filters by class name.
        """

        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return

        if '.' in arg and arg.endswith('.all()'):

            # Split class name and method
            cls_name = arg.split('.')[0]

            if cls_name in globals() and issubclass(globals()[cls_name], BaseModel):
                instances = [
                    str(obj) for key, obj in storage.all().items()
                    if key.startswith(cls_name + '.')
                ]
                print(instances)

            else:
                print("** class doesn't exist **")

        else:
            print("** Invalid command synatx **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and ID by adding or
        updating an instance.
        """

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        cls = globals().get(args[0])
        if not cls or not issubclass(cls, BaseModel):
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
        attr_name = args[2]
        attr_value = args[3].strip('"')

        try:
            # Cast to proper type dynamically
            attr_type = type(getattr(obj, attr_name, attr_value))
            setattr(obj, attr_name, attr_type(attr_value))
            obj.save()

        except ValueError:
            print("** invalid value **")

    def do_count(self, arg):
        """Counts the number of instances of a class"""

        if not arg:
            print("** class name missing **")
            return

        cls_name = arg.strip()
        if cls_name in globals() and issubclass(globals()[cls_name], BaseModel):
            count = sum(
                1 for key in storage.all()
                if key.startswith(cls_name + '.')
            )
            print(count)

        else:
            print("** class does't exist **")

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
