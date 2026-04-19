
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # Primes (should return x)
    (2, 10, 20, 10),          # Smallest prime
    (3, 10, 20, 10),          # Small prime
    (5, 10, 20, 10),
    (7, 34, 12, 34),          # Example case
    (11, 100, 200, 100),
    (13, 10, 20, 10),
    (17, 10, 20, 10),
    (19, 10, 20, 10),
    (23, 10, 20, 10),
    (97, 1, 0, 1),            # Large prime
    (101, 1, 0, 1),           # Three digit prime
    
    # Non-Primes / Composites (should return y)
    (4, 10, 20, 20),          # Small composite
    (6, 10, 20, 20),
    (8, 10, 20, 20),
    (9, 10, 20, 20),          # Odd composite
    (10, 10, 20, 20),
    (12, 10, 20, 20),
    (14, 10, 20, 20),
    (15, 8, 5, 5),            # Example case
    (21, 100, 200, 200),
    (25, 10, 20, 20),
    (91, 1, 0, 0),            # Composite (7 * 13)
    (100, 10, 20, 20),
    (121, 1, 2, 2),           # Square of prime (11*11)
    (143, 1, 2, 2),           # Product of primes (11*13)
    
    # Edge Cases (Not Prime, should return y)
    (0, 10, 20, 20),
    (1, 10, 20, 20),
    (-1, 10, 20, 20),
    (-2, 10, 20, 20),
    (-3, 10, 20, 20),
    (-7, 10, 20, 20),
    (-11, 10, 20, 20),
])
def test_x_or_y(n, x, y, expected):
    """Test x_or_y with various prime and non-prime integer inputs."""
    assert x_or_y(n, x, y) == expected

def test_x_or_y_complex_types():
    """Test x_or_y with various data types as return values (x, y)."""
    # Strings
    assert x_or_y(7, "Yes", "No") == "Yes"
    assert x_or_y(12, "Yes", "No") == "No"
    
    # Lists
    list_x, list_y = [1, 2, 3], [4, 5, 6]
    assert x_or_y(5, list_x, list_y) == list_x
    assert x_or_y(6, list_x, list_y) == list_y
    
    # Booleans
    assert x_or_y(17, True, False) == True
    assert x_or_y(18, True, False) == False
    
    # Dictionaries
    dict_x, dict_y = {"result": "prime"}, {"result": "not_prime"}
    assert x_or_y(19, dict_x, dict_y) == dict_x
    assert x_or_y(20, dict_x, dict_y) == dict_y