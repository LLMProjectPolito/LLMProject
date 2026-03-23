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
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0 and i < 10:
            result.append(i)
    return result

def test_ascending_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reversed_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_digits():
    assert generate_integers(10, 14) == []

def test_single_digit_range():
    assert generate_integers(1, 5) == [2, 4]

def test_range_including_ten():
    assert generate_integers(8, 12) == [8]

def test_equal_numbers_even():
    assert generate_integers(4, 4) == [4]

def test_equal_numbers_odd():
    assert generate_integers(3, 3) == []

def test_zero_in_range():
    assert generate_integers(0, 5) == [0, 2, 4]

def test_zero_to_one():
    assert generate_integers(0, 1) == [0]

def test_nine_to_ten():
    assert generate_integers(9, 10) == [8]