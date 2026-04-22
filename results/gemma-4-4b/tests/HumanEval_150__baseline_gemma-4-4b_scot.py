
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    return y

import pytest

# STEP 1: REASONING
# The function `x_or_y` takes an integer `n`, and two integers `x` and `y` as input.
# It checks if `n` is a prime number. If it is, it returns `x`. Otherwise, it returns `y`.
# We need to test various scenarios:
# 1. `n` is a prime number.
# 2. `n` is not a prime number.
# 3. `n` is 0 or 1 (edge cases).
# 4. `x` and `y` are positive integers.
# 5. `x` and `y` are negative integers.
# 6. `x` and `y` are zero.
# 7. `x` and `y` are large numbers.

# STEP 2: PLAN
# Test functions:
# test_prime_n_returns_x: Test when n is prime, x is returned.
# test_non_prime_n_returns_y: Test when n is not prime, y is returned.
# test_n_is_zero_returns_y: Test when n is 0, y is returned.
# test_n_is_one_returns_y: Test when n is 1, y is returned.
# test_positive_x_y: Test with positive x and y.
# test_negative_x_y: Test with negative x and y.
# test_x_is_zero: Test when x is zero.
# test_y_is_zero: Test when y is zero.
# test_large_numbers: Test with large numbers for n, x, and y.

# STEP 3: CODE
class TestXOrY:
    def test_prime_n_returns_x(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(13, 5, 2) == 5
        assert x_or_y(2, 10, 5) == 10
        assert x_or_y(3, 1, 0) == 1

    def test_non_prime_n_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 10, 5) == 5
        assert x_or_y(6, 1, 0) == 0
        assert x_or_y(8, 1, 0) == 0

    def test_n_is_zero_returns_y(self):
        assert x_or_y(0, 10, 5) == 5
        assert x_or_y(0, -1, 0) == 0

    def test_n_is_one_returns_y(self):
        assert x_or_y(1, 10, 5) == 5
        assert x_or_y(1, -1, 0) == 0

    def test_positive_x_y(self):
        assert x_or_y(5, 10, 20) == 10
        assert x_or_y(7, 1, 2) == 1

    def test_negative_x_y(self):
        assert x_or_y(5, -10, -20) == -10
        assert x_or_y(7, -1, -2) == -1

    def test_x_is_zero(self):
        assert x_or_y(5, 0, 20) == 20
        assert x_or_y(7, 0, 1) == 0

    def test_y_is_zero(self):
        assert x_or_y(5, 10, 0) == 10
        assert x_or_y(7, 1, 0) == 1

    def test_large_numbers(self):
        assert x_or_y(1000000007, 1, 0) == 1
        assert x_or_y(1000000000, 1, 0) == 0
        assert x_or_y(999999999, 1, 0) == 0