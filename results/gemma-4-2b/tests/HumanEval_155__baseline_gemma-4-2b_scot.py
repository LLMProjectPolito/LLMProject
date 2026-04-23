
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

# STEP 1: REASONING
# The function `even_odd_count(num)` takes an integer as input and returns a tuple containing the count of even and odd digits.
# We need to create a pytest suite to test various scenarios, including:
# 1. Positive integers with even and odd digits.
# 2. Negative integers.
# 3. Integers with only even digits.
# 4. Integers with only odd digits.
# 5. Zero.
# 6. Edge cases like single-digit numbers.

# STEP 2: PLAN
# We will define pytest test functions for each scenario.
# Each test function will call `even_odd_count` with different inputs and assert the returned tuple.

# Test cases:
# - even_odd_count(123) == (1, 2)
# - even_odd_count(-12) == (1, 1)
# - even_odd_count(2468) == (4, 0)
# - even_odd_count(13579) == (0, 5)
# - even_odd_count(0) == (1, 0)
# - even_odd_count(1) == (0, 1)
# - even_odd_count(-1) == (0, 1)
# - even_odd_count(-2) == (1, 0)
# - even_odd_count(-1234567890) == (5, 5)

# STEP 3: CODE
import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num_str = str(abs(num))
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

class TestEvenOddCount:

    def test_positive_integer_with_even_and_odd_digits(self):
        assert even_odd_count(123) == (1, 2)

    def test_negative_integer(self):
        assert even_odd_count(-12) == (1, 1)

    def test_integer_with_only_even_digits(self):
        assert even_odd_count(2468) == (4, 0)

    def test_integer_with_only_odd_digits(self):
        assert even_odd_count(13579) == (0, 5)

    def test_zero(self):
        assert even_odd_count(0) == (1, 0)

    def test_single_digit_number(self):
        assert even_odd_count(1) == (0, 1)

    def test_negative_single_digit_number(self):
        assert even_odd_count(-1) == (0, 1)

    def test_negative_even_single_digit_number(self):
        assert even_odd_count(-2) == (1, 0)

    def test_large_integer(self):
        assert even_odd_count(-1234567890) == (5, 5)