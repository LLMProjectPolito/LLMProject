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

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 5, 10) == 5
    assert x_or_y(3, 100, 200) == 100
    assert x_or_y(5, 1, 2) == 1
    assert x_or_y(11, 7, 8) == 7
    assert x_or_y(13, 15, 20) == 15
    assert x_or_y(17, 25, 30) == 25
    assert x_or_y(19, 35, 40) == 35
    assert x_or_y(23, 45, 50) == 45
    assert x_or_y(29, 60, 65) == 60

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(6, 30, 40) == 40
    assert x_or_y(8, 50, 60) == 60
    assert x_or_y(9, 70, 80) == 80
    assert x_or_y(10, 90, 100) == 100
    assert x_or_y(12, 110, 120) == 120
    assert x_or_y(14, 130, 140) == 140
    assert x_or_y(20, 150, 160) == 160
    assert x_or_y(21, 170, 180) == 180
    assert x_or_y(22, 190, 200) == 200
    assert x_or_y(24, 210, 220) == 220
    assert x_or_y(25, 230, 240) == 240

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(-5, 5, 10) == 10
    assert x_or_y(-2, 1, 2) == 2
    assert x_or_y(2, -1, 0) == -1
    assert x_or_y(3, 0, -1) == 0

def test_x_or_y_type_handling():
    assert x_or_y(7, 34.5, 12) == 34.5
    assert x_or_y(7, "hello", "world") == "hello"
    assert x_or_y(7, [1, 2], [3, 4]) == [1, 2]
    assert x_or_y(7, {"a": 1}, {"b": 2}) == {"a": 1}
    with pytest.raises(TypeError):
        x_or_y(7, 34, 12.5)
    with pytest.raises(TypeError):
        x_or_y(7, "34", 12)
    with pytest.raises(TypeError):
        x_or_y("7", 34, 12)