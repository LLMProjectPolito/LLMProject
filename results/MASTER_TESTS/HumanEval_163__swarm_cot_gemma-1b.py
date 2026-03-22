import pytest
from math import gcd

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
        for digit in str(num):
            digit = int(digit)
            if digit % 2 == 0:
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
        for digit in str(num):
            digit = int(digit)
            if digit % 2 == 0:
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
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(1, 6) == [2, 4, 6]
    assert generate_integers(1, 7) == [2, 4, 6, 8]
    assert generate_integers(1, 9) == [2, 4, 6, 8]
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(1, 11) == [2, 4, 6, 8]
    assert generate_integers(1, 12) == []
    print("All tests passed")