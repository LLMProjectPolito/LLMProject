
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
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return i
    return x

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(11, 11, 11) == 11
    assert x_or_y(13, 13, 13) == 13
    assert x_or_y(17, 17, 17) == 17
    assert x_or_y(2, 2, 2) == 2
    assert x_or_y(3, 3, 3) == 3
    assert x_or_y(4, 4, 4) == 4
    assert x_or_y(5, 5, 5) == 5
    assert x_or_y(6, 6, 6) == 6
    assert x_or_y(9, 9, 9) == 9
    assert x_or_y(10, 10, 10) == 10
    assert x_or_y(11, 11, 11) == 11
    assert x_or_y(12, 12, 12) == 12
    assert x_or_y(13, 13, 13) == 13
    assert x_or_y(14, 14, 14) == 14
    assert x_or_y(15, 15, 15) == 15
    assert x_or_y(16, 16, 16) == 16
    assert x_or_y(17, 17, 17) == 17
    assert x_or_y(18, 18, 18) == 18
    assert x_or_y(19, 19, 19) == 19
    assert x_or_y(20, 20, 20) == 20
    assert x_or_y(21, 21, 21) == 21
    assert x_or_y(22, 22, 22) == 22
    assert x_or_y(23, 23, 23) == 23
    assert x_or_y(24, 24, 24) == 24
    assert x_or_y(25, 25, 25) == 25
    assert x_or_y(26, 26, 26) == 26
    assert x_or_y(27, 27, 27) == 27
    assert x_or_y(28, 28, 28) == 28
    assert x_or_y(29, 29, 29) == 29
    assert x_or_y(30, 30, 30) == 30
    assert x_or_y(31, 31, 31) == 31
    assert x_or_y(32, 32, 32) == 32
    assert x_or_y(33, 33, 33) == 33
    assert x_or_y(34, 34, 34) == 34
    assert x_or_y(35, 35, 35) == 35
    assert x_or_y(36, 36, 36) == 36
    assert x_or_y(37, 37, 37) == 37
    assert x_or_y(38, 38, 38) == 38
    assert x_or_y(39, 39, 39) == 39
    assert x_or_y(40, 40, 40) == 40
    assert x_or_y(41, 41, 41) == 41
    assert x_or_y(42, 42, 42) == 42
    assert x_or_y(43, 43, 43) == 43
    assert x_or_y(44, 44, 44) == 44
    assert x_or_y(45, 45, 45) == 45
    assert x_or_y(46, 46, 46) == 46
    assert x_or_y(47, 47, 47) == 47
    assert x_or_y(48, 48, 48) == 48
    assert x_or_y(49, 49, 49) == 49
    assert x_or_y(50, 50, 50) == 50
    assert x_or_y(51, 51, 51) == 51
    assert x_or_y(52, 52, 52) == 52
    assert x_or_y(53, 53, 53) == 53
    assert x_or_y(54, 54, 54) == 54
    assert x_or_y(55, 55, 55) == 55
    assert x_or_y(56, 56, 56) == 56
    assert x_or_y(57, 57, 57) == 57
    assert x_or_y(58, 58, 58) == 58
    assert x_or_y(59, 59, 59) == 59
    assert x_or_y(60, 60, 60) == 60
    assert x_or_y(61, 61, 61) == 61
    assert x_or_y(62, 62, 62) == 62
    assert x_or_y(63, 63, 63) == 63
    assert x_or_y(64, 64, 64) == 64
    assert x_or_y(65, 65, 65) == 65
    assert x_or_y(66, 66, 66) == 66
    assert x_or_y(67, 67, 67) == 67
    assert x_or_y(68, 68, 68) == 68
    assert x_or_y(69, 69, 69) == 69
    assert x_or_y(70, 70, 70) == 70
    assert x_or_y(71, 71, 71) == 71
    assert x_or_y(72, 72, 72) == 72
    assert x_or_y(73, 73, 73) == 73
    assert x_or_y(74, 74, 74) == 74
    assert x_or_y(75, 75, 75) == 75
    assert x_or_y(76, 76, 76) == 76
    assert x_or_y(77, 77, 77) == 77
    assert x_or_y(78, 78, 78) == 78
    assert x