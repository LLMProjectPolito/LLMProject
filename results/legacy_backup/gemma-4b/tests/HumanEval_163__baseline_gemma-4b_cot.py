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

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(10, 5) == [6, 8]

def test_generate_integers_a_equal_b():
    assert generate_integers(5, 5) == [ ]

def test_generate_integers_large_numbers():
    assert generate_integers(100, 102) == []

def test_generate_integers_with_zero():
    assert generate_integers(20, 28) == [20, 22, 24, 26, 28]

def test_generate_integers_with_odd_numbers():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_with_mixed_numbers():
    assert generate_integers(1, 10) == [2, 4, 6, 8]