
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
            if int(digit) % 2 == 0:
                s.add(i)
    return sorted(list(s))

def test_generate_integers():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 1) == [2]
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 1) == []
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 3) == []
    assert generate_integers(1, 3) == []
    assert generate_integers(3, 4) == [3]
    assert generate_integers(4, 5) == [4]
    assert generate_integers(5, 6) == [5]
    assert generate_integers(6, 7) == []
    assert generate_integers(7, 8) == [7]
    assert generate_integers(8, 9) == []
    assert generate_integers(9, 10) == []
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(10, 1) == []
    assert generate_integers(1, 10) == [2, 4, 6, 8]