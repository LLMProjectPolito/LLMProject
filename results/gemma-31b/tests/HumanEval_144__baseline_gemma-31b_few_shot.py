
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

import pytest

def test_simplify_provided_examples():
    """Tests the examples provided in the docstring."""
    assert simplify("1/5", "5/1") is True
    assert simplify("1/6", "2/1") is False
    assert simplify("7/10", "10/2") is False

def test_simplify_whole_results():
    """Tests cases where the multiplication results in a whole number."""
    assert simplify("1/2", "2/1") is True    # 1/2 * 2/1 = 1
    assert simplify("3/4", "8/1") is True    # 3/4 * 8/1 = 6
    assert simplify("2/3", "9/2") is True    # 2/3 * 9/2 = 3
    assert simplify("10/3", "3/10") is True  # 10/3 * 3/10 = 1
    assert simplify("5/2", "4/5") is True    # 5/2 * 4/5 = 2

def test_simplify_fractional_results():
    """Tests cases where the multiplication results in a non-whole number."""
    assert simplify("1/3", "1/3") is False   # 1/9
    assert simplify("1/2", "1/2") is False   # 1/4
    assert simplify("2/5", "1/2") is False   # 1/5
    assert simplify("3/7", "7/2") is False   # 3/2 = 1.5
    assert simplify("1/10", "1/10") is False # 1/100

def test_simplify_integer_fractions():
    """Tests cases where fractions represent whole numbers (denominator is 1)."""
    assert simplify("1/1", "1/1") is True    # 1 * 1 = 1
    assert simplify("2/1", "3/1") is True    # 2 * 3 = 6
    assert simplify("1/1", "1/2") is False   # 1 * 0.5 = 0.5

def test_simplify_large_numbers():
    """Tests cases with larger numerators and denominators."""
    assert simplify("100/1", "1/100") is True    # 1
    assert simplify("1000/3", "3/1000") is True  # 1
    assert simplify("1000/3", "1/1000") is False # 1/3000
    assert simplify("123/456", "456/123") is True # 1