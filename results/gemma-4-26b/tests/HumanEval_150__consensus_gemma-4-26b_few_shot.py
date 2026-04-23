
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
    (2, "x", "y", "x"),
    (3, 10, 20, 10),
    (5, "x", "y", "x"),
    (7, 34, 12, 34),
    (11, True, False, True),
    (13, [1], [2], [1]),
    (17, 3.14, 2.71, 3.14),
    (97, 100, 0, 100),
    (104729, "prime", "not", "prime"),
    
    # Composite numbers (should return y)
    (4, "x", "y", "y"),
    (6, "apple", "orange", "orange"),
    (8, 3.14, 2.71, 2.71),
    (9, 34, 12, 12),
    (15, 8, 5, 5),
    (25, 1, 0, 0),
    (100, "a", "b", "b"),
    (104730, "prime", "not", "not"),

    # Edge cases: Numbers <= 1 (should return y)
    (1, "x", "y", "y"),
    (0, "x", "y", "y"),
    (-1, "x", "y", "y"),
    (-7, "x", "y", "y"),
    (-10, "x", "y", "y"),
])
def test_x_or_y_logic(n, x, y, expected):
    """Tests the core logic for prime, composite, and edge case integers."""
    assert x_or_y(n, x, y) == expected

def test_x_or_y_types_and_identity():
    """Verifies type flexibility and object identity preservation."""
    # Test with dictionaries
    assert x_or_y(7, {"status": "prime"}, {"status": "not"}) == {"status": "prime"}
    assert x_or_y(8, {"status": "prime"}, {"status": "not"}) == {"status": "not"}
    
    # Test with None
    assert x_or_y(7, None, 0) is None
    assert x_or_y(8, None, 0) == 0
    
    # Test with mixed types
    assert x_or_y(13, "string", 5.5) == "string"
    assert x_or_y(14, "string", 5.5) == 5.5

    # Test identity preservation (ensures the exact object is returned)
    complex_obj = [1, 2, {"key": "val"}]
    assert x_or_y(2, complex_obj, "other") is complex_obj
    assert x_or_y(4, "other", complex_obj) is complex_obj

def test_x_or_y_large_values():
    """Tests with larger integer values for n."""
    # A large prime
    assert x_or_y(1000000007, "is_prime", "is_not_prime") == "is_prime"
    # A large composite
    assert x_or_y(1000000008, "is_prime", "is_not_prime") == "is_not_prime"