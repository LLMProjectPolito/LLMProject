
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

# STEP 1: REASONING
# The function `x_or_y(n, x, y)` returns `x` if `n` is a prime number, and `y` otherwise.
# We need to test cases where n is prime and where n is not prime.
# We also need to test edge cases like n = 1, n = 2, and potentially larger numbers.
# We should also test with different values of x and y to ensure the return value is correct.

# STEP 2: PLAN
# Test functions:
# - test_prime_returns_x: Tests when n is a prime number.
# - test_non_prime_returns_y: Tests when n is not a prime number.
# - test_n_is_1_returns_y: Tests when n is 1.
# - test_n_is_2_returns_x: Tests when n is 2.
# - test_large_prime_returns_x: Tests with a larger prime number.
# - test_large_non_prime_returns_y: Tests with a larger non-prime number.
# - test_x_and_y_are_negative: Tests when x and y are negative numbers.
# - test_x_is_negative_y_is_positive: Tests when x is negative and y is positive.
# - test_x_is_positive_y_is_negative: Tests when x is positive and y is negative.

# STEP 3: CODE
import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

class TestXorY:
    def test_prime_returns_x(self):
        assert x_or_y(7, 34, 12) == 34

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5

    def test_n_is_1_returns_y(self):
        assert x_or_y(1, 10, 20) == 20

    def test_n_is_2_returns_x(self):
        assert x_or_y(2, 5, 10) == 5

    def test_large_prime_returns_x(self):
        assert x_or_y(101, 100, 200) == 100

    def test_large_non_prime_returns_y(self):
        assert x_or_y(100, 100, 200) == 200

    def test_x_and_y_are_negative(self):
        assert x_or_y(5, -34, -12) == -34

    def test_x_is_negative_y_is_positive(self):
        assert x_or_y(4, -10, 20) == 20

    def test_x_is_positive_y_is_negative(self):
        assert x_or_y(3, 10, -20) == 10