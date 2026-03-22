# STEP 1: REASONING
# The function `x_or_y` takes an integer `n`, and two values `x` and `y` as input.
# It checks if `n` is a prime number. If `n` is prime, it returns `x`. Otherwise, it returns `y`.
# We need to test the function with prime and non-prime numbers to ensure it behaves as expected.
# We also need to test with different values of `x` and `y` to ensure they are returned correctly.
# Edge cases to consider: n = 1 (not prime), n = 2 (prime), negative n (should probably treat as non-prime).

# STEP 2: PLAN
# 1. test_x_or_y_prime: Test with a prime number for n.
# 2. test_x_or_y_not_prime: Test with a non-prime number for n.
# 3. test_x_or_y_n_equals_1: Test with n = 1 (not prime).
# 4. test_x_or_y_n_equals_2: Test with n = 2 (prime).
# 5. test_x_or_y_negative_n: Test with a negative number for n.
# 6. test_x_or_y_different_x_y: Test with different values for x and y.
# 7. test_x_or_y_same_x_y: Test with the same value for x and y.

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

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(2, 5, 6) == 5

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(9, 1, 0) == 0

def test_x_or_y_n_equals_1():
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_n_equals_2():
    assert x_or_y(2, 30, 40) == 30

def test_x_or_y_negative_n():
    assert x_or_y(-5, 100, 200) == 200

def test_x_or_y_different_x_y():
    assert x_or_y(13, 100, 200) == 100
    assert x_or_y(8, 500, 600) == 600

def test_x_or_y_same_x_y():
    assert x_or_y(17, 7, 7) == 7
    assert x_or_y(6, 9, 9) == 9