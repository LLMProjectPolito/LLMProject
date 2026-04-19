
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
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

@pytest.mark.parametrize("n, x, y, expected", [
    # Basic cases from examples
    (7, 34, 12, 34),    # 7 is prime
    (15, 8, 5, 5),      # 15 is not prime
    
    # Prime number edge cases
    (2, "Prime", "Not Prime", "Prime"),   # Smallest prime
    (3, "Prime", "Not Prime", "Prime"),   # Small odd prime
    (13, 100, 200, 100),                  # Medium prime
    (101, True, False, True),             # Larger prime
    
    # Non-prime positive cases
    (1, "Prime", "Not Prime", "Not Prime"), # 1 is not prime
    (4, "Prime", "Not Prime", "Not Prime"), # Smallest composite
    (9, "Prime", "Not Prime", "Not Prime"), # Odd composite
    (100, "Prime", "Not Prime", "Not Prime"), # Even composite
    
    # Zero and Negative numbers (not prime by definition)
    (0, "Prime", "Not Prime", "Not Prime"),
    (-1, "Prime", "Not Prime", "Not Prime"),
    (-7, "Prime", "Not Prime", "Not Prime"),
    (-11, "Prime", "Not Prime", "Not Prime"),
    
    # Testing different data types for x and y
    (5, [1, 2], [3, 4], [1, 2]),          # Lists
    (6, {"a": 1}, {"b": 2}, {"b": 2}),    # Dictionaries
    (17, None, "Value", None),            # NoneType
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected