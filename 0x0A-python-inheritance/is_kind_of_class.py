#!/usr/bin/python3
"""
Defines a function that checks if an object is an instance of, or if the object
is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of a
    class that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or a
        subclass; False otherwise.
    """
    return isinstance(obj, a_class)
