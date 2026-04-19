
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively."""
    # Implementation assumed to be provided elsewhere
    pass

@pytest.mark.parametrize("num, expected", [
    # Basic positive integers
    (123, (1, 2)),
    (468, (3, 0)),
    (135, (0, 3)),
    # Negative integers (signs should be ignored)
    (-12, (1, 1)),
    (-246, (3, 0)),
    (-135, (0, 3)),
    (-101, (1, 2)),
    # Edge cases: Zero and Single Digits
    (0, (1, 0)),
    (2, (1, 0)),
    (7, (0, 1)),
    # Large numbers
    (10000000000, (10, 1)),
    (2468, (4, 0)),
    (1357, (0, 4)),
])
def test_even_odd_count_valid_inputs(num, expected):
    """Tests various valid integer inputs including negatives, zero, and large numbers."""
    assert even_odd_count(num) == expected

@pytest.mark.parametrize("invalid_input", [
    12.3,        # Float
    "123",       # String
    None,        # NoneType
    [1, 2, 3],   # List
])
def test_even_odd_count_invalid_types(invalid_input):
    """Tests that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        even_odd_count(invalid_input)