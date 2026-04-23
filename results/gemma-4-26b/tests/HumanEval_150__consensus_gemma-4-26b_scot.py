
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # Prime numbers (should return x)
    (2, "a", "b", "a"),
    (2, "prime", "not_prime", "prime"),
    (2, 3.14, 2.71, 3.14),
    (3, "a", "b", "a"),
    (3, 10, 20, 10),
    (5, "a", "b", "a"),
    (5, 10, 20, 10),
    (5, [1, 2], {1: 2}, [1, 2]),
    (5, {"a": 1}, {"b": 2}, {"a": 1}),
    (7, 34, 12, 34),
    (7, [1, 2], {"key": "val"}, [1, 2]),
    (7, 3.14, None, 3.14),
    (11, 100, 200, 100),
    (11, 1.1, 2.2, 1.1),
    (13, 1, 0, 1),
    (13, True, False, True),
    (17, True, False, True),
    (97, "x", "y", "x"),
    (104729, "prime", "not", "prime"),
    
    # Composite numbers (should return y)
    (4, "a", "b", "b"),
    (4, "prime", "not_prime", "not_prime"),
    (4, [1, 2], [3, 4], [3, 4]),
    (6, "a", "b", "b"),
    (6, 10, 20, 20),
    (6, None, True, True),
    (8, "a", "b", "b"),
    (8, [1, 2], {"key": "val"}, {"key": "val"}),
    (8, 3.14, None, None),
    (8, None, "None", "None"),
    (9, "a", "b", "b"),
    (9, 1, 0, 0),
    (10, "a", "b", "b"),
    (12, "a", "b", "b"),
    (15, 8, 5, 5),
    (21, 1, 2, 2),
    (25, 1, 0, 0),
    (25, 1.5, 2.5, 2.5),
    (100, 1, 0, 0),
    (100, "a", "b", "b"),
    (104730, "prime", "not", "not"),
    (104730, 5, 10, 10),
    
    # Edge cases: 0, 1, and negative numbers (not prime)
    (1, "a", "b", "b"),
    (1, "x", "y", "y"),
    (0, "a", "b", "b"),
    (0, "x", "y", "y"),
    (-1, "a", "b", "b"),
    (-1, "x", "y", "y"),
    (-2, "a", "b", "b"),
    (-2, "x", "y", "y"),
    (-7, "a", "b", "b"),
    (-7, "x", "y", "y"),
    (-13, "a", "b", "b"),
])
def test_x_or_y(n, x, y, expected):
    """
    Tests x_or_y with a variety of inputs:
    - Prime numbers (returns x)
    - Composite numbers (returns y)
    - Edge cases: 0, 1, and negative integers (returns y)
    - Large prime and non-prime numbers
    - Various data types for x and y (lists, dicts, floats, None)
    """
    assert x_or_y(n, x, y) == expected