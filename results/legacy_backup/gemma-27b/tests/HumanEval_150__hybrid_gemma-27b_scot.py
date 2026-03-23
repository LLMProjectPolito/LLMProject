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

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (2, 10, 20, 10),
    (3, 100, 200, 100),
    (5, 50, 60, 50),
    (11, 111, 222, 111),
    (13, 333, 444, 333),
    (4, 40, 50, 50),
    (6, 60, 70, 70),
    (8, 80, 90, 90),
    (9, 90, 100, 100),
    (10, 100, 110, 110),
    (16, 160, 170, 170),
    (18, 180, 190, 190),
    (20, 200, 210, 210),
    (21, 210, 220, 220),
    (22, 220, 230, 230),
    (24, 240, 250, 250),
    (25, 250, 260, 260),
    (0, 1, 2, 2),
    (1, 3, 4, 4),
    (-1, 5, 6, 6),
    (-2, 7, 8, 8),
    (17, 77, 88, 77),
    (19, 99, 100, 99),
    (23, 33, 44, 33)
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected