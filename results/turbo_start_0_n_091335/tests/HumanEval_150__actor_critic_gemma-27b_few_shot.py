import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.
    Negative numbers and zero are treated as non-prime and will return y.

    Examples:
    x_or_y(7, 34, 12) == 34
    x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_prime_numbers():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 1) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, 99, 0) == 99
    assert x_or_y(7919, 1, 2) == 1  # Test with a larger prime
    assert x_or_y(17, 5, 10) == 5

def test_non_prime_numbers():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 4) == 4
    assert x_or_y(8, 7, 6) == 6
    assert x_or_y(9, 10, 11) == 11
    assert x_or_y(10, 12, 13) == 13
    assert x_or_y(100, 1, 0) == 0 # Test with a larger non-prime

def test_edge_cases():
    assert x_or_y(1, 1, 2) == 2
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(-1, 1, 2) == 2

def test_same_values():
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(10, 5, 5) == 5