
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
        for digit in s:
            if int(digit) % 2 == 0:
                result.append(num)
                break
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
        for digit in s:
            if int(digit) % 2 == 0:
                result.append(num)
                break
    return result

def test_generate_integers():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(2, 10) == [2, 4, 6, 8]
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 2) == [2]
    assert generate_integers(1, 3) == []
    assert generate_integers(1, 4) == [2, 4]
    assert generate_integers(1, 5) == []
    assert generate_integers(1, 6) == [2, 4, 6]
    assert generate_integers(1, 7) == []
    assert generate_integers(1, 8) == [2, 4, 6, 8]
    assert generate_integers(2, 10) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    print("All tests passed")