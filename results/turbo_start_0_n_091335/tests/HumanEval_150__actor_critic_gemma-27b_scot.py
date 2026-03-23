import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.
    Negative numbers are treated as composite and return y.

    Examples:
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_prime_number_returns_x():
    # Test case for a prime number
    assert x_or_y(7, 34, 12) == 34
    # Test case for another prime number
    assert x_or_y(11, 100, 200) == 100
    # Test case for a small prime number
    assert x_or_y(5, 1, 0) == 1
    # Test case for a large prime number
    assert x_or_y(7919, 1000, 2000) == 1000

def test_composite_number_returns_y():
    # Test case for a composite number
    assert x_or_y(15, 8, 5) == 5
    # Test case for another composite number
    assert x_or_y(4, 1, 2) == 2
    # Test case for another composite number
    assert x_or_y(9, 10, 20) == 20
    # Test case for a large composite number
    assert x_or_y(7920, 1000, 2000) == 2000

def test_negative_number_returns_y():
    # Test case for a negative number, which should return y
    assert x_or_y(-5, 1, 2) == 2
    # Test case for another negative number, which should return y
    assert x_or_y(-1, 3, 4) == 4

def test_x_equals_y():
    # Test case where x and y are equal
    assert x_or_y(7, 5, 5) == 5
    # Test case where x and y are equal and n is composite
    assert x_or_y(12, 5, 5) == 5