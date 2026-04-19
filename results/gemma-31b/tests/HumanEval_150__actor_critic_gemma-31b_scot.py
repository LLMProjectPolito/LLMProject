
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# The function x_or_y is assumed to be defined in the environment as per instructions.

@pytest.mark.parametrize("n, x, y, expected", [
    (2, "prime", "not prime", "prime"),      # Smallest prime
    (3, "prime", "not prime", "prime"),      # Small odd prime
    (7, 34, 12, 34),                         # Example 1 from docstring
    (13, "A", "B", "A"),                     # Medium prime
    (101, True, False, True),                # Larger prime
    (997, "Yes", "No", "Yes"),               # Large 3-digit prime
])
def test_prime_cases(n, x, y, expected):
    """Test that the function returns x when n is a prime number."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (4, "prime", "not prime", "not prime"),  # Smallest composite
    (9, "prime", "not prime", "not prime"),  # Odd composite
    (15, 8, 5, 5),                           # Example 2 from docstring
    (100, "A", "B", "B"),                    # Even composite
    (1000, True, False, False),              # Large composite
])
def test_composite_cases(n, x, y, expected):
    """Test that the function returns y when n is a composite number."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (1, "prime", "not prime", "not prime"),  # 1 is not prime
    (0, "prime", "not prime", "not prime"),  # 0 is not prime
    (-1, "prime", "not prime", "not prime"), # Negative is not prime
    (-7, "prime", "not prime", "not prime"), # Negative prime-looking is not prime
])
def test_boundary_and_negative_cases(n, x, y, expected):
    """Test that numbers <= 1 are correctly identified as non-prime."""
    assert x_or_y(n, x, y) == expected

def test_different_types_for_x_y():
    """Verify that x and y can be of any data type (floats, lists, etc)."""
    # Testing with floats
    assert x_or_y(7, 10.5, 20.5) == 10.5
    # Testing with lists
    assert x_or_y(4, [1, 2], [3, 4]) == [3, 4]
    # Testing with None
    assert x_or_y(2, None, "Value") is None

def test_identical_x_y():
    """Verify behavior when x and y are the same value."""
    assert x_or_y(7, 100, 100) == 100
    assert x_or_y(4, 100, 100) == 100