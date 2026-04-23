
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

# STEP 1: REASONING
# The function `x_or_y(n, x, y)` takes an integer `n` and two integers `x` and `y` as input.
# It returns `x` if `n` is a prime number, and `y` otherwise.
# We need to test the following scenarios:
# 1. `n` is a prime number and `x` is a positive integer.
# 2. `n` is a prime number and `x` is a non-positive integer.
# 3. `n` is not a prime number and `x` is a positive integer.
# 4. `n` is not a prime number and `x` is a non-positive integer.
# 5. `n` is a prime number and `y` is a positive integer.
# 6. `n` is a prime number and `y` is a non-positive integer.
# 7. `n` is not a prime number and `y` is a positive integer.
# 8. `n` is not a prime number and `y` is a non-positive integer.
# We should also test edge cases like `n` being 0 or 1.

# STEP 2: PLAN
# We will create pytest test functions for each scenario.
# Each test function will call `x_or_y` with different inputs and assert the expected output.

# STEP 3: CODE
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

def test_prime_n_positive_x():
    assert x_or_y(7, 34, 12) == 34

def test_prime_n_non_positive_x():
    assert x_or_y(7, -1, 12) == 12

def test_non_prime_n_positive_x():
    assert x_or_y(15, 8, 5) == 5

def test_non_prime_n_non_positive_x():
    assert x_or_y(15, -1, 5) == 5

def test_prime_n_positive_y():
    assert x_or_y(7, 34, 10) == 34

def test_prime_n_non_positive_y():
    assert x_or_y(7, 34, -1) == 34

def test_non_prime_n_positive_y():
    assert x_or_y(15, 8, 10) == 10

def test_non_prime_n_non_positive_y():
    assert x_or_y(15, 8, -1) == -1