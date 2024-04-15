#!/usr/bin/python3
"""Defines an inherited list of class MyList."""


class MyList(list):
    """Implements functionality for a list with sorted printing."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
