import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num = abs(num)
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `even_odd_count` takes an integer as input and returns a tuple containing the number of even and odd digits in the integer.
# The function should handle negative integers correctly by taking the absolute value.
# The function should handle integers with zero correctly.
# The function should handle integers with only even or only odd digits correctly.

# STEP 2: PLAN - List test functions names and scenarios.
# test_even_odd_count_positive
# test_even_odd_count_negative
# test_even_odd_count_zero
# test_even_odd_count_all_even
# test_even_odd_count_all_odd
# test_even_odd_count_mixed

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-13579) == (0, 5)
    assert even_odd_count(-1234567890) == (5, 5)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_mixed():
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(246813579) == (4, 5)