
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# The function even_odd_count is assumed to be imported or defined in the scope

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),          # Standard positive integer
    (-12, (1, 1)),          # Negative integer (sign should be ignored)
    (0, (1, 0)),            # Zero (0 is an even digit)
    (246, (3, 0)),          # All even digits
    (135, (0, 3)),          # All odd digits
    (10, (1, 1)),           # Mixed digits including zero
    (7, (0, 1)),            # Single digit odd
    (8, (1, 0)),            # Single digit even
    (-7, (0, 1)),           # Single digit negative odd
    (-8, (1, 0)),           # Single digit negative even
    (1000000, (6, 1)),      # Large number (six 0s, one 1)
    (2222222222, (10, 0)),  # Large even number
    (1111111111, (0, 10)),  # Large odd number
])
def test_even_odd_count_logic(num, expected):
    """Tests the core logic for various integer scenarios including negatives and zero."""
    assert even_odd_count(num) == expected

def test_return_type_and_structure():
    """Ensures the function returns a tuple containing exactly two integers."""
    result = even_odd_count(42)
    assert isinstance(result, tuple), "Output must be a tuple"
    assert len(result) == 2, "Output tuple must have exactly two elements"
    assert isinstance(result[0], int), "First element must be an integer"
    assert isinstance(result[1], int), "Second element must be an integer"

@pytest.mark.parametrize("invalid_input", [
    ("123"),       # String
    (12.3),        # Float
    (None),        # NoneType
    ([1, 2]),      # List
    (complex(1, 2)) # Complex number
])
def test_input_type_safety(invalid_input):
    """
    Ensures the function raises a TypeError when provided with non-integer inputs.
    A robust implementation should strictly enforce the 'integer' requirement.
    """
    with pytest.raises(TypeError):
        even_odd_count(invalid_input)

def test_large_integer_performance():
    """Tests behavior with extremely large integers to ensure no overflow or recursion issues."""
    large_num = int("1" * 1000 + "2" * 1000)
    # 1000 ones (odd), 1000 twos (even)
    assert even_odd_count(large_num) == (1000, 1000)