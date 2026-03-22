import pytest
import math


# Focus: Boundary Values
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

@pytest.mark.parametrize("num, expected", [
    (0, (1, 0)),  # Zero
    (1, (0, 1)),  # Smallest positive odd
    (2, (1, 0)),  # Smallest positive even
    (-1, (0, 1)), # Smallest negative odd
    (-2, (1, 0)), # Smallest negative even
    (9, (0, 1)),  # Largest single digit odd
    (8, (1, 0)),  # Largest single digit even
    (10, (1, 1)), # Smallest two-digit number
    (99, (0, 2)), # Largest two-digit odd number
    (88, (2, 0)), # Largest two-digit even number
    (123456789, (4, 5)), # All digits
    (-123456789, (4, 5)), # All digits negative
    (111111111, (0, 9)), # All odd digits
    (222222222, (9, 0)), # All even digits
])
def test_even_odd_count_boundary(num, expected):
    assert even_odd_count(num) == expected

# Focus: Negative Numbers
import pytest

def test_negative_number_even_odd():
    """Test with a negative number containing both even and odd digits."""
    assert even_odd_count(-12) == (1, 1)

def test_negative_number_all_odd():
    """Test with a negative number containing only odd digits."""
    assert even_odd_count(-135) == (0, 3)

def test_negative_number_all_even():
    """Test with a negative number containing only even digits."""
    assert even_odd_count(-246) == (3, 0)

# Focus: Digit Composition
import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(num)
    even_count = 0
    odd_count = 0
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_digit_composition_positive():
    assert even_odd_count(12345) == (2, 3)

def test_digit_composition_negative():
    assert even_odd_count(-12345) == (2, 3)

def test_digit_composition_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_digit_composition_all_odd():
    assert even_odd_count(13579) == (0, 5)

def test_digit_composition_zero():
    assert even_odd_count(0) == (1, 0)