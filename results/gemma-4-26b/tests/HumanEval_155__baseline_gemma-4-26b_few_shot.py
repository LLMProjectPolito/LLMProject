
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_even_odd_count_provided_examples():
    """Tests the examples provided in the docstring."""
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_zero():
    """Tests the edge case of zero. 0 is an even digit."""
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digits():
    """Tests single digit positive and negative integers."""
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(-4) == (1, 0)
    assert even_odd_count(-7) == (0, 1)

def test_even_odd_count_all_even():
    """Tests numbers consisting only of even digits."""
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(802) == (3, 0)
    assert even_odd_count(-24) == (2, 0)

def test_even_odd_count_all_odd():
    """Tests numbers consisting only of odd digits."""
    assert even_odd_count(1357) == (0, 4)
    assert even_odd_count(91) == (0, 2)
    assert even_odd_count(-13) == (0, 2)

def test_even_odd_count_mixed_digits():
    """Tests numbers with a mix of even and odd digits."""
    assert even_odd_count(1024) == (3, 1)  # 0, 2, 4 are even; 1 is odd
    assert even_odd_count(55522) == (2, 3) # 2, 2 are even; 5, 5, 5 are odd
    assert even_odd_count(-101) == (1, 2)  # 0 is even; 1, 1 are odd

@pytest.mark.parametrize("num, expected", [
    (2, (1, 0)),
    (1, (0, 1)),
    (0, (1, 0)),
    (-12, (1, 1)),
    (123, (1, 2)),
    (2468, (4, 0)),
    (1357, (0, 4)),
    (100, (2, 1)),
    (-202, (3, 0)),
])
def test_even_odd_count_parameterized(num, expected):
    """Comprehensive parameterized test for various scenarios."""
    assert even_odd_count(num) == expected