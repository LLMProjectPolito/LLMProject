
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

def test_generate_integers_examples():
    """Tests the examples provided in the problem description."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_ranges():
    """Tests ranges within the single-digit space (0-9)."""
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(2, 6) == [2, 4, 6]
    assert generate_integers(3, 7) == [4, 6]
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 4) == [4]

def test_generate_integers_out_of_range_values():
    """Tests ranges that fall entirely outside the single-digit even numbers."""
    assert generate_integers(10, 20) == []
    assert generate_integers(100, 1000) == []
    assert generate_integers(11, 13) == []
    assert generate_integers(15, 17) == []

def test_generate_integers_input_order_independence():
    """Tests that the order of a and b does not affect the result."""
    assert generate_integers(2, 8) == generate_integers(8, 2)
    assert generate_integers(1, 5) == generate_integers(5, 1)
    assert generate_integers(10, 14) == generate_integers(14, 10)

def test_generate_integers_ascending_order_requirement():
    """Tests that the returned list is always in ascending order."""
    # Even if input is descending, output should be ascending
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(6, 2) == [2, 4, 6]

@pytest.mark.parametrize("a, b, expected", [
    (1, 9, [2, 4, 6, 8]),
    (0, 5, [0, 2, 4]), # Testing 0 if input allows non-positive, though prompt says positive
    (7, 9, [8]),
    (9, 7, [8]),
])
def test_generate_integers_parametrized(a, b, expected):
    """Parametrized test for various boundary and edge cases."""
    assert generate_integers(a, b) == expected