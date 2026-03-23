import pytest

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (23, 10, 20, 10),
    (30, 40, 50, 50),
    (2, 3, 4, 3),
    (1, 5, 6, 6),
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_edge_case():
    assert x_or_y(1, 5, 6) == 6

def test_x_or_y_large_input():
    assert x_or_y(1000003, 10, 20) == 10

def test_x_or_y_negative_input():
    with pytest.raises(ValueError):
        x_or_y(-5, 10, 20)

def test_x_or_y_non_integer_input():
    with pytest.raises(TypeError):
        x_or_y(3.5, 10, 20)