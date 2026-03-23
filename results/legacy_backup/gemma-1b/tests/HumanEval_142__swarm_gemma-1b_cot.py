import pytest
import math

def calculate_total(lst):
    """
    Calculates the total of squares of numbers divisible by 3 and 4.
    """
    total = 0
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 == 0:
            total += lst[i] ** 2
        elif i % 3 == 0:
            total += lst[i] ** 2
        elif i % 4 == 0:
            total += lst[i] ** 3
        else:
            total += lst[i]
    return total

def test_calculate_total():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert calculate_total(lst) == 36