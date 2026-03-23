import math

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
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

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(5, 5, 10) == 5

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 20) == 20

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(-1, 5, 10) == 10
    assert x_or_y(1, 5, 10) == 10
    assert x_or_y(2, 5, 10) == 5