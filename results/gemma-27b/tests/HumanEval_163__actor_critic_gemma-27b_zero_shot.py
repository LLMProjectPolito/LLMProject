
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
    if a > b:
        a, b = b, a

    if a < 0 or b < 0:
        raise ValueError("Inputs must be positive integers.")

    result = []
    for i in range(a, b + 1):
        for digit in str(i):
            digit = int(digit)
            if digit % 2 == 0:
                result.append(digit)
    return sorted(list(set(result)))

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_range():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_odd_range():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_edge_case_0_1():
    assert generate_integers(0, 1) == [0]

def test_generate_integers_edge_case_9_10():
    assert generate_integers(9, 10) == [0]

def test_generate_integers_edge_case_1_1():
    assert generate_integers(1, 1) == []

def test_generate_integers_edge_case_0_0():
    assert generate_integers(0, 0) == [0]

def test_generate_integers_large_range():
    assert generate_integers(1, 20) == [0, 2, 4, 6, 8]

def test_generate_integers_larger_range():
    assert generate_integers(100, 110) == [0, 2, 4, 6, 8]

def test_generate_integers_negative_input_a_raises_error():
    with pytest.raises(ValueError):
        generate_integers(-5, 5)

def test_generate_integers_negative_input_b_raises_error():
    with pytest.raises(ValueError):
        generate_integers(1, -5)

def test_generate_integers_both_negative_raises_error():
    with pytest.raises(ValueError):
        generate_integers(-5, -1)

def test_generate_integers_range_with_multiple_even_digits():
    assert generate_integers(23, 28) == [2, 3, 4, 5, 6, 7, 8]

def test_generate_integers_range_with_leading_even_digit():
    assert generate_integers(20, 25) == [0, 2, 3, 4, 5]