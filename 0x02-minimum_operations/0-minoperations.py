#!/usr/bin/python3
"""method that calculates the fewest number of operations
needed to result in exactly n H characters in the file"""


def minOperations(n: int) -> int:
    """method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file"""
    num: int = 0
    for i in range(2, n + 1):
        while n % i == 0:
            num += i
            n //= i
    return num
