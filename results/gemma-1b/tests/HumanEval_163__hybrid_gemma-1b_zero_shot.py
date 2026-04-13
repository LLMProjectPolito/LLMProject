
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
        for digit in str(num):
            if int(digit) % 2 == 0:
                result.append(num)
                break
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

def test_generate_integers_1_4():
    assert generate_integers(1, 4) == [2]

def test_generate_integers_4_1():
    assert generate_integers(4, 1) == [2]

def test_generate_integers_1_5():
    assert generate_integers(1, 5) == [2]

def test_generate_integers_5_1():
    assert generate_integers(5, 1) == [2]

def test_generate_integers_1_6():
    assert generate_integers(1, 6) == [2]

def test_generate_integers_6_1():
    assert generate_integers(6, 1) == [2]

def test_generate_integers_1_7():
    assert generate_integers(1, 7) == [2]

def test_generate_integers_7_1():
    assert generate_integers(7, 1) == [2]

def test_generate_integers_1_8():
    assert generate_integers(1, 8) == [2]

def test_generate_integers_8_8():
    assert generate_integers(8, 8) == []