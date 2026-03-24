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
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

def test_generate_integers_2_8():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_8_2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_10_14():
    assert generate_integers(10, 14) == []

def test_generate_integers_2_2():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_4_4():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_1_1():
    assert generate_integers(1, 1) == []

def test_generate_integers_3_3():
    assert generate_integers(3, 3) == []

def test_generate_integers_5_5():
    assert generate_integers(5, 5) == []

def test_generate_integers_7_7():
    assert generate_integers(7, 7) == []

def test_generate_integers_20_22():
    assert generate_integers(20, 22) == [2, 2]