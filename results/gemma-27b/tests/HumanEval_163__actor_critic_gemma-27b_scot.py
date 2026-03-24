
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
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result


def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_numbers():
    assert generate_integers(11, 13) == []

def test_generate_integers_equal_inputs_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_single_digit_range():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_multi_digit_range():
    assert generate_integers(20, 25) == [20, 22, 24]

def test_generate_integers_boundary_case():
    assert generate_integers(10, 14) == []

def test_generate_integers_large_range():
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_generate_integers_negative_input():
    with pytest.raises(ValueError):
        generate_integers(-5, 5)

def test_generate_integers_both_even():
    assert generate_integers(2, 4) == [2, 4]

def test_generate_integers_odd_range():
    assert generate_integers(3, 6) == [4, 6]