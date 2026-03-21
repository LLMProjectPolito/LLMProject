import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

class TestXorY:
    def test_prime_two(self):
        assert x_or_y(2, 34, 12) == 34

    def test_negative_n(self):
        assert x_or_y(-7, 34, 12) == 12

    def test_large_prime(self):
        assert x_or_y(97, 34, 12) == 34

    def test_large_non_prime(self):
        assert x_or_y(100, 34, 12) == 12

    def test_float_n(self):
        assert x_or_y(7.0, 34, 12) == 34
        assert x_or_y(15.0, 34, 12) == 12

    def test_prime_small(self):
        assert x_or_y(2, 34, 12) == 34
        assert x_or_y(3, 34, 12) == 34
        assert x_or_y(5, 34, 12) == 34
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(11, 34, 12) == 34

    def test_prime_large(self):
        assert x_or_y(13, 34, 12) == 34
        assert x_or_y(17, 34, 12) == 34
        assert x_or_y(19, 34, 12) == 34
        assert x_or_y(23, 34, 12) == 34

    def test_non_prime_small(self):
        assert x_or_y(1, 34, 12) == 12
        assert x_or_y(4, 34, 12) == 12
        assert x_or_y(6, 34, 12) == 12
        assert x_or_y(8, 34, 12) == 12
        assert x_or_y(9, 34, 12) == 12
        assert x_or_y(10, 34, 12) == 12
        assert x_or_y(12, 34, 12) == 12
        assert x_or_y(14, 34, 12) == 12
        assert x_or_y(15, 34, 12) == 12

    def test_non_prime_large(self):
        assert x_or_y(16, 34, 12) == 12
        assert x_or_y(18, 34, 12) == 12
        assert x_or_y(20, 34, 12) == 12
        assert x_or_y(21, 34, 12) == 12
        assert x_or_y(22, 34, 12) == 12
        assert x_or_y(24, 34, 12) == 12

    def test_edge_zero(self):
        assert x_or_y(0, 34, 12) == 12

    def test_negative_xy(self):
        assert x_or_y(7, -34, -12) == -34
        assert x_or_y(15, -34, -12) == -12

    def test_zero_xy(self):
        assert x_or_y(7, 0, 0) == 0
        assert x_or_y(15, 0, 0) == 0

    def test_float_xy(self):
        assert x_or_y(7, 34.5, 12.2) == 34.5
        assert x_or_y(15, 34.5, 12.2) == 12.2