
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

    x and y can be of any type.

    Examples:
    x_or_y(7, 34, 12) == 34
    x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
])
def test_x_or_y_docstring_examples(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_prime():
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 0) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, -1, -2) == -1
    assert x_or_y(17, 10.5, 20.5) == 10.5
    assert x_or_y(19, "a", "b") == "a"
    assert x_or_y(97, 1, 2) == 1
    assert x_or_y(7919, 1, 2) == 1  # Larger prime

def test_x_or_y_not_prime():
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 5) == 5
    assert x_or_y(8, 20, 10) == 10
    assert x_or_y(9, 3, 1) == 1
    assert x_or_y(10, -1, -2) == -2
    assert x_or_y(12, 10.5, 20.5) == 20.5
    assert x_or_y(14, "a", "b") == "b"

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 10, 20) == 20
    assert x_or_y(-1, 10, 20) == 20
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(1, 0, 0) == 0
    assert x_or_y(2, 1, 0) == 1
    assert x_or_y(1, 1, 0) == 0

def test_x_or_y_mixed_types():
    assert x_or_y(7, "hello", 123) == "hello"
    assert x_or_y(15, 42, "world") == "world"
    assert x_or_y(2, 1.5, "test") == 1.5
    assert x_or_y(4, "test", 2.7) == 2.7

def test_x_or_y_negative_non_prime():
    assert x_or_y(-2, 1, 2) == 2
    assert x_or_y(-3, 3, 4) == 4
    assert x_or_y(-4, 5, 6) == 6
    assert x_or_y(-6, 7, 8) == 8

def test_x_or_y_square_root_optimization():
    # Test a composite number where the square root optimization should be effective
    assert x_or_y(49, 1, 2) == 2  # 49 = 7 * 7
    assert x_or_y(51, 1, 2) == 2  # 51 = 3 * 17