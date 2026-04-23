
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
import math

def even_odd_count(n):
    """
    Counts the number of even and odd numbers in a given integer.

    Args:
        n: An integer.

    Returns:
        A tuple containing the count of even and odd numbers.
    """
    even_count = 0
    odd_count = 0
    if n == 0:
        return (0, 0)
    while n > 0:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n //= 2
    return (even_count, odd_count)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (2, 2)
    assert even_odd_count(13579) == (2, 2)
    assert even_odd_count(1) == (1, 1)
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(10) == (1, 1)
    assert even_odd_count(11) == (1, 1)
    assert even_odd_count(12) == (1, 2)
    assert even_odd_count(-1) == (1, 1)
    assert even_odd_count(1) == (1, 1)
    assert even_odd_count(12345) == (1, 2)
    assert even_odd_count(-12345) == (1, 2)