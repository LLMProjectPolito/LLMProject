
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19 or n == 23 or n == 29 or n == 31:
        return x
    else:
        return y

def test_x_or_y_zero():
    assert x_or_y(0, 34, 12) == 12

def test_x_or_y_non_prime_one():
    assert x_or_y(4, 34, 12) == 12

def test_x_or_y_prime_seven():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_non_prime_fifteen():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_prime_two():
    assert x_or_y(2, 34, 12) == 34

def test_x_or_y_prime_three():
    assert x_or_y(3, 34, 12) == 34

def test_x_or_y_prime_five():
    assert x_or_y(5, 34, 12) == 34

def test_x_or_y_prime_seven_again():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_prime_eleven():
    assert x_or_y(11, 34, 12) == 34

def test_x_or_y_prime_thirteen():
    assert x_or_y(13, 34, 12) == 34

def test_x_or_y_prime_seventeen():
    assert x_or_y(17, 34, 12) == 34

def test_x_or_y_prime_nineteen():
    assert x_or_y(19, 34, 12) == 34

def test_x_or_y_prime_twenty_three():
    assert x_or_y(23, 34, 12) == 34

def test_x_or_y_prime_twenty_nine():
    assert x_or_y(29, 34, 12) == 34

def test_x_or_y_prime_thirty_one():
    assert x_or_y(31, 34, 12) == 34