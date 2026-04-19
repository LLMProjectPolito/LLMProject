
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def test_x_or_y_basic_primes():
    """Test standard prime numbers to ensure x is returned."""
    # Smallest prime
    assert x_or_y(2, "prime", "not prime") == "prime"
    # Odd primes
    assert x_or_y(3, 10, 20) == 10
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(13, True, False) == True
    # Larger prime
    assert x_or_y(101, "x", "y") == "x"

def test_x_or_y_basic_composites():
    """Test standard composite numbers to ensure y is returned."""
    # Even composites
    assert x_or_y(4, "x", "y") == "y"
    assert x_or_y(10, 100, 200) == 200
    # Odd composites
    assert x_or_y(9, "x", "y") == "y"
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(25, "x", "y") == "y"

def test_x_or_y_edge_cases_n():
    """Test critical boundary values for n where primality logic often fails."""
    # 1 is NOT a prime number
    assert x_or_y(1, "x", "y") == "y", "Failed: 1 should not be considered prime"
    # 0 is NOT a prime number
    assert x_or_y(0, "x", "y") == "y", "Failed: 0 should not be considered prime"
    # Negative numbers are NOT prime
    assert x_or_y(-2, "x", "y") == "y", "Failed: Negative numbers should not be prime"
    assert x_or_y(-7, "x", "y") == "y", "Failed: Negative numbers should not be prime"

def test_x_or_y_value_types():
    """Ensure the function handles various types for x and y without crashing."""
    # Testing with None, lists, and mixed types
    assert x_or_y(7, None, [1, 2]) is None
    assert x_or_y(8, None, [1, 2]) == [1, 2]
    assert x_or_y(7, {"key": "val"}, 123) == {"key": "val"}

def test_x_or_y_identical_values():
    """Test case where x and y are the same value."""
    assert x_or_y(7, 50, 50) == 50
    assert x_or_y(8, 50, 50) == 50

@pytest.mark.parametrize("n, expected_return", [
    (17, 'x'), (19, 'x'), (23, 'x'), (29, 'x'), (31, 'x'), # Primes
    (16, 'y'), (20, 'y'), (21, 'y'), (27, 'y'), (33, 'y'), # Composites
])
def test_x_or_y_parametrized(n, expected_return):
    """Bulk test for a range of numbers to ensure consistency."""
    assert x_or_y(n, 'x', 'y') == expected_return