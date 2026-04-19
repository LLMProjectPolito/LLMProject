
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

# The function simplify is already defined in the environment.
# We are writing the test suite for it.

@pytest.mark.parametrize("x, n, expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
])
def test_docstring_examples(x, n, expected):
    """Verify the examples provided in the function docstring."""
    assert simplify(x, n) == expected

@pytest.mark.parametrize("x, n", [
    ("1/1", "1/1"),       # 1 * 1 = 1
    ("2/1", "3/1"),       # 2 * 3 = 6
    ("1/2", "2/1"),       # 0.5 * 2 = 1
    ("1/2", "4/1"),       # 0.5 * 4 = 2
    ("3/4", "8/3"),       # (3*8)/(4*3) = 24/12 = 2
    ("10/3", "3/10"),     # 1
    ("5/2", "4/5"),       # (5*4)/(2*5) = 20/10 = 2
    ("100/1", "1/100"),   # 1
])
def test_whole_number_products(x, n):
    """Test cases where the product of fractions is a whole number."""
    assert simplify(x, n) is True

@pytest.mark.parametrize("x, n", [
    ("1/2", "1/2"),       # 1/4
    ("1/3", "1/1"),       # 1/3
    ("2/3", "1/2"),       # 2/6 = 1/3
    ("7/10", "1/1"),      # 7/10
    ("3/4", "1/2"),       # 3/8
    ("1/10", "9/1"),      # 9/10
    ("11/13", "1/1"),     # 11/13
])
def test_non_whole_number_products(x, n):
    """Test cases where the product of fractions is NOT a whole number."""
    assert simplify(x, n) is False

def test_large_values():
    """Test with large integers to ensure no overflow issues."""
    # (10^12 / 1) * (1 / 10^12) = 1
    x = "1000000000000/1"
    n = "1/1000000000000"
    assert simplify(x, n) is True
    
    # (10^12 / 1) * (1 / (10^12 + 1)) = fraction
    n_plus = "1/1000000000001"
    assert simplify(x, n_plus) is False

def test_unit_fractions():
    """Test cases involving 1/1 as identity."""
    assert simplify("5/1", "1/1") is True
    assert simplify("1/2", "1/1") is False
    assert simplify("1/1", "1/1") is True