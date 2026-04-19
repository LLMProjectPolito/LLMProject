
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # Prime numbers: should return x
    (2, 10, 20, 10),
    (3, "apple", "banana", "apple"),
    (5, [1], [2], [1]),
    (7, 34, 12, 34),
    (11, "Prime", "Not", "Prime"),
    (13, True, False, True),
    (17, 0, 1, 0),
    (19, 5.5, 6.6, 5.5),
    (97, "prime", "composite", "prime"),
    (101, 1, 0, 1),
    
    # Non-prime numbers: should return y
    (0, 10, 20, 20),
    (1, "apple", "banana", "banana"),
    (4, [1], [2], [2]),
    (6, 34, 12, 12),
    (8, 100, 200, 200),
    (9, True, False, False),
    (10, 0, 1, 1),
    (12, 5.5, 6.6, 6.6),
    (15, 8, 5, 5),
    (21, "prime", "composite", "composite"),
    (25, 1, 2, 2),
    (100, 1, 0, 0),
    
    # Negative numbers: not prime, should return y
    (-1, 10, 20, 20),
    (-2, 10, 20, 20),
    (-7, 10, 20, 20),
    (-11, 10, 20, 20),
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_different_types():
    # Testing with different return types to ensure robustness
    assert x_or_y(13, [1, 2], [3, 4]) == [1, 2]
    assert x_or_y(14, [1, 2], [3, 4]) == [3, 4]