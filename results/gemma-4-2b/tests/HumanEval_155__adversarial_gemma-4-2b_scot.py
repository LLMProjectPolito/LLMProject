
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
    num = abs(int(num))
    even_count = 0
    odd_count = 0
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


def test_even_odd_count_positive_single_digit():
    assert even_odd_count(5) == (0, 1)

def test_even_odd_count_positive_multiple_digits():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 1)

def test_even_odd_count_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_mixed_digits():
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_float():
    with pytest.raises(TypeError):
        even_odd_count(3.14)

def test_even_odd_count_string():
    with pytest.raises(TypeError):
        even_odd_count("123")