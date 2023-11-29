#!/usr/bin/python3
"""Implementing minimum operations to determine the least amount
of operations to create n numbers of H"""

import sys


def minOperations(n):
    """args n: amount of H occurences
    Return: count of operations to crete H
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
