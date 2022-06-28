#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attr, value):
        if attr != "first_name":
            message = "'LockedClass' object has no attribute '{}'"
            raise AttributeError(message.format(attr))
        self.__dict__.update({attr: value})
