from src.classes.StringClass import *
from src.classes.CommandClass import *
# import sys
# sys.path.append("..")
# from classes.CommandClass import *
# from classes.StringClass import *

from typing import List


context = None
command_constructors = {
    "echo": EchoCommand,
    "exit": ExitCommand,
    "pwd": PwdCommand,
    "cat": CatCommand,
    "wc": WcCommand,
    "=" : VarAssignment
}
command_list = ["echo", "exit", "pwd", "cat", "wc", "="]


class InputError(Exception):
    """
    Base exception for parser
    """

    def __init__(self):
        self.msg = "Command not found!"


def parser(input: List[InterpretString | PlainString]) -> Command:
    """
    Parses string of command to an object of CommandClass class.

    Parameters:
        input: one lexem between pypes
    Returns:
        CommandClass if command is valid
    """
    if len(input) == 0 or input[0].raw_str not in command_list:      # TODO: VarAssignment
        raise InputError
    
    obj = command_constructors[input[0].raw_str](input[1])
    return obj
