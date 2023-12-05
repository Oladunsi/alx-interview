#!/usr/bin/python
"""A representation of pascal triangle"""


def pascal_triangle(n):
    """A function that implements the pascal triangle application
       and returns a list of list representing the pascal triangle"""

    outer_box = []
    if n > 0:
        for i in range(1, n + 1):
            inner_box = []
            c = 1
            for j in range(1, i + 1):
                inner_box.append(c)
                c = c * (i - j) // j
            outer_box.append(inner_box)
    return outer_box
