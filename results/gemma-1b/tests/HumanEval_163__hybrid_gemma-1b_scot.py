
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
    s = set()
    for i in range(a, b + 1):
        for digit in str(i):
            digit = int(digit)
            if digit % 2 == 0:
                s.add(digit)
    return sorted(list(s))


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

def test_generate_integers_3_2():
    assert generate_integers(3, 2) == [2]

def test_generate_integers_2_3():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_2_4():
    assert generate_integers(2, 4) == [2]

def test_generate_integers_4_2():
    assert generate_integers(4, 2) == [2]

def test_generate_integers_4_3():
    assert generate_integers(4, 3) == [2]

def test_generate_integers_5_2():
    assert generate_integers(5, 2) == [2]

def test_generate_integers_6_2():
    assert generate_integers(6, 2) == [2]

def test_generate_integers_7_2():
    assert generate_integers(7, 2) == [2]

def test_generate_integers_8_2():
    assert generate_integers(8, 2) == [2]

def test_generate_integers_8_3():
    assert generate_integers(8, 3) == []

def test_generate_integers_1_4():
    assert generate_integers(1, 4) == [2]

def test_generate_integers_5_4():
    assert generate_integers(5, 4) == [2]

def test_generate_integers_6_4():
    assert generate_integers(6, 4) == [2]

def test_generate_integers_7_4():
    assert generate_integers(7, 4) == [2]

def test_generate_integers_9_4():
    assert generate_integers(9, 4) == []

def test_generate_integers_10_14():
    assert generate_integers(10, 14) == []