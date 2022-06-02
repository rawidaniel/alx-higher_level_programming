#!/usr/bin/python3
import sys
size = len(sys.argv)
sum = 0
if size > 1:
    for i in range(1, size):
        sum += int(sys.argv[i])
print("{}".format(sum))
