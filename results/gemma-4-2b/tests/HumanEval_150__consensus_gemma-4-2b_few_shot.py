
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
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

def test_x_or_y_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 5, 2) == 5
    assert x_or_y(13, 100, 50) == 100
    assert x_or_y(2, 1, 0) == 1
    assert x_or_y(3, 10, 20) == 10

def test_x_or_y_not_prime_number():
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(1, 1, 0) == 0
    assert x_or_y(6, 10, 20) == 20

def test_x_or_y_edge_cases():
    assert x_or_y(2, 1, 0) == 1
    assert x_or_y(3, 1, 0) == 1
    assert x_or_y(5, 1, 0) == 1
    assert x_or_y(7, 1, 0) == 1
    assert x_or_y(11, 1, 0) == 1
    assert x_or_y(13, 1, 0) == 1
    assert x_or_y(17, 1, 0) == 1
    assert x_or_y(19, 1, 0) == 1
    assert x_or_y(23, 1, 0) == 1
    assert x_or_y(29, 1, 0) == 1
    assert x_or_y(31, 1, 0) == 1
    assert x_or_y(37, 1, 0) == 1
    assert x_or_y(41, 1, 0) == 1
    assert x_or_y(43, 1, 0) == 1
    assert x_or_y(47, 1, 0) == 1
    assert x_or_y(53, 1, 0) == 1
    assert x_or_y(59, 1, 0) == 1
    assert x_or_y(61, 1, 0) == 1
    assert x_or_y(67, 1, 0) == 1
    assert x_or_y(71, 1, 0) == 1
    assert x_or_y(73, 1, 0) == 1
    assert x_or_y(79, 1, 0) == 1
    assert x_or_y(83, 1, 0) == 1
    assert x_or_y(89, 1, 0) == 1
    assert x_or_y(97, 1, 0) == 1
    assert x_or_y(101, 1, 0) == 1
    assert x_or_y(103, 1, 0) == 1
    assert x_or_y(107, 1, 0) == 1
    assert x_or_y(109, 1, 0) == 1
    assert x_or_y(113, 1, 0) == 1
    assert x_or_y(127, 1, 0) == 1
    assert x_or_y(131, 1, 0) == 1
    assert x_or_y(137, 1, 0) == 1
    assert x_or_y(139, 1, 0) == 1
    assert x_or_y(149, 1, 0) == 1
    assert x_or_y(151, 1, 0) == 1
    assert x_or_y(157, 1, 0) == 1
    assert x_or_y(163, 1, 0) == 1
    assert x_or_y(167, 1, 0) == 1
    assert x_or_y(173, 1, 0) == 1
    assert x_or_y(179, 1, 0) == 1
    assert x_or_y(181, 1, 0) == 1
    assert x_or_y(191, 1, 0) == 1
    assert x_or_y(193, 1, 0) == 1
    assert x_or_y(197, 1, 0) == 1
    assert x_or_y(199, 1, 0) == 1
    assert x_or_y(211, 1, 0) == 1
    assert x_or_y(223, 1, 0) == 1
    assert x_or_y(227, 1, 0) == 1
    assert x_or_y(229, 1, 0) == 1
    assert x_or_y(233, 1, 0) == 1
    assert x_or_y(239, 1, 0) == 1
    assert x_or_y(241, 1, 0) == 1
    assert x_or_y(251, 1, 0) == 1
    assert x_or_y(257, 1, 0) == 1
    assert x_or_y(263, 1, 0) == 1
    assert x_or_y(269, 1, 0) == 1
    assert x_or_y(271, 1, 0) == 1
    assert x_or_y(277, 1, 0) == 1
    assert x_or_y(281, 1, 0) == 1
    assert x_or_y(283, 1, 0) == 1
    assert x_or_y(293, 1, 0) == 1
    assert x_or_y(307, 1, 0) == 1
    assert x_or_y(311, 1, 0) == 1
    assert x_or_y(313, 1, 0) == 1
    assert x_or_y(317, 1, 0) == 1
    assert x_or_y(331, 1, 0) == 1
    assert x_or_y(337, 1, 0) == 1
    assert x_or_y(347, 1, 0) == 1
    assert x_or_y(349, 1, 0) == 1
    assert x_or_y(353, 1, 0) == 1
    assert x_or_y(359, 1, 0) == 1
    assert x_or_y(367, 1, 0) == 1
    assert x_or_y(373, 1, 0) == 1
    assert x_or_y(379, 1, 0) == 1