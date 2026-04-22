
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("input_num, expected", [
    (0, (1, 0)),                # Zero (0 is even)
    (2, (1, 0)),                # Single digit even
    (7, (0, 1)),                # Single digit odd
    (-4, (1, 0)),               # Negative single even
    (-5, (0, 1)),               # Negative single odd
    (123, (1, 2)),              # Positive mixed
    (-12, (1, 1)),              # Negative mixed
    (10, (1, 1)),               # Positive mixed with zero
    (2468, (4, 0)),             # All even
    (1357, (0, 4)),             # All odd
    (-246, (3, 0)),             # Negative all even
    (-135, (0, 3)),             # Negative all odd
    (12345, (2, 3)),            # Multiple digits mixed
    (1234567890, (5, 5)),       # Large number mixed
    (12345678901234567890, (10, 10)), # Very large number
    (999999999, (0, 9)),        # Large number all odd
    (888888888, (9, 0)),        # Large number all even
])
def test_even_odd_count(input_num, expected):
    """Tests the even_odd_count function with various integer inputs."""
    assert even_odd_count(input_num) == expected

def test_even_odd_count_return_type():
    """Ensures the return type is a tuple of length 2."""
    result = even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_even_odd_count_element_types():
    """Ensures the elements within the tuple are integers."""
    result = even_odd_count(123)
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)