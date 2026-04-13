
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
    def test_prime_returns_x(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 10, 20) == 10
        assert x_or_y(5, 100, 200) == 100
        assert x_or_y(11, 5, 10) == 5

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 20) == 20
        assert x_or_y(9, 5, 10) == 10

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20  # 1 is not prime
        assert x_or_y(0, 10, 20) == 20  # 0 is not prime
        assert x_or_y(-5, 10, 20) == 20 # Negative numbers are not prime
        assert x_or_y(2, 10, 10) == 10 # Prime, x and y are same
        assert x_or_y(4, 10, 10) == 10 # Non-prime, x and y are same

    def test_type_handling_strings(self):
        assert x_or_y(7, "hello", 12) == "hello"
        assert x_or_y(7, 34, "world") == "world"
        assert x_or_y(7.0, 34, 12) == 34 # float n, prime
        assert x_or_y(7.5, 34, 12) == 12 # float n, non-prime
        assert x_or_y(7, 34.5, 12) == 34.5
        assert x_or_y(7, 34, 12.5) == 12.5

    def test_type_handling_errors(self):
        with pytest.raises(TypeError):
            x_or_y("7", 34, 12)  # n is not an integer
        with pytest.raises(TypeError):
            x_or_y(7, "34", 12)  # x is not an integer
        with pytest.raises(TypeError):
            x_or_y(7, 34, "12")  # y is not an integer

    def test_large_numbers(self):
        assert x_or_y(1000000007, 1, 2) == 1 # Large prime
        assert x_or_y(1000000000, 1, 2) == 2 # Large non-prime
        assert x_or_y(997, 1000, 2000) == 1000
        assert x_or_y(999, 1000, 2000) == 2000

    def test_zero_values(self):
        assert x_or_y(7, 0, 12) == 0
        assert x_or_y(15, 8, 0) == 0
        assert x_or_y(0, 0, 0) == 0
        assert x_or_y(2, 0, 0) == 0 # Prime number, x = 0
        assert x_or_y(3, 0, 0) == 0 # Prime number, x = 0
        assert x_or_y(4, 0, 0) == 0 # Non-prime number, y = 0