import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

# STEP 1: REASONING
# The function x_or_y(n, x, y) returns x if n is prime, and y otherwise.
# We need to test cases where n is prime and where n is not prime.
# Edge cases include n <= 1, and small prime numbers.
# We should also test with different values of x and y.

# STEP 2: PLAN
# Test functions:
# - test_prime_number: Tests with a prime number.
# - test_not_prime_number: Tests with a non-prime number.
# - test_n_less_than_equal_to_one: Tests with n <= 1.
# - test_small_prime: Tests with a small prime number (2, 3, 5, 7).
# - test_x_and_y_equal: Tests when x and y are equal.
# - test_large_prime: Tests with a larger prime number.
# - test_large_not_prime: Tests with a larger non-prime number.

# STEP 3: CODE
def test_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(13, 5, 6) == 5

def test_not_prime_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(9, 7, 8) == 8

def test_n_less_than_equal_to_one():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 5, 10) == 10
    assert x_or_y(-5, 1, 2) == 2

def test_small_prime():
    assert x_or_y(2, 1, 2) == 1
    assert x_or_y(3, 3, 4) == 3
    assert x_or_y(5, 5, 6) == 5
    assert x_or_y(7, 7, 8) == 7

def test_x_and_y_equal():
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(10, 5, 5) == 5

def test_large_prime():
    assert x_or_y(7919, 1000, 2000) == 1000
    assert x_or_y(10007, 1, 2) == 1

def test_large_not_prime():
    assert x_or_y(10000, 1, 2) == 2
    assert x_or_y(7920, 3, 4) == 4