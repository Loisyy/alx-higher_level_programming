#!/usr/bin/python3
"""
Defines the MyList class, which inherits from the built-in list class.
"""


class MyList(list):
    """
    Implements functionality for a list with sorted printing.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))
