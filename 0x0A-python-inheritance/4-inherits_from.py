#!/usr/bin/python3
"""
Defines a function that checks if an object is an instance of a class that
inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of a subclass of the specified
        class; False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
