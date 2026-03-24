
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_positive_numbers():
    assert even_odd_count(123456) == (3, 3)
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_numbers():
    assert even_odd_count(-123456) == (3, 3)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-13579) == (0, 5)

def test_single_even_digit():
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    assert even_odd_count(1) == (0, 1)

def test_edge_cases():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(2**31 - 1) == (8, 8)  # Max int
    assert even_odd_count(-2**31) == (8, 8)  # Min int
    assert even_odd_count(-2147483648) == (4, 5)
    assert even_odd_count(2147483647) == (4, 5)
    assert even_odd_count(-1234567890) == (5, 5) # Large negative number

def test_type_checking():
    with pytest.raises(TypeError):
        even_odd_count("123")
    with pytest.raises(TypeError):
        even_odd_count(12.34)
    with pytest.raises(TypeError):
        even_odd_count(None)