
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

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
    else:
        return y

### SCoT Steps:

### STEP 1: REASONING
# The function `x_or_y` checks if a number `n` is prime. If it is, it returns `x`; otherwise, it returns `y`.
# We need to test various scenarios:
# 1. n is prime: Should return x.
# 2. n is not prime: Should return y.
# 3. n is 1: Should return y.
# 4. x and y are the same: Should return x if n is prime, y otherwise.
# 5. x and y are different: Should return x if n is prime, y otherwise.
# 6. n is a large prime number.
# 7. n is a large non-prime number.

### STEP 2: PLAN
# Test functions:
# - test_prime_x
# - test_non_prime_y
# - test_n_is_one_y
# - test_x_equals_y_prime
# - test_x_equals_y_non_prime
# - test_large_prime
# - test_large_non_prime

### STEP 3: CODE
def test_prime_x():
    assert x_or_y(7, 34, 12) == 34

def test_non_prime_y():
    assert x_or_y(15, 8, 5) == 5

def test_n_is_one_y():
    assert x_or_y(1, 34, 12) == 12

def test_x_equals_y_prime():
    assert x_or_y(2, 5, 5) == 5

def test_x_equals_y_non_prime():
    assert x_or_y(4, 5, 5) == 5

def test_large_prime():
    assert x_or_y(997, 1000, 1001) == 1000

def test_large_non_prime():
    assert x_or_y(1000, 1000, 1001) == 1001