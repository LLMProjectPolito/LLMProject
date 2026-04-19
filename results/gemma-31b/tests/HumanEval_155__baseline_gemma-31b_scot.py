
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),        # 2 is even, 1 and 3 are odd
    (-12, (1, 1)),        # 2 is even, 1 is odd
    (0, (1, 0)),          # 0 is even
    (2468, (4, 0)),       # All even
    (1357, (0, 4)),       # All odd
    (102, (2, 1)),        # 0 and 2 are even, 1 is odd
    (-444, (3, 0)),       # Negative all even
    (-111, (0, 3)),       # Negative all odd
    (1234567890, (5, 5)), # Large mixed number
    (7, (0, 1)),          # Single odd digit
    (8, (1, 0)),          # Single even digit
])
def test_even_odd_count(num, expected):
    """
    Test the even_odd_count function with various integer inputs 
    including positive, negative, zero, and large numbers.
    """
    assert even_odd_count(num) == expected