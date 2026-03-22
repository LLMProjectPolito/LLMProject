# STEP 1: REASONING
# The function `x_or_y(n, x, y)` returns `x` if `n` is a prime number, and `y` otherwise.
# We need to test cases where n is prime and where n is not prime.
# We also need to test edge cases like n = 1, n = 2, and potentially larger numbers.
# We should also test with different values of x and y to ensure the return value is correct.

# STEP 2: PLAN
# Test functions:
# - test_prime_number: n is a prime number, should return x.
# - test_non_prime_number: n is not a prime number, should return y.
# - test_n_equals_1: n is 1, should return y.
# - test_n_equals_2: n is 2, should return x.
# - test_large_prime: n is a large prime number, should return x.
# - test_large_non_prime: n is a large non-prime number, should return y.
# - test_x_and_y_negative: x and y are negative numbers.
# - test_x_and_y_zero: x and y are zero.

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
    def test_prime_number(self):
        assert x_or_y(7, 34, 12) == 34

    def test_non_prime_number(self):
        assert x_or_y(15, 8, 5) == 5

    def test_n_equals_1(self):
        assert x_or_y(1, 10, 20) == 20

    def test_n_equals_2(self):
        assert x_or_y(2, 5, 10) == 5

    def test_large_prime(self):
        assert x_or_y(101, 100, 200) == 100

    def test_large_non_prime(self):
        assert x_or_y(100, 50, 75) == 75

    def test_x_and_y_negative(self):
        assert x_or_y(5, -34, -12) == -34

    def test_x_and_y_zero(self):
        assert x_or_y(10, 0, 0) == 0

    def test_prime_with_negative_y(self):
        assert x_or_y(11, 1, -5) == 1

    def test_non_prime_with_negative_x(self):
        assert x_or_y(4, -10, 2) == 2