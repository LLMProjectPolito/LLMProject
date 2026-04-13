
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
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")

    digits = set()
    for i in range(min(a, b), max(a, b) + 1):
        for digit in str(i):
            digit = int(digit)
            if digit % 2 == 0:
                digits.add(digit)
    return sorted(list(digits))

def test_generate_integers_basic_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_range():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_large_numbers():
    assert generate_integers(200, 208) == [0, 2, 8]

def test_generate_integers_mixed_digits():
    assert generate_integers(12, 15) == [2, 4]

def test_generate_integers_negative_a():
    with pytest.raises(ValueError):
        generate_integers(-1, 5)

def test_generate_integers_negative_b():
    with pytest.raises(ValueError):
        generate_integers(1, -5)

def test_generate_integers_negative_both():
    with pytest.raises(ValueError):
        generate_integers(-1, -5)

def test_generate_integers_equal_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_large_range():
    assert generate_integers(1000, 1010) == [0]