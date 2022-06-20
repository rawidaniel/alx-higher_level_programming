#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        div = 0
        try:
            for j in range(i, i + 1):
                div = my_list_1[i] / my_list_2[j]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(div)
    return new_list
