
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("x, prime_val, non_prime_val, expected", [
    (1, "is_prime", "is_not_prime", "is_not_prime"),
    (1, "prime_val", "non_prime_val", "non_prime_val"),
    (1, 100, 200, 200),
])
def test_x_or_y_one_is_not_prime(x, prime_val, non_prime_val, expected):
    """Test that n=1 is correctly identified as non-prime, returning the non-prime value."""
    assert x_or_y(x, prime_val, non_prime_val) == expected