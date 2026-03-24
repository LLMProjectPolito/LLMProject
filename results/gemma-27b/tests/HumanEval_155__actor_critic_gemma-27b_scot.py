
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
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_number_with_even_and_odd_digits():
    """Test with a number containing both even and odd digits."""
    assert even_odd_count(12345) == (2, 3)

def test_all_even_digits():
    """Test with a number containing only even digits."""
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    """Test with a number containing only odd digits."""
    assert even_odd_count(13579) == (0, 5)

def test_single_digit_even():
    """Test with a single even digit."""
    assert even_odd_count(2) == (1, 0)

def test_single_digit_odd():
    """Test with a single odd digit."""
    assert even_odd_count(1) == (0, 1)

def test_zero():
    """Test with zero."""
    assert even_odd_count(0) == (1, 0)

def test_number_containing_zero():
    """Test with a number that includes zero."""
    assert even_odd_count(102) == (2, 1)

def test_non_integer_input_string():
    """Test with a string input to verify TypeError is raised."""
    with pytest.raises(TypeError):
        even_odd_count("abc")

def test_non_integer_input_float():
    """Test with a float input to verify TypeError is raised."""
    with pytest.raises(TypeError):
        even_odd_count(123.45)

def test_large_number():
    """Test with a large number to check for potential overflow issues."""
    assert even_odd_count(1234567890) == (5, 5)

def test_small_negative_number():
    """Test with a small negative number."""
    assert even_odd_count(-1) == (0, 1)