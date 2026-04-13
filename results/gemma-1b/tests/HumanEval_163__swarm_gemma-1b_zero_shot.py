
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

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
    for num in range(a, b + 1):
        s = str(num)
        even_digits = []
        for digit in s:
            digit = int(digit)
            if digit % 2 == 0:
                even_digits.append(digit)
        even_digits.sort()
        result = even_digits
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
    for num in range(a, b + 1):
        s = str(num)
        even_digits = []
        for digit in s:
            digit = int(digit)
            if digit % 2 == 0:
                even_digits.append(digit)
        even_digits.sort()
        result = even_digits
    return result

def test_generate_integers():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(2, 1) == []
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 3) == [2]
    assert generate_integers(3, 4) == [2, 4]
    assert generate_integers(4, 5) == [2, 4]
    assert generate_integers(5, 6) == [2, 4]
    assert generate_integers(6, 7) == [2, 4]
    assert generate_integers(7, 8) == [2, 4]
    assert generate_integers(8, 9) == [2, 4]
    assert generate_integers(9, 10) == []
    assert generate_integers(1, 10) == [2]
    assert generate_integers(10, 1) == []
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(10, 10) == []