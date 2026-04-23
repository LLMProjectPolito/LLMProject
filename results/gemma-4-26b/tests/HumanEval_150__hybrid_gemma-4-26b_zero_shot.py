
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
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

@pytest.mark.parametrize("n, x, y, expected", [
    # 1. Docstring Examples
    (7, 34, 12, 34),    # 7 is prime
    (15, 8, 5, 5),      # 15 is not prime
    
    # 2. Edge Cases: Boundary of primality (n < 2)
    (-10, "P", "NP", "NP"),
    (-1, "P", "NP", "NP"),
    (0, "P", "NP", "NP"),
    (1, "P", "NP", "NP"),
    
    # 3. Smallest Primes and Composites
    (2, "P", "NP", "P"),    # Smallest prime
    (3, "P", "NP", "P"),    # Next prime
    (4, "P", "NP", "NP"),   # Smallest composite
    (9, "P", "NP", "NP"),   # Square of a prime
    
    # 4. Boundary Conditions (Perfect Squares and Near-Squares)
    (121, "P", "NP", "NP"), # 11^2 (Boundary check)
    (127, "P", "NP", "P"),  # Prime near a square boundary
    
    # 5. Large Numbers
    (7919, "A", "B", "A"),    # 1000th prime
    (104729, "A", "B", "A"),  # 10,000th prime
    (104730, "A", "B", "B"),  # 10,000th composite
    
    # 6. Data Type Flexibility (x and y can be any type)
    (13, [1, 2], [3, 4], [1, 2]),               # Lists
    (14, [1, 2], [3, 4], [3, 4]),               # Lists
    (17, {"key": "val"}, None, {"key": "val"}), # Dictionary and None
    (18, 3.14, 2.71, 2.71),                     # Floats
    (19, True, False, True),                    # Booleans
    (20, None, True, True),                     # None and Boolean
])
def test_x_or_y_logic_and_types(n, x, y, expected):
    """Tests core logic, edge cases, large numbers, and type flexibility."""
    assert x_or_y(n, x, y) == expected

def test_x_or_y_performance():
    """Tests behavior with a very large prime number to ensure O(sqrt(n)) efficiency."""
    large_prime = 1000000007 
    assert x_or_y(large_prime, "yes", "no") == "yes"