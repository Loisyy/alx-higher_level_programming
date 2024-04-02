#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_element = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            printed_elemnt += 1
    except IndexError:
        pass
    print()
    return printed_element
