
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
from your_module import x_or_y  # Replace your_module

class TestXorY:
    def test_prime_returns_y(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 10, 20) == 10
        assert x_or_y(11, 5, 15) == 5
        assert x_or_y(13, 100, 200) == 100

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 25, 30) == 30
        assert x_or_y(9, 10, 11) == 11

    def test_edge_cases(self):
        assert x_or_y(1, 5, 10) == 10  # 1 is not prime
        assert x_or_y(0, 15, 20) == 20  # 0 is not prime
        assert x_or_y(-5, 2, 4) == 4  # Negative numbers are not prime
        assert x_or_y(2, 0, 0) == 0  # Prime number, x = 0
        assert x_or_y(3, 0, 0) == 0  # Prime number, x = 0
        assert x_or_y(4, 0, 0) == 0  # Non-prime number, y = 0

    def test_type_handling(self):
        assert x_or_y(7, "hello", 12) == "hello"
        assert x_or_y(7, 34, "world") == "world"
        assert x_or_y(7.0, 34, 12) == 34  # float input for n, should still work
        assert x_or_y(7, 34.5, 12) == 12  # float input for x or y
        assert x_or_y(7, 34, 12.5) == 12.5
        with pytest.raises(TypeError):
            x_or_y("7", 34, 12)
        with pytest.raises(TypeError):
            x_or_y(7, "34", 12)
        with pytest.raises(TypeError):
            x_or_y(7, 34, "12")

    def test_large_numbers(self):
        assert x_or_y(997, 1000, 2000) == 1000
        assert x_or_y(1000, 1000, 2000) == 2000
        assert x_or_y(99991, 5000, 10000) == 5000
        assert x_or_y(100000, 1, 2) == 2