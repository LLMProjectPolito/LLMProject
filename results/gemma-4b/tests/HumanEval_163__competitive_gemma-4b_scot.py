
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
    if a <= b:
        for i in range(a, b + 1):
            s = str(i)
            for digit in s:
                digit = int(digit)
                if digit % 2 == 0:
                    if digit not in result:
                        result.append(digit)
    else:
        for i in range(a, b - 1, -1):
            s = str(i)
            for digit in s:
                digit = int(digit)
                if digit % 2 == 0:
                    if digit not in result:
                        result.append(digit)
    result.sort()
    return result

def test_generate_integers_2_8():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_8_2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_10_14():
    assert generate_integers(10, 14) == []

def test_generate_integers_1_9():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_2_2():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_4_4():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_1_1():
    assert generate_integers(1, 1) == []

def test_generate_integers_20_22():
    assert generate_integers(20, 22) == [2, 2]

def test_generate_integers_123456789_123456780():
    assert generate_integers(123456789, 123456780) == [2, 4, 6, 8, 0]

def test_generate_integers_1_10():
    assert generate_integers(1, 10) == [2, 4, 6, 8]

def test_generate_integers_11_11():
    assert generate_integers(11, 11) == []