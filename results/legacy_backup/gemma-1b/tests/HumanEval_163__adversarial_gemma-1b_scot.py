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
        if even_digits:
            result.extend(even_digits)
    result.sort()
    return result

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_even_numbers():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == []

def test_generate_integers_large_numbers():
    assert generate_integers(100, 100) == [0, 2, 4, 6, 8, 0]

def test_generate_integers_negative_numbers():
    assert generate_integers(-2, 2) == [-2, 0, 2, 4]

def test_generate_integers_zero():
    assert generate_integers(0, 0) == []

def test_generate_integers_one():
    assert generate_integers(1, 1) == []