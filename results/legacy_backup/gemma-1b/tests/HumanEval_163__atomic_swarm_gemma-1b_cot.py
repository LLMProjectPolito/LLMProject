import pytest
import math

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    for i in range(a, b + 1):
        s = str(i)
        even_digits = ""
        for digit in s:
            if int(digit) % 2 == 0:
                even_digits += digit
        if even_digits:
            result.append(int(even_digits))
    result.sort()
    return result

result = []
    for i in range(a, b + 1):
        s = str(i)
        if s[0] == '0' and len(s) > 1:
            continue
        if int(s) % 2 == 0:
            result.append(i)
    return result

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    for i in range(a, b + 1):
        s = str(i)
        even_digits = ""
        for digit in s:
            digit = int(digit)
            if digit % 2 == 0:
                even_digits += digit
        if even_digits:
            result.append(int(even_digits))
    result.sort()
    return result