#!/usr/bin/python3
""" minimum operations"""


def minOperations(n):
    """the fewest operations needed to result in n H characters"""
    # outputs should be min 2 chars: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            # total divisions by root = total operations
            ops += root
            # the remainder n
            n = n / root
            # reduce root to find remaining smaller vals that divide n
            root -= 1
        # increment root until it divides n
        root += 1
    return ops