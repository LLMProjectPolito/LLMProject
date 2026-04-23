
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
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")

    result = []
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_basic_case():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_a_is_even():
    assert generate_integers(4, 10) == [4, 6, 8, 10]

def test_b_is_even():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_both_even():
    assert generate_integers(2, 4) == [2, 4]

def test_single_even():
    assert generate_integers(1, 2) == [2]

def test_edge_case_small_range():
    assert generate_integers(1, 3) == [2]

def test_edge_case_large_range():
    assert generate_integers(1, 100) == [i for i in range(2, 101, 2)]

def test_non_integer_input_a():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)

def test_non_integer_input_b():
    with pytest.raises(TypeError):
        generate_integers(2, 8.5)

def test_identical_inputs():
    assert generate_integers(5, 5) == []

def test_positive_input_error():
    with pytest.raises(ValueError):
        generate_integers(-2, 8)

def test_positive_input_error_b():
    with pytest.raises(ValueError):
        generate_integers(2, -8)