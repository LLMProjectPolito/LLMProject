import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

def test_x_or_y_prime_n1():
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_prime_n2():
    assert x_or_y(2, 34, 12) == 34

def test_x_or_y_prime_n3():
    assert x_or_y(3, 34, 12) == 34

def test_x_or_y_prime_n7():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_prime_n11():
    assert x_or_y(11, 34, 12) == 34

def test_x_or_y_prime_n13():
    assert x_or_y(13, 34, 12) == 34

def test_x_or_y_prime_n17():
    assert x_or_y(17, 34, 12) == 34

def test_x_or_y_prime_n19():
    assert x_or_y(19, 34, 12) == 34

def test_x_or_y_prime_n23():
    assert x_or_y(23, 34, 12) == 34

def test_x_or_y_prime_n29():
    assert x_or_y(29, 34, 12) == 34

def test_x_or_y_prime_large():
    assert x_or_y(97, 34, 12) == 34

def test_x_or_y_non_prime_close_to_prime():
    assert x_or_y(28, 34, 12) == 12

def test_x_or_y_non_prime_n1():
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_non_prime_n2():
    assert x_or_y(2, 34, 12) == 12