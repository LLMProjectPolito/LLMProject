
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # --- Prime Numbers (Should return x) ---
    (2, 10, 20, 10),               # Smallest prime
    (3, "apple", "banana", "apple"), # Odd prime
    (7, 34, 12, 34),               # Basic prime
    (11, "Prime", "Not Prime", "Prime"),
    (13, [1], [2], [1]),           # Prime with list types
    (17, "Apple", "Banana", "Apple"),
    (19, "Apple", "Banana", "Apple"),
    (101, True, False, True),      # Larger prime

    # --- Composite Numbers (Should return y) ---
    (4, 10, 20, 20),               # Even composite
    (8, 100, 200, 200),            # Even composite
    (9, "apple", "banana", "banana"), # Odd composite
    (12, "X", "Y", "Y"),           # Even composite
    (15, 8, 5, 5),                 # Odd composite
    (21, "Apple", "Banana", "Banana"), # Composite (3*7)
    (25, "Apple", "Banana", "Banana"), # Composite (5*5)
    (100, True, False, False),     # Larger composite

    # --- Non-Prime Edges (Should return y) ---
    (1, "x", "y", "y"),            # 1 is not prime
    (0, "x", "y", "y"),            # 0 is not prime
    (-2, "x", "y", "y"),           # Negative even
    (-7, "x", "y", "y"),           # Negative odd
])
def test_x_or_y_logic(n, x, y, expected):
    """Tests the core logic: returns x if n is prime, else returns y."""
    assert x_or_y(n, x, y) == expected

def test_x_or_y_complex_types():
    """Tests that x and y can be any data type, including complex structures."""
    list_x = [1, 2, 3]
    list_y = [4, 5, 6]
    dict_x = {"status": "prime"}
    dict_y = {"status": "composite"}
    
    # Prime cases
    assert x_or_y(7, list_x, list_y) == list_x
    assert x_or_y(11, dict_x, dict_y) == dict_x
    assert x_or_y(11, {"key": "val"}, None) == {"key": "val"}
    
    # Non-prime cases
    assert x_or_y(8, list_x, list_y) == list_y
    assert x_or_y(12, dict_x, dict_y) == dict_y
    assert x_or_y(12, {"key": "val"}, None) == None