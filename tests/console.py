#!/usr/bin/python3
"""
    For debugging and testing of the program
"""
import cmd
from seniors.base_seniors import BaseSenior
from seniors import storage
import shlex

all_classes = {"BaseSenior": BaseSenior}

class SeniorCommand(cmd.Cmd):
    """
        The Console
    """
    prompt = "(9ja3S) "

    def do_quit(self, arg):
        """
            Quit the console
        """
        return True
    
    def do_EOF(self, arg):
        """
            Exit the console, same as quit
        """
        return True
    
    def do_emptyline(self):
        """
            Empty line + ENTER does nothing
        """
        return False
    
    def do_create(self, args):
        """"
        Create an instance of a class
        """
        if not args:
            print("** class name missing **")
            return
        all_args = shlex.split(args)
        if not all_classes.get(all_args[0]):
            print("** class doesn't exist **")
            return
        new_instance = all_classes[all_args[0]]()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, args):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        all_args = shlex.split(args)
        if not all_classes.get(all_args[0]):
            print("** class doesn't exist **")
            return
        if len(all_args) == 1:
            print("** instance id missing **")
            return
        instance_key = all_args[0] + "." + all_args[1]
        all_instances = storage.all()
        for key in all_instances.keys():
            if key == instance_key:
                print(all_instances[key])
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        all_args = shlex.split(args)
        if not all_classes.get(all_args[0]):
            print("** class doesn't exist **")
            return
        if len(all_args) == 1:
            print("** instance id missing **")
            return
        instance_key = all_args[0] + "." + all_args[1]
        all_instances = storage.all()
        for key in all_instances.keys():
            if key == instance_key:
                storage.delete(instance_key)
                return
        print("** no instance found **")

    def do_all(self, args):
        """
            Prints all string representation of all
            instances based or not on the class name
        """
        new_list = []
        if args:
            all_args = shlex.split(args)
            if all_classes.get(all_args[0]):
                all_instances = storage.all(all_args[0])
            else:
                print("** class doesn't exist **")
                return
        else:
            all_instances = storage.all()
        for value in all_instances.values():
                new_list.append('"' + str(value) + '"')
        print("[", end="")
        print(", ".join(new_list), end="")
        print("]")
    
    def do_update(self, args):
        """
            Updates an instance based on the class name
            and id by adding or updating attribute
        """
        if not args:
            print("** class name missing **")
            return
        all_args = shlex.split(args)
        if not all_classes.get(all_args[0]):
            print("** class doesn't exist **")
            return
        if len(all_args) < 2:
            print("** instance id missing **")
            return
        if len(all_args) < 3:
            print("** attribute name missing **")
            return
        if len(all_args) < 4:
            print("** value missing **")
            return
        instance_key = all_args[0] + '.' + all_args[1]
        all_instances = storage.all(all_args[0])
        if all_args[2] in ["id", "created_at", "updated_at"]:
            return
        if all_args[3]:
            if isinstance(all_args[3], int):
                all_args[3] = int(all_args[3])
            elif isinstance(all_args[3], float):
                all_args[3] = float(all_args[3])
        for key in all_instances.keys():
            if key == instance_key:
                setattr(all_instances[key], all_args[2], all_args[3])
                all_instances[key].save()
                return
        print("** no instance found **")
    
    def do_count(self, args):
        """"
            Count the number of instances
        """
        if args:
            all_args = shlex.split(args)
            if all_classes.get(all_args[0]):
                all_instances = storage.all(all_args[0])
            else:
                print("** class doesn't exist **")
                return
        else:
            all_instances = storage.all()
        count = 0
        for obj in all_instances:
            count += 1
        print(count)



if __name__ == "__main__":
    SeniorCommand().cmdloop()

