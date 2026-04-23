
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

def test_x_or_y_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 5, 20) == 5
    assert x_or_y(13, 10, 1) == 10
    assert x_or_y(17, 2, 7) == 2
    assert x_or_y(19, 1, 99) == 1

def test_x_or_y_not_prime_number():
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(25, 10, 1) == 1
    assert x_or_y(36, 2, 7) == 7
    assert x_or_y(49, 1, 99) == 99

def test_x_or_y_edge_case_n_is_1():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(1, 5, 20) == 20

def test_x_or_y_edge_case_n_is_2():
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(2, 5, 20) == 5

def test_x_or_y_edge_case_n_is_3():
    assert x_or_y(3, 34, 12) == 34
    assert x_or_y(3, 5, 20) == 5

def test_x_or_y_edge_case_n_is_5():
    assert x_or_y(5, 34, 12) == 34
    assert x_or_y(5, 5, 20) == 5

def test_x_or_y_edge_case_n_is_6():
    assert x_or_y(6, 34, 12) == 12
    assert x_or_y(6, 5, 20) == 20

def test_x_or_y_edge_case_n_is_8():
    assert x_or_y(8, 34, 12) == 12
    assert x_or_y(8, 5, 20) == 20

def test_x_or_y_edge_case_n_is_9():
    assert x_or_y(9, 34, 12) == 12
    assert x_or_y(9, 5, 20) == 20

def test_x_or_y_edge_case_n_is_10():
    assert x_or_y(10, 34, 12) == 12
    assert x_or_y(10, 5, 20) == 20

def test_x_or_y_edge_case_n_is_12():
    assert x_or_y(12, 34, 12) == 12
    assert x_or_y(12, 5, 20) == 20

def test_x_or_y_edge_case_n_is_14():
    assert x_or_y(14, 34, 12) == 12
    assert x_or_y(14, 5, 20) == 20

def test_x_or_y_edge_case_n_is_15():
    assert x_or_y(15, 34, 12) == 12
    assert x_or_y(15, 5, 20) == 20

def test_x_or_y_edge_case_n_is_16():
    assert x_or_y(16, 34, 12) == 12
    assert x_or_y(16, 5, 20) == 20

def test_x_or_y_edge_case_n_is_17():
    assert x_or_y(17, 34, 12) == 34
    assert x_or_y(17, 5, 20) == 5

def test_x_or_y_edge_case_n_is_18():
    assert x_or_y(18, 34, 12) == 12
    assert x_or_y(18, 5, 20) == 20

def test_x_or_y_edge_case_n_is_19():
    assert x_or_y(19, 34, 12) == 34
    assert x_or_y(19, 5, 20) == 5

def test_x_or_y_edge_case_n_is_20():
    assert x_or_y(20, 34, 12) == 12
    assert x_or_y(20, 5, 20) == 20