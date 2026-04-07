
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
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

@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (7, 34, 12, 34),
        (2, 10, 20, 10),
        (5, 100, 200, 100),
        (11, 5, 10, 5),
        (15, 8, 5, 5),
        (4, 10, 20, 20),
        (6, 100, 200, 200),
        (9, 5, 10, 10),
    ],
)
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20  # 1 is not prime
    assert x_or_y(0, 10, 20) == 20  # 0 is not prime
    assert x_or_y(-5, 10, 20) == 20 # Negative numbers are not prime
    assert x_or_y(2, 10, 10) == 10 # x and y are the same

def test_x_or_y_type_checking():
    assert x_or_y(7, "hello", 12) == "hello"
    assert x_or_y(15, 8, "world") == "world"
    assert x_or_y(7, 34.5, 12) == 34.5
    assert x_or_y(15, 8, 5.5) == 5.5
    assert x_or_y(7, True, False) == True
    assert x_or_y(15, True, False) == False
    assert x_or_y(7, [1, 2], {1: 'a'}) == [1, 2]
    assert x_or_y(15, {1: 'a'}, (1, 2)) == (1, 2)
    assert x_or_y(7, "abc", 12) == "abc"
    assert x_or_y(15, 8, "def") == "def"
    assert x_or_y(7, 12, "ghi") == 12
    assert x_or_y(15, "jkl", 8) == 8