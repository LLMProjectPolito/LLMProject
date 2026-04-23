
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    s = str(abs(num))
    evens = sum(1 for d in s if int(d) % 2 == 0)
    odds = len(s) - evens
    return (evens, odds)

@pytest.mark.parametrize("input_val, expected_output", [
    # Docstring examples
    (123, (1, 2)),
    (-12, (1, 1)),
    
    # Single digit cases
    (0, (1, 0)),      # 0 is even
    (1, (0, 1)),      # 1 is odd
    (2, (1, 0)),      # 2 is even
    (7, (0, 1)),      # 7 is odd
    (8, (1, 0)),      # 8 is even
    (9, (0, 1)),      # 9 is odd
    
    # Negative numbers
    (-5, (0, 1)),
    (-246, (3, 0)),
    (-101, (1, 2)),
    (-1357, (0, 4)),
    (-987654321, (4, 5)),
    
    # All even / All odd sequences
    (2468, (4, 0)),
    (1357, (0, 4)),
    (222, (3, 0)),
    (111, (0, 3)),
    (2046, (4, 0)),
    (13579, (0, 5)),
    (2222222222, (10, 0)),
    (1111111111, (0, 10)),
    
    # Numbers containing zero / Mixed digits
    (102, (2, 1)),
    (1000, (3, 1)),
    (2001, (3, 1)),
    (20406, (5, 0)),
    
    # Large numbers
    (1029384756, (5, 5)),
    (1234567890, (5, 5)),
    (9876543210, (5, 5)),
])
def test_even_odd_count_logic(input_val, expected_output):
    """Test various integer inputs including negative, zero, and large numbers."""
    assert even_odd_count(input_val) == expected_output

def test_even_odd_count_metadata():
    """Ensure the return type is a tuple of exactly two integers."""
    result = even_odd_count(42)
    assert isinstance(result, tuple), "Return type must be a tuple"
    assert len(result) == 2, "Tuple must contain exactly two elements"
    assert isinstance(result[0], int), "First element must be an integer"
    assert isinstance(result[1], int), "Second element must be an integer"

def test_even_odd_count_immutability():
    """Ensure the function returns an immutable tuple."""
    result = even_odd_count(123)
    with pytest.raises(TypeError):
        # Attempting to mutate a tuple should raise a TypeError
        result[0] = 5