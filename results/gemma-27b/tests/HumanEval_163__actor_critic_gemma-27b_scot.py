
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
    Given two positive integers a and b, return the even numbers between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => [10, 12, 14]
    """
    if a > b:
        a, b = b, a
    if a < 0 or b < 0:
        raise ValueError("Inputs must be positive integers.")

    result = [i for i in range(a, b + 1) if i % 2 == 0]
    return sorted(result)


def test_docstring_example_1():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_docstring_example_2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_docstring_example_3():
    assert generate_integers(10, 14) == [10, 12, 14]

def test_zero_a():
    assert generate_integers(0, 5) == [0, 2, 4]

def test_zero_b():
    assert generate_integers(2, 0) == [0, 2, 4]

def test_negative_input():
    with pytest.raises(ValueError):
        generate_integers(-5, 5)

def test_both_negative_inputs():
    with pytest.raises(ValueError):
        generate_integers(-8, -2)

def test_single_digit_even():
    assert generate_integers(2, 2) == [2]

def test_single_digit_odd():
    assert generate_integers(1, 1) == []

def test_large_range():
    assert generate_integers(100, 108) == [100, 102, 104, 106, 108]

def test_mixed_digits():
    assert generate_integers(12, 15) == [12, 14]

def test_no_even_digits():
    assert generate_integers(11, 15) == []

def test_overlapping_even_digits():
    assert generate_integers(22, 24) == [22, 24]

def test_large_numbers_with_even_digits():
    assert generate_integers(2000, 2008) == [2000, 2002, 2004, 2006, 2008]

def test_equal_odd():
    assert generate_integers(3, 3) == []

def test_equal_even():
    assert generate_integers(4, 4) == [4]