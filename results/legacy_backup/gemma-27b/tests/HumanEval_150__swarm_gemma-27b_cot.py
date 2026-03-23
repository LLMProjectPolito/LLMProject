import pytest

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

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@pytest.mark.parametrize("n, x, y, expected", [
    (2, 10, 20, 10),
    (3, 5, 15, 5),
    (4, 1, 2, 2),
    (5, 100, 200, 100),
    (6, 300, 400, 400),
    (7, 700, 800, 700),
    (8, 900, 1000, 1000),
    (9, 1100, 1200, 1200),
    (10, 1300, 1400, 1400),
    (11, 1500, 1600, 1500),
    (12, 1700, 1800, 1800),
    (13, 1900, 2000, 1900),
    (14, 2100, 2200, 2200),
    (15, 2300, 2400, 2400),
    (16, 2500, 2600, 2600),
    (17, 2700, 2800, 2700),
    (18, 2900, 3000, 3000),
    (19, 3100, 3200, 3100),
    (20, 3300, 3400, 3400),
    (1, 1, 2, 2),  # Edge case: n = 1 (not prime)
    (0, 3, 4, 4),  # Edge case: n = 0 (not prime)
    (-1, 5, 6, 6), # Edge case: n = -1 (not prime)
    (2**31 - 1, 7, 8, 7), # Large prime
    (2**31, 9, 10, 10) # Large non-prime
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_edge_case_one():
    assert x_or_y(1, 10, 20) == 20