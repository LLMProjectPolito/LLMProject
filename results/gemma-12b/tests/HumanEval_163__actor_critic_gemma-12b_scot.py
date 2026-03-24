
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
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers.")

    start = min(a, b)
    end = max(a, b)
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_start_is_even():
    assert generate_integers(4, 10) == [4, 6, 8, 10]

def test_end_is_even():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_equal_even():
    assert generate_integers(4, 4) == [4]

def test_equal_odd():
    assert generate_integers(3, 3) == []

def test_single_even():
    assert generate_integers(1, 3) == [2]

def test_adjacent_even():
    assert generate_integers(2, 4) == [2, 4]

def test_adjacent_odd():
    assert generate_integers(1, 3) == [2]

def test_same_odd():
    assert generate_integers(3, 3) == []

def test_negative_input():
    with pytest.raises(ValueError):
        generate_integers(-2, 8)

def test_negative_input_b():
    with pytest.raises(ValueError):
        generate_integers(2, -8)

def test_zero_input():
    with pytest.raises(ValueError):
        generate_integers(0, 8)

def test_zero_input_b():
    with pytest.raises(ValueError):
        generate_integers(2, 0)

def test_both_negative():
    with pytest.raises(ValueError):
        generate_integers(-2, -8)

def test_invalid_input_type():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)