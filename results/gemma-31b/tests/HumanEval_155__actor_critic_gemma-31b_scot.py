
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# The function even_odd_count is assumed to be defined as per the problem description.

@pytest.mark.parametrize("num, expected", [
    # Standard mixed cases
    (123, (1, 2)),
    (4567, (2, 2)),
    (102, (2, 1)),
    
    # Negative cases (sign should be ignored)
    (-12, (1, 1)),
    (-123, (1, 2)),
    (-444, (3, 0)),
    (-135, (0, 3)),
    
    # Zero case (0 is even)
    (0, (1, 0)),
    
    # All even digits
    (2468, (4, 0)),
    (880, (3, 0)),
    
    # All odd digits
    (1357, (0, 4)),
    (999, (0, 3)),
    
    # Single digit cases
    (2, (1, 0)),
    (3, (0, 1)),
    (8, (1, 0)),
    (7, (0, 1)),
    
    # Large integer case
    (1234567890, (5, 5)),
    (111222333444, (6, 6)),
])
def test_even_odd_count(num, expected):
    """
    Test the even_odd_count function with a variety of inputs including
    positive, negative, zero, and large integers.
    
    Note: Equality check against a tuple implicitly validates return type and length.
    """
    assert even_odd_count(num) == expected