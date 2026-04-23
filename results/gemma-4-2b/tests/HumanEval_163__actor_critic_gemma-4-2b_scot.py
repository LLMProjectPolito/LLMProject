
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
    if a > b:
        return []

    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_negative_numbers():
    assert generate_integers(-2, -1) == [-2]
    assert generate_integers(-1, -3) == [-2, -4, -6, -8]

def test_a_greater_than_b():
    assert generate_integers(5, 2) == []
    assert generate_integers(10, 5) == []

def test_close_numbers():
    assert generate_integers(1000, 1002) == [1000, 1002]
    assert generate_integers(1001, 1003) == [1002]

def test_large_numbers():
    assert generate_integers(10000, 10005) == [10000, 10002, 10004]
    assert generate_integers(100000, 100005) == [100000, 100002, 100004]