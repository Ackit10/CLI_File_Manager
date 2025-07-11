from Command_classes import PwdClass
from Command_classes import CdClass
from Command_classes import LsClass
from Command_classes import RmClass
from Command_classes import MvClass
from Command_classes import MkDirClass
from Command_classes import CpClass

#TODO Create the multiArgument support for parser, so make parser function more adopdable for commandClass,
#more depended from command information, like amount of arguments, and if arguments are actualy taked
#And make parser function more....reliable and easy for refactor, so split it in multiple functions

def parse(user_input: str) -> str | None:
        command_functions = {"pwd": PwdClass.pwdClass, "cd": CdClass.cdClass,"ls": LsClass.lsClass,
                             "rm": RmClass.rmClass,  "mv": MvClass.mvClass, "mkdir": MkDirClass.mkDir,
                             "cp": CpClass.cpClass}
        if user_input == "quit":
                return None
        else:
                input_list = user_input.split()
                if input_list[0] in command_functions:
                        excecutive_command = command_functions[input_list[0]]()
                        return excecutive_command.exec(input_list[1:len(input_list)])
                else:
                        return "Command not found"

