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
# The function `x_or_y(n, x, y)` checks if `n` is a prime number.
# If `n` is prime, it returns `x`; otherwise, it returns `y`.
# We need to test various prime and non-prime numbers, and different values for `x` and `y`.
# Edge cases: n <= 1, n = 2 (the first prime), n = 3 (the second prime), etc.

### STEP 2: PLAN
# Test cases:
# 1. n is prime, x is returned
# 2. n is prime, y is returned (should not happen)
# 3. n is not prime, x is returned
# 4. n is not prime, y is returned
# 5. n = 1 (edge case)
# 6. n = 2 (edge case - prime)
# 7. n = 3 (edge case - prime)
# 8. n = 4 (edge case - not prime)
# 9. n = 5 (edge case - prime)
# 10. n = 6 (edge case - not prime)
# 11. n = 7 (edge case - prime)
# 12. n = 8 (edge case - not prime)
# 13. n = 9 (edge case - not prime)
# 14. n = 10 (edge case - not prime)

### STEP 3: CODE
def test_n_is_prime_x_returned():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 55, 10) == 55
    assert x_or_y(13, 99, 22) == 99

def test_n_is_prime_y_returned():
    assert x_or_y(2, 34, 12) == 12
    assert x_or_y(3, 34, 12) == 12
    assert x_or_y(5, 34, 12) == 12
    assert x_or_y(7, 34, 12) == 12

def test_n_is_not_prime_x_returned():
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(6, 34, 12) == 12
    assert x_or_y(8, 34, 12) == 12
    assert x_or_y(9, 34, 12) == 12
    assert x_or_y(10, 34, 12) == 12

def test_n_is_not_prime_y_returned():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(15, 34, 12) == 12
    assert x_or_y(20, 34, 12) == 12

def test_n_is_one():
    assert x_or_y(1, 34, 12) == 12

def test_n_is_two():
    assert x_or_y(2, 34, 12) == 34

def test_n_is_three():
    assert x_or_y(3, 34, 12) == 34

def test_n_is_four():
    assert x_or_y(4, 34, 12) == 12

def test_n_is_five():
    assert x_or_y(5, 34, 12) == 34

def test_n_is_six():
    assert x_or_y(6, 34, 12) == 12

def test_n_is_seven():
    assert x_or_y(7, 34, 12) == 34

def test_n_is_eight():
    assert x_or_y(8, 34, 12) == 12

def test_n_is_nine():
    assert x_or_y(9, 34, 12) == 12

def test_n_is_ten():
    assert x_or_y(10, 34, 12) == 12