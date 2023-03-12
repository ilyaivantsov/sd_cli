from src.classes.StringClass import *

from typing import List


def lexer(stdin: str) -> List[List[InterpretString | PlainString]]:
    """
    Parameters:
        stdin: raw string from stdin

    Returns:
      List of several lists with InterpretString / PlainString objects.
      If there is a pipe in a raw command, parser will need
      separate commands as separate lists
    """
    words = []

    start = 0
    for i in range(len(stdin)):

        if stdin[i] == "'":
            words.append(stdin[start:i])
            start = i + 1
            words.append("'")

        elif stdin[i] == '"':
            words.append(stdin[start:i])
            start = i + 1
            words.append('"')

    # if there are no quotes in stdin
    if not start and len(stdin):
        words = stdin.split()
        if len(words) == 1 and "=" in stdin:
            words = stdin.split("=")
            words.insert(0, "=")
        obj_list = []
        for i in range(len(words)):
            obj = InterpretString(words[i])
            obj_list.append(obj)
        lexer_res = [obj_list]
        return lexer_res

    met_mark = None
    quotes = ["'", '"']
    words_as_objs = []
    elem = ""

    for word in words:

        if met_mark is None and word in quotes:
            if elem:
                obj = InterpretString(elem.rstrip())
                words_as_objs.append(obj)
                elem = ""
            met_mark = word
            continue

        elif word == met_mark:
            if met_mark == "'":
                obj = PlainString(elem.rstrip())
            else:
                obj = InterpretString(elem.rstrip())

            words_as_objs.append(obj)
            elem = ""
            met_mark = None
            continue

        elem += word

    lexer_res = [words_as_objs]

    return lexer_res
