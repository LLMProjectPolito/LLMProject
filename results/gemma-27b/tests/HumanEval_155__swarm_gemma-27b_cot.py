
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_negative_number_with_zero():
    """Test case for a negative number containing zero."""
    assert even_odd_count(-102) == (2, 1)

def test_even_odd_count_negative_number_with_zero():
    assert even_odd_count(-120) == (2, 1)