
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
    and b, in ascending order. Only single-digit even numbers are returned.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    if a < 0 or b < 0:
        raise ValueError("Inputs must be positive integers.")
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0 and 0 <= i <= 9:
            result.append(i)
    return result

def test_normal_case():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_no_even_digits():
    assert generate_integers(10, 14) == []

def test_single_digit_range():
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 2) == [2]

def test_range_with_one_even():
    assert generate_integers(1, 3) == [2]
    assert generate_integers(3, 5) == [4]

def test_range_with_multiple_even():
    assert generate_integers(1, 6) == [2, 4, 6]
    assert generate_integers(5, 9) == [6, 8]

def test_start_at_zero():
    assert generate_integers(0, 5) == [2, 4]

def test_end_at_nine():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_large_range_no_evens():
    assert generate_integers(11, 15) == []

def test_large_range_with_evens():
    assert generate_integers(11, 18) == []

def test_a_equals_b_and_even():
    assert generate_integers(4, 4) == [4]

def test_a_equals_b_and_odd():
    assert generate_integers(3, 3) == []

def test_even_a_odd_b():
    assert generate_integers(2, 5) == [2, 4]

def test_odd_a_even_b():
    assert generate_integers(1, 6) == [2, 4, 6]

def test_negative_input():
    with pytest.raises(ValueError):
        generate_integers(-5, 5)

def test_negative_range():
    with pytest.raises(ValueError):
        generate_integers(-2, -1)