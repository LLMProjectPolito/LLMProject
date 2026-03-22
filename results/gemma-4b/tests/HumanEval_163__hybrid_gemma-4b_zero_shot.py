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
    for i in range(a, b + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 4) == [4]
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(6, 6) == [6]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 3) == []
    assert generate_integers(5, 7) == []
    assert generate_integers(9, 11) == []

def test_generate_integers_with_mixed_digits():
    assert generate_integers(12, 16) == [2, 4, 6]
    assert generate_integers(14, 18) == [4, 6, 8]
    assert generate_integers(20, 25) == [2, 4]
    assert generate_integers(22, 28) == [2, 4, 6, 8]

def test_generate_integers_large_range():
    assert generate_integers(100, 105) == [0, 2, 4, 6, 8]
    assert generate_integers(200, 205) == [0, 2, 4, 6, 8]
    assert generate_integers(1000, 1005) == [0, 2, 4, 6, 8]

def test_generate_integers_edge_cases():
    assert generate_integers(0, 2) == [2]
    assert generate_integers(2, 0) == [2]
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 3) == [2]
    assert generate_integers(3, 2) == [2]
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(10, 1) == [2, 4, 6, 8]