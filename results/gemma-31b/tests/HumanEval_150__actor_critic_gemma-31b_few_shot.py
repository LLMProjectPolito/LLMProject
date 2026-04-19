
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def test_x_or_y_prime():
    """Test cases where n is a prime number (should return x)."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, "apple", "banana") == "apple"
    assert x_or_y(3, 100, 200) == 100
    assert x_or_y(13, True, False) == True
    assert x_or_y(101, [1], [2]) == [1]

def test_x_or_y_not_prime():
    """Test cases where n is a composite number (should return y)."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, "apple", "banana") == "banana"
    assert x_or_y(9, 100, 200) == 200
    assert x_or_y(100, True, False) == False

def test_x_or_y_edge_cases():
    """Test edge cases for primality: 0, 1, and negative numbers."""
    # 1 is not a prime number
    assert x_or_y(1, "prime", "not prime") == "not prime"
    # 0 is not a prime number
    assert x_or_y(0, "prime", "not prime") == "not prime"
    # Negative numbers are not prime
    assert x_or_y(-7, "prime", "not prime") == "not prime"
    assert x_or_y(-2, "prime", "not prime") == "not prime"

def test_x_or_y_large_numbers():
    """Test with larger prime and non-prime numbers."""
    # 104729 is the 10,000th prime number
    assert x_or_y(104729, "X", "Y") == "X"
    # 104730 is clearly even and not prime
    assert x_or_y(104730, "X", "Y") == "Y"