
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

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

def test_prime_n_equal_x():
    assert x_or_y(7, 7, 12) == 7

def test_prime_n_not_equal_x():
    assert x_or_y(7, 34, 7) == 34

def test_non_prime_n_equal_x():
    assert x_or_y(4, 4, 12) == 4

def test_non_prime_n_not_equal_x():
    assert x_or_y(4, 8, 5) == 5

def test_edge_case_2():
    assert x_or_y(2, 2, 12) == 2

def test_edge_case_3():
    assert x_or_y(3, 3, 12) == 3

def test_edge_case_5():
    assert x_or_y(5, 5, 12) == 5

def test_large_prime():
    assert x_or_y(1000000007, 1000000007, 12) == 1000000007

def test_x_equal_y():
    assert x_or_y(7, 7, 7) == 7

def test_x_not_equal_y():
    assert x_or_y(7, 34, 7) == 34

def test_large_x_y():
    assert x_or_y(7, 1000000, 2000000) == 1000000

def test_invalid_n_less_than_2():
    assert x_or_y(1, 34, 12) == 12

def test_negative_x():
    assert x_or_y(-7, -7, 12) == 12

def test_negative_y():
    assert x_or_y(7, -7, 12) == -7

def test_zero_x():
    assert x_or_y(7, 0, 12) == 12

def test_zero_y():
    assert x_or_y(7, 7, 0) == 0

def test_invalid_type_n():
    with pytest.raises(TypeError):
        x_or_y("7", 34, 12)

def test_prime_n_different_x_y():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 5, 2) == 5
    assert x_or_y(13, 10, 1) == 10

def test_non_prime_n_different_x_y():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(9, 10, 1) == 1
    assert x_or_y(10, 1, 2) == 2

def test_prime_n_same_x_y():
    assert x_or_y(7, 34, 34) == 34
    assert x_or_y(11, 5, 5) == 5
    assert x_or_y(13, 10, 10) == 10

def test_non_prime_n_same_x_y():
    assert x_or_y(15, 8, 8) == 8
    assert x_or_y(9, 10, 10) == 10
    assert x_or_y(10, 1, 1) == 1

def test_small_prime_numbers():
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 12, 5) == 12
    assert x_or_y(5, 10, 1) == 10
    assert x_or_y(7, 5, 2) == 5

def test_small_non_prime_numbers():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(4, 12, 5) == 5
    assert x_or_y(6, 10, 1) == 1
    assert x_or_y(8, 1, 2) == 2
    assert x_or_y(9, 1, 1) == 1

def test_large_prime_numbers():
    assert x_or_y(1009, 34, 12) == 34
    assert x_or_y(1013, 5, 2) == 5
    assert x_or_y(10007, 10, 1) == 1

def test_zero_n():
    assert x_or_y(0, 34, 12) == 12