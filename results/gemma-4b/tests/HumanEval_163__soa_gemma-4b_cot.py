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
    for i in range(min(a, b), max(a, b) + 1):
        s = str(i)
        if all(int(digit) % 2 == 0 for digit in s):
            result.append(i)
    return result

def test_generate_integers_normal():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 4) == [4]

def test_generate_integers_with_zeros():
    assert generate_integers(20, 28) == [20, 22, 24, 26, 28]
    assert generate_integers(28, 20) == [20, 22, 24, 26, 28]
    assert generate_integers(100, 102) == []
    assert generate_integers(102, 100) == []

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(8, 8) == [8]
    assert generate_integers(1, 2) == [2]
    assert generate_integers(1, 8) == [2, 4, 6, 8]

def test_generate_integers_large_numbers():
    assert generate_integers(1000, 1002) == []
    assert generate_integers(1000, 1004) == [1000, 1002]
    assert generate_integers(1004, 1000) == [1000, 1002]

def test_generate_integers_edge_cases():
    assert generate_integers(1, 1) == [1]
    assert generate_integers(2, 1) == [2]
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 1) == [2]
    assert generate_integers(0, 2) == [2]
    assert generate_integers(2, 0) == [2]