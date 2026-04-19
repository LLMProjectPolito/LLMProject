
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),       # Standard positive integer
    (-12, (1, 1)),       # Standard negative integer
    (0, (1, 0)),         # Zero (treated as even)
    (2468, (4, 0)),      # All even digits
    (1357, (0, 4)),      # All odd digits
    (-2468, (4, 0)),     # Negative all even
    (-1357, (0, 4)),     # Negative all odd
    (100, (2, 1)),       # Multiple zeros
    (1010, (2, 2)),      # Mixed zeros and odds
    (7, (0, 1)),         # Single odd digit
    (8, (1, 0)),         # Single even digit
    (-9, (0, 1)),        # Single negative odd digit
    (-4, (1, 0)),        # Single negative even digit
    (1234567890, (5, 5)), # Large mixed integer
])
def test_even_odd_count(num, expected):
    """
    Tests the even_odd_count function with various integers including
    positive, negative, zero, and edge cases of digit composition.
    """
    assert even_odd_count(num) == expected