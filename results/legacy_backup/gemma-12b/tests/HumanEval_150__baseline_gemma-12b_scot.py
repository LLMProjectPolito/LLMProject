# STEP 1: REASONING
# The function `x_or_y(n, x, y)` returns `x` if `n` is a prime number, and `y` otherwise.
# We need to test cases where n is prime and where n is not prime.
# We also need to test edge cases like n = 1, n = 2, and potentially larger numbers.
# We should also test with negative numbers for n, x, and y, although the problem description doesn't explicitly mention this.
# We need to ensure the function handles different data types appropriately (integers).

# STEP 2: PLAN
# Test functions:
# - test_prime_number: n is a prime number, should return x.
# - test_non_prime_number: n is not a prime number, should return y.
# - test_n_is_one: n is 1, should return y.
# - test_n_is_two: n is 2, should return x.
# - test_negative_n: n is negative, should return y.
# - test_negative_x_and_y: x and y are negative.
# - test_large_prime: n is a large prime number.
# - test_large_non_prime: n is a large non-prime number.

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

    def test_n_is_one(self):
        assert x_or_y(1, 10, 20) == 20

    def test_n_is_two(self):
        assert x_or_y(2, 5, 10) == 5

    def test_negative_n(self):
        assert x_or_y(-5, 1, 2) == 2

    def test_negative_x_and_y(self):
        assert x_or_y(5, -1, -2) == -1

    def test_large_prime(self):
        assert x_or_y(101, 100, 200) == 100

    def test_large_non_prime(self):
        assert x_or_y(100, 100, 200) == 200

    def test_zero_n(self):
        assert x_or_y(0, 1, 2) == 2

    def test_zero_x_and_y(self):
        assert x_or_y(5, 0, 0) == 0