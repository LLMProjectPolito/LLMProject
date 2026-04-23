
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

```python
import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return None
    if n == x or n == y:
        return x
    else:
        return y

def test_x_or_y():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 2, 3) == 2
    assert x_or_y(1, 2, 4) == 2
    assert x_or_y(1, 2, 1) == 2
    assert x_or_y(1, 2, 1) == 1
    assert x_or_y(1, 1, 1) == 1
    assert x_or_y(1, 1, 2) == 1
    assert x_or_y(1, 1, 3) == 1
    assert x_or_y(1, 1, 4) == 1
    assert x_or_y(1, 1, 5) == 1
    assert x_or_y(1, 1, 6) == 1
    assert x_or_y(1, 1, 7) == 1
    assert x_or_y(1, 1, 8) == 1
    assert x_or_y(1, 1, 9) == 1
    assert x_or_y(1, 1, 10) == 1
    assert x_or_y(1, 1, 11) == 1
    assert x_or_y(1, 1, 12) == 1
    assert x_or_y(1, 1, 13) == 1
    assert x_or_y(1, 1, 14) == 1
    assert x_or_y(1, 1, 15) == 1
    assert x_or_y(1, 1, 16) == 1
    assert x_or_y(1, 1, 17) == 1
    assert x_or_y(1, 1, 18) == 1
    assert x_or_y(1, 1, 19) == 1
    assert x_or_y(1, 1, 20) == 1
    assert x_or_y(1, 1, 21) == 1
    assert x_or_y(1, 1, 22) == 1
    assert x_or_y(1, 1, 23) == 1
    assert x_or_y(1, 1, 24) == 1
    assert x_or_y(1, 1, 25) == 1
    assert x_or_y(1, 1, 26) == 1
    assert x_or_y(1, 1, 27) == 1
    assert x_or_y(1, 1, 28) == 1
    assert x_or_y(1, 1, 29) == 1
    assert x_or_y(1, 1, 30) == 1
    assert x_or_y(1, 1, 31) == 1
    assert x_or_y(1, 1, 32) == 1
    assert x_or_y(1, 1, 33) == 1
    assert x_or_y(1, 1, 34) == 1
    assert x_or_y(1, 1, 35) == 1
    assert x_or_y(1, 1, 36) == 1
    assert x_or_y(1, 1, 37) == 1
    assert x_or_y(1, 1, 38) == 1
    assert x_or_y(1, 1, 39) == 1
    assert x_or_y(1, 1, 40) == 1
    assert x_or_y(1, 1, 41) == 1
    assert x_or_y(1, 1, 42) == 1
    assert x_or_y(1, 1, 43) == 1
    assert x_or_y(1, 1, 44) == 1
    assert x_or_y(1, 1, 45) == 1
    assert x_or_y(1, 1, 46) == 1
    assert x_or_y(1, 1, 47) == 1
    assert x_or_y(1, 1, 48) == 1
    assert x_or_y(1, 1, 49) == 1
    assert x_or_y(1, 1, 50) == 1
    assert x_or_y(1, 1, 51) == 1
    assert x_or_y(1, 1, 52) == 1
    assert x_or_y(1, 1, 53) == 1
    assert x_or_y(1, 1, 54) == 1
    assert x_or_y(1, 1, 55) == 1
    assert x_or_y(1, 1, 56) == 1
    assert x_or_y(1, 1, 57) == 1
    assert x_or_y(1, 1, 58) == 1
    assert x_or_y(1, 1, 59) == 1
    assert x_or_y(1, 1, 60) == 1
    assert x_or_y(1, 1, 61) == 1
    assert x_or_y(1, 1, 62) == 1
    assert x_or_y(1, 1, 63) == 1
    assert x_or_y(1, 1, 64) == 1
    assert x_or_y(1, 1, 65) == 1
    assert x_or_y(1, 1, 66) == 1
    assert x_or_y(1, 1, 67) == 1
    assert x_or_y(1, 1, 68) == 1
    assert x_or_y(1, 1, 69) == 1
    assert x_or_y(1, 1, 70) == 1
    assert x_or_y(1, 1, 71) == 1
    assert x_or_y(1, 1, 72) == 1
    assert x_or_y(1, 1, 73) == 1
    assert x_or_y(1, 1, 74) == 1
    assert x_or_y(1, 1, 75) == 1
    assert x_or_y(1, 1, 76) == 1
    assert x_or_y(1, 1, 77) == 1
    assert x_or_y(1, 1, 78) == 1
    assert x_or_y(1, 1, 79) == 1
    assert x_or_y(1, 1, 80) == 1
    assert x_or_y(1, 1, 81) == 1
    assert x_or_y(1, 1, 82) == 1
    assert x_or_y(1, 1, 83) == 1
    assert x_or_