
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
        even_digits = [digit for digit in s if int(digit) % 2 == 0]
        even_digits.sort()
        result.extend(even_digits)
    return result

def test_generate_integers_2_8():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_8_2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_10_14():
    assert generate_integers(10, 14) == []

def test_generate_integers_1_2():
    assert generate_integers(1, 2) == [2]

def test_generate_integers_2_1():
    assert generate_integers(2, 1) == [2]

def test_generate_integers_1_3():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_3_1():
    assert generate_integers(3, 1) == [2]