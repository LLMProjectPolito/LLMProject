
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
import math

def even_odd_count(n):
    """Counts the number of even and odd digits in a number."""
    even_count = 0
    odd_count = 0
    for digit in str(abs(n)):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)