
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
from math import abs

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(222) == (2, 2)
    assert even_odd_count(1234) == (2, 2)
    assert even_odd_count(12345) == (2, 2)
    assert even_odd_count(123456) == (2, 2)
    assert even_odd_count(1234567) == (2, 2)
    assert even_odd_count(12345678) == (2, 2)
    assert even_odd_count(123456789) == (2, 2)
    assert even_odd_count(1234567890) == (2, 2)
    assert even_odd_count(12345678901) == (2, 2)
    assert even_odd_count(123456789012) == (2, 2)
    assert even_odd_count(1234567890123) == (2, 2)
    assert even_odd_count(12345678901234) == (2, 2)
    assert even_odd_count(123456789012345) == (2, 2)
    assert even_odd_count(1234567890123456) == (2, 2)
    assert even_odd_count(12345678901234567) == (2, 2)
    assert even_odd_count(123456789012345678) == (2, 2)
    assert even_odd_count(1234567890123456789) == (2, 2)
    assert even_odd_count(12345678901234567890) == (2, 2)
    print("All tests passed")