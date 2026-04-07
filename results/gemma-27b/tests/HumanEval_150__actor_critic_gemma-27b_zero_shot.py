
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
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y  # Return y for n <= 1 as these are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 0) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, -1, 0) == -1
    assert x_or_y(17, 10, -10) == 10
    assert x_or_y(19, 0, 1) == 0
    assert x_or_y(101, 5, 6) == 5  # Test with a larger prime

def test_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 5, 1) == 1
    assert x_or_y(9, 100, 0) == 0
    assert x_or_y(10, 1, 2) == 2
    assert x_or_y(12, -1, 0) == 0
    assert x_or_y(14, 10, -10) == -10
    assert x_or_y(16, 0, 1) == 1

def test_edge_cases():
    assert x_or_y(1, 10, 20) == 20  # Test case where n is 1 (not prime)
    assert x_or_y(0, 10, 20) == 20  # Test case where n is 0 (not prime)
    assert x_or_y(-1, 10, 20) == 20 # Test case where n is negative (not prime)
    assert x_or_y(2, 0, 0) == 0  # Test case where x and y are 0 and n is prime
    assert x_or_y(4, 0, 0) == 0  # Test case where x and y are 0 and n is not prime
    assert x_or_y(2, 1, -1) == 1 # Test case where y is negative and n is prime
    assert x_or_y(4, 1, -1) == -1 # Test case where y is negative and n is not prime

def test_zero_values():
    assert x_or_y(0, 5, 0) == 0  # x is not zero, y is zero, n is not prime
    assert x_or_y(2, 0, 5) == 0  # x is zero, y is not zero, n is prime

def test_same_values():
    assert x_or_y(7, 5, 5) == 5  # x and y are the same, n is prime
    assert x_or_y(4, 5, 5) == 5  # x and y are the same, n is not prime

def test_negative_input():
    assert x_or_y(-7, 34, 12) == 12 # Test case with negative n