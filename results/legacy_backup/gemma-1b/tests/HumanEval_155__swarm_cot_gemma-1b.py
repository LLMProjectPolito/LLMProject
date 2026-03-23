import pytest
from math import abs

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    for digit in str(abs(num)):
        digit = int(digit)
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

def testfile():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(222) == (2, 2)
    assert even_odd_count(1357) == (1, 3)
    assert even_odd_count(12345) == (1, 2)
    assert even_odd_count(123456789) == (1, 2)
    assert even_odd_count(-2147483648) == (1, 1)
    assert even_odd_count(-2147483649) == (1, 1)
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(1) == (1, 0)
    assert even_odd_count(2) == (0, 1)
    assert even_odd_count(3) == (1, 0)
    assert even_odd_count(4) == (0, 1)
    assert even_odd_count(5) == (1, 0)
    assert even_odd_count(6) == (0, 1)
    assert even_odd_count(7) == (1, 0)
    assert even_odd_count(8) == (0, 1)
    assert even_odd_count(9) == (1, 0)
    assert even_odd_count(10) == (1, 0)
    assert even_odd_count(11) == (0, 1)
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(13) == (1, 0)
    assert even_odd_count(14) == (0, 1)
    assert even_odd_count(15) == (1, 0)
    assert even_odd_count(16) == (0, 1)
    assert even_odd_count(17) == (1, 0)
    assert even_odd_count(18) == (0, 1)
    assert even_odd_count(19) == (1, 0)
    assert even_odd_count(20) == (0, 1)