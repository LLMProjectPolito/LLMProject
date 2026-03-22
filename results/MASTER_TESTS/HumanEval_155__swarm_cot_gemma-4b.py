import pytest
import math

def even_odd_count(n):
    """Counts the number of even and odd numbers in a given integer."""
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_zero_input():
    assert even_odd_count(0) == (1, 0)