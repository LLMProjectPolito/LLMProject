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

def test_prime_returns_x():
    assert x_or_y(7, 34, 12) == 34

def test_non_prime_returns_y():
    assert x_or_y(15, 8, 5) == 5

def test_n_is_1_returns_y():
    assert x_or_y(1, 10, 20) == 20

def test_n_is_2_returns_x():
    assert x_or_y(2, "hello", "world") == "hello"

def test_x_and_y_are_strings():
    assert x_or_y(5, "apple", "banana") == "apple"
    assert x_or_y(4, "apple", "banana") == "banana"

def test_x_is_int_y_is_string():
    assert x_or_y(7, 10, "banana") == 10
    assert x_or_y(10, 10, "banana") == "banana"

def test_x_is_string_y_is_int():
    assert x_or_y(7, "apple", 10) == "apple"
    assert x_or_y(10, "apple", 10) == 10

def test_x_is_float_y_is_int():
    assert x_or_y(3, 3.14, 5) == 3.14
    assert x_or_y(4, 3.14, 5) == 5

def test_x_is_int_y_is_float():
    assert x_or_y(7, 10, 5.5) == 10
    assert x_or_y(8, 10, 5.5) == 5.5

def test_negative_n_returns_y():
    assert x_or_y(-5, 1, 2) == 2

def test_large_prime():
    assert x_or_y(101, "prime", "not prime") == "prime"

def test_large_non_prime():
    assert x_or_y(100, "prime", "not prime") == "not prime"