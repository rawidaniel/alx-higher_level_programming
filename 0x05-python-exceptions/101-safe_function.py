#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    new_list = []
    for arg in args:
        new_list.append(arg)
    try:
        return fct(new_list[0], new_list[1])
    except ZeroDivisionError as e:
        print(f"Exception: {e}", file=sys.stderr)
    except IndexError as e:
        print(f"Exception: {e}", file=sys.stderr)
    return None
