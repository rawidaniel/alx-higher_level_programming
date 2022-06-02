#!/usr/bin/python3
import sys
if __name__ == "__main__":
    size = len(sys.argv)
    if (size == 1):
        print("{} arguments.".format(size - 1))
    elif (size == 2):
        print("{} argument:".format(size - 1))
    else:
        print("{} arguments:".format(size - 1))

    for i in range(1, size):
        print("{}: {}".format(i, sys.argv[i]))
