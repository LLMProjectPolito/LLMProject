
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# The function is provided in the environment; we are testing it.
# from solution import even_odd_count 

@pytest.mark.parametrize("num, expected", [
    # Standard cases from examples
    (123, (1, 2)),
    (-12, (1, 1)),
    
    # Edge case: Zero
    (0, (1, 0)),
    
    # All even digits
    (2468, (4, 0)),
    (-2468, (4, 0)),
    (200, (3, 0)),
    
    # All odd digits
    (1357, (0, 4)),
    (-1357, (0, 4)),
    (111, (0, 3)),
    
    # Single digit cases
    (2, (1, 0)),
    (3, (0, 1)),
    (-2, (1, 0)),
    (-3, (0, 1)),
    
    # Large integers
    (1234567890, (5, 5)),
    (-1234567890, (5, 5)),
    (11223344556677889900, (10, 10)),
])
def test_even_odd_count_scenarios(num, expected):
    """
    Tests the even_odd_count function with various integer inputs 
    including negative numbers, zero, and large integers.
    """
    assert even_odd_count(num) == expected

def test_return_type():
    """
    Ensure the function returns a tuple as specified in the docstring.
    """
    result = even_odd_count(123)
    assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"
    assert len(result) == 2, f"Expected tuple of length 2, got {len(result)}"

def test_non_destructive():
    """
    Ensure the function does not modify the input (though integers are immutable in Python,
    this is a sanity check for the logic).
    """
    val = 123
    even_odd_count(val)
    assert val == 123