
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
    x_or_y(7, 34, 12) == 34
    x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

class TestXOrY:
    def test_prime_number(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(13, 8, 5) == 8
        assert x_or_y(2, 34, 12) == 34
        assert x_or_y(3, 34, 12) == 34
        assert x_or_y(5, 34, 12) == 34
        assert x_or_y(17, 8, 5) == 8
        assert x_or_y(23, 8, 5) == 8

    def test_non_prime_number(self):
        assert x_or_y(4, 34, 12) == 12
        assert x_or_y(6, 34, 12) == 12
        assert x_or_y(8, 34, 12) == 12
        assert x_or_y(9, 34, 12) == 12
        assert x_or_y(10, 34, 12) == 12
        assert x_or_y(12, 34, 12) == 12
        assert x_or_y(14, 34, 12) == 12
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(20, 8, 5) == 5
        assert x_or_y(21, 8, 5) == 5
        assert x_or_y(22, 8, 5) == 5
        assert x_or_y(24, 8, 5) == 5
        assert x_or_y(25, 8, 5) == 5
        assert x_or_y(26, 8, 5) == 5
        assert x_or_y(27, 8, 5) == 5
        assert x_or_y(28, 8, 5) == 5
        assert x_or_y(30, 8, 5) == 5
        assert x_or_y(32, 8, 5) == 5
        assert x_or_y(33, 8, 5) == 5
        assert x_or_y(34, 8, 5) == 5
        assert x_or_y(35, 8, 5) == 5
        assert x_or_y(36, 8, 5) == 5
        assert x_or_y(40, 8, 5) == 5
        assert x_or_y(42, 8, 5) == 5
        assert x_or_y(44, 8, 5) == 5
        assert x_or_y(45, 8, 5) == 5
        assert x_or_y(46, 8, 5) == 5
        assert x_or_y(48, 8, 5) == 5
        assert x_or_y(49, 8, 5) == 5
        assert x_or_y(50, 8, 5) == 5
        assert x_or_y(51, 8, 5) == 5
        assert x_or_y(52, 8, 5) == 5
        assert x_or_y(54, 8, 5) == 5
        assert x_or_y(55, 8, 5) == 5
        assert x_or_y(56, 8, 5) == 5
        assert x_or_y(57, 8, 5) == 5
        assert x_or_y(58, 8, 5) == 5
        assert x_or_y(60, 8, 5) == 5
        assert x_or_y(62, 8, 5) == 5
        assert x_or_y(63, 8, 5) == 5
        assert x_or_y(64, 8, 5) == 5
        assert x_or_y(65, 8, 5) == 5
        assert x_or_y(66, 8, 5) == 5
        assert x_or_y(68, 8, 5) == 5
        assert x_or_y(69, 8, 5) == 5
        assert x_or_y(70, 8, 5) == 5
        assert x_or_y(72, 8, 5) == 5
        assert x_or_y(74, 8, 5) == 5
        assert x_or_y(75, 8, 5) == 5
        assert x_or_y(76, 8, 5) == 5
        assert x_or_y(77, 8, 5) == 5
        assert x_or_y(78, 8, 5) == 5
        assert x_or_y(80, 8, 5) == 5
        assert x_or_y(81, 8, 5) == 5
        assert x_or_y(82, 8, 5) == 5
        assert x_or_y(84, 8, 5) == 5
        assert x_or_y(85, 8, 5) == 5
        assert x_or_y(86, 8, 5) == 5
        assert x_or_y(87, 8, 5) == 5
        assert x_or_y(88, 8, 5) == 5
        assert x_or_y(90, 8, 5) == 5
        assert x_or_y(91, 8, 5) == 5
        assert x_or_y(92, 8, 5) == 5
        assert x_or_y(93, 8, 5) == 5
        assert x_or_y(94, 8, 5) == 5
        assert x_or_y(95, 8, 5) == 5
        assert x_or_y(96, 8, 5) == 5
        assert x_or_y(98, 8, 5) == 5
        assert x_or_y(99, 8, 5) == 5
        assert x_or_y(100, 8, 5) == 5
        assert x_or_y(102, 8, 5) == 5
        assert x_or_y(104, 8, 5) == 5
        assert x_or_y(105, 8, 5) == 5
        assert x_or_y(106, 8, 5) == 5
        assert x_or_y(108, 8, 5) == 5
        assert x_or_y(110, 8, 5) == 5
        assert x_or_y(111, 8, 5) == 5
        assert x_or_y(112, 8, 5) == 5
        assert x_or_y(114, 8, 5) == 5
        assert x_or_y(115, 8, 5