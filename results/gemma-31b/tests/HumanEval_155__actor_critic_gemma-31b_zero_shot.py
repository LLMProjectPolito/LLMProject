
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

@pytest.mark.parametrize("num, expected", [
    # Basic cases from examples
    (-12, (1, 1)),
    (123, (1, 2)),
    
    # Edge case: Zero (0 is considered an even digit)
    (0, (1, 0)),
    
    # Single digit cases
    (2, (1, 0)),
    (3, (0, 1)),
    (-2, (1, 0)),
    (-3, (0, 1)),
    
    # All even digits
    (2468, (4, 0)),
    (-2468, (4, 0)),
    (204, (3, 0)),
    
    # All odd digits
    (1357, (0, 4)),
    (-1357, (0, 4)),
    
    # Mixed digits
    (102, (2, 1)),
    (1358, (1, 3)),
    (-1358, (1, 3)),
    
    # Large numbers
    (1234567890, (5, 5)),
    (-987654321, (4, 5)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected

def test_return_type():
    """Ensure the function returns a tuple."""
    result = even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2