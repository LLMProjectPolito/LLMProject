import pytest

def x_or_y(n, x, y):
    """
    Determines if a number is prime or not.

    Args:
        n: The number to check.
        x: The value to return if n is prime.
        y: The value to return if n is not prime.

    Returns:
        The value to return if n is prime, otherwise the value of y.
    """
    if n > 1:
        for i in range(2, int(n**0.5) + 1):  # Optimized loop
            if n % i == 0:
                return i
    else:
        return y

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(2, 3, 5) == 5
    assert x_or_y(3, 3, 3) == 3
    assert x_or_y(4, 6, 2) == 2
    assert x_or_y(9, 11, 1) == 1
    assert x_or_y(1, 1, 1) == 1
    assert x_or_y(1, 2, 1) == 1
    assert x_or_y(1, 3, 1) == 1
    assert x_or_y(1, 4, 1) == 1
    assert x_or_y(1, 5, 1) == 1
    assert x_or_y(1, 6, 1) == 1
    assert x_or_y(1, 7, 1) == 1
    assert x_or_y(1, 8, 1) == 1
    assert x_or_y(1, 9, 1) == 1
    assert x_or_y(1, 10, 1) == 1
    assert x_or_y(1, 11, 1) == 1
    assert x_or_y(1, 12, 1) == 1
    assert x_or_y(1, 13, 1) == 1
    assert x_or_y(1, 14, 1) == 1
    assert x_or_y(1, 15, 1) == 1
    assert x_or_y(1, 16, 1) == 1
    assert x_or_y(1, 17, 1) == 1
    assert x_or_y(1, 18, 1) == 1
    assert x_or_y(1, 19, 1) == 1
    assert x_or_y(1, 20, 1) == 1
    assert x_or_y(1, 21, 1) == 1
    assert x_or_y(1, 22, 1) == 1
    assert x_or_y(1, 23, 1) == 1
    assert x_or_y(1, 24, 1) == 1
    assert x_or_y(1, 25, 1) == 1
    assert x_or_y(1, 26, 1) == 1
    assert x_or_y(1, 27, 1) == 1
    assert x_or_y(1, 28, 1) == 1
    assert x_or_y(1, 29, 1) == 1
    assert x_or_y(1, 30, 1) == 1
    assert x_or_y(1, 31, 1) == 1
    assert x_or_y(1, 32, 1) == 1
    assert x_or_y(1, 33, 1) == 1
    assert x_or_y(1, 34, 1) == 1
    print("All tests passed")