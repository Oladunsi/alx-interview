#!/usr/bin/python3

import sys
"""Implementing minimum operations"""


def minOperations(n):
    """
    args n: amount of H occurences
    """
    if n <= 1:
        return 0

    minimum_ops = 0
    i = 2
    while i <= n:
        if n % i == 0:
            minimum_ops += i
            n = n / i
        else:
            i += 1
    return minimum_ops