import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

class TestXorY:
    def test_prime_number(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(5, 5, 10) == 5
        assert x_or_y(11, "a", "b") == "a"

    def test_non_prime_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 20) == 20
        assert x_or_y(9, "x", "y") == "y"

    def test_edge_cases(self):
        assert x_or_y(1, 5, 10) == 10  # 1 is not prime
        assert x_or_y(0, 1, 2) == 2  # 0 is not prime
        assert x_or_y(-5, 1, 2) == 2 # Negative numbers are not prime
        assert x_or_y(23, 1000, 1) == 1000

    def test_type_handling(self):
        assert x_or_y(7, 3.14, 2.71) == 3.14
        assert x_or_y(10, True, False) == False
        assert x_or_y(11, [1,2], (3,4)) == [1,2]
        assert x_or_y(12, {1: 'a'}, {2: 'b'}) == {2: 'b'}