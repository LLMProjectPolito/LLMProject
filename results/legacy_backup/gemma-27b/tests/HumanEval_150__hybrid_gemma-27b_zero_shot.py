import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestXOrY:
    def test_prime_number(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 10, 20) == 10
        assert x_or_y(3, 5, 8) == 5
        assert x_or_y(5, 1, 2) == 1
        assert x_or_y(11, 100, 200) == 100
        assert x_or_y(13, -5, 10) == -5
        assert x_or_y(17, 0, 1) == 0
        assert x_or_y(19, "a", "b") == "a"
        assert x_or_y(23, 3.14, 2.71) == 3.14
        assert x_or_y(29, True, False) == True

    def test_composite_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 5) == 5
        assert x_or_y(8, 20, 10) == 10
        assert x_or_y(9, 30, 15) == 15
        assert x_or_y(10, 100, 50) == 50
        assert x_or_y(12, -10, 5) == 5
        assert x_or_y(14, "hello", "world") == "world"

    def test_edge_cases(self):
        assert x_or_y(0, 1, 2) == 2
        assert x_or_y(1, 1, 2) == 2
        assert x_or_y(2, 1, 2) == 1
        assert x_or_y(-1, 1, 2) == 2
        assert x_or_y(-7, 1, 2) == 2
        assert x_or_y(1, 1, 2) == 2  # 1 is not prime
        assert x_or_y(0, 1, 2) == 2  # 0 is not prime
        assert x_or_y(-1, 1, 2) == 2 # Negative number is not prime
        assert x_or_y(-7, 1, 2) == 2 # Negative prime is not prime
        assert x_or_y(2, 2, 2) == 2
        assert x_or_y(4, 4, 4) == 4

    def test_large_numbers(self):
        assert x_or_y(101, 1000, 2000) == 1000  # Prime
        assert x_or_y(100, 1000, 2000) == 2000  # Composite
        assert x_or_y(997, 5, 10) == 5 #Prime
        assert x_or_y(999, 5, 10) == 10 #Composite
        assert x_or_y(101, 1000, 2000) == 1000 # Prime
        assert x_or_y(100, 1000, 2000) == 2000 # Not prime
        assert x_or_y(997, 1, 0) == 1 # Large prime
        assert x_or_y(999, 1, 0) == 0 # Large non-prime

    def test_x_and_y_are_same(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(15, 5, 5) == 5

    def test_data_types(self):
        assert x_or_y(7, 3.14, 2.71) == 3.14
        assert x_or_y(15, 3.14, 2.71) == 2.71
        assert x_or_y(7, True, False) == True
        assert x_or_y(15, True, False) == False
        assert x_or_y(7, "hello", "world") == "hello"
        assert x_or_y(10, 1.5, 2.5) == 2.5
        assert x_or_y(5, True, False) == True
        assert x_or_y(4, [1, 2], [3, 4]) == [3, 4]
        assert x_or_y(2, (1, 2), (3, 4)) == (1, 2)