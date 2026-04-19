
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
    for char in num_str:
        if int(char) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

@pytest.mark.parametrize("num, expected", [
    # Basic examples from docstring
    (-12, (1, 1)),
    (123, (1, 2)),
    
    # Edge cases: Zero
    (0, (1, 0)),
    (-0, (1, 0)),
    
    # Single digits
    (2, (1, 0)),
    (3, (0, 1)),
    (-2, (1, 0)),
    (-3, (0, 1)),
    (-4, (1, 0)),
    (-5, (0, 1)),
    
    # All even digits
    (2468, (4, 0)),
    (-2468, (4, 0)),
    (200, (3, 0)),
    (86420, (5, 0)),
    
    # All odd digits
    (13579, (0, 5)),
    (-13579, (0, 5)),
    (1357, (0, 4)),
    (-1357, (0, 4)),
    (999, (0, 3)),
    
    # Mixed digits
    (102, (2, 1)),
    (-102, (2, 1)),
    (13570, (1, 4)),
    (102345, (3, 3)),
    (-102345, (3, 3)),
    (8642013579, (5, 5)),
    (1234567890, (5, 5)),
    (-1234567890, (5, 5)),
    (111222, (3, 3)),
    (111222333444, (6, 6)),
])
def test_even_odd_count_parametrized(num, expected):
    """Test various integer inputs including positive, negative, zero, and mixed digits."""
    assert even_odd_count(num) == expected

def test_even_odd_count_type():
    """Verify that the function returns a tuple of exactly two integers."""
    result = even_odd_count(42)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)

def test_even_odd_count_extreme_large_input():
    """Test with an extremely large integer to ensure string conversion handles scale."""
    # 2 followed by 100 zeros = 101 even digits
    num = 2 * 10**100 
    assert even_odd_count(num) == (101, 0)

def test_even_odd_count_large_mixed_integer():
    """Test with a large mixed integer to ensure no overflow or precision issues."""
    num = 22222222223333333333
    # 10 evens, 10 odds
    assert even_odd_count(num) == (10, 10)