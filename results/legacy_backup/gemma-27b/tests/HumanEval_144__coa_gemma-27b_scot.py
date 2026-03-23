import pytest
import math


# Focus: Boundary Values
import pytest

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
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    result = (x_num * n_num) / (x_den * n_den)
    return result == int(result)

@pytest.mark.parametrize("x, n, expected", [
    ("1/1", "1/1", True),  # Both are whole numbers
    ("1/2", "2/1", True),  # Simplifies to a whole number
    ("1/3", "3/1", True),
    ("1/4", "4/1", True),
    ("1/5", "5/1", True),
    ("1/6", "6/1", True),
    ("1/7", "7/1", True),
    ("1/8", "8/1", True),
    ("1/9", "9/1", True),
    ("1/10", "10/1", True),
    ("1/2", "1/2", True),  # Simplifies to a whole number
    ("1/3", "1/3", True),
    ("1/4", "1/4", True),
    ("1/5", "1/5", True),
    ("1/6", "1/6", True),
    ("1/7", "1/7", True),
    ("1/8", "1/8", True),
    ("1/9", "1/9", True),
    ("1/10", "1/10", True),
    ("1/2", "2/3", False),  # Does not simplify to a whole number
    ("1/3", "2/5", False),
    ("1/4", "2/7", False),
    ("1/5", "2/9", False),
    ("1/6", "2/11", False),
    ("1/7", "2/13", False),
    ("1/8", "2/15", False),
    ("1/9", "2/17", False),
    ("1/10", "2/19", False),
    ("1/2", "1/3", False),
    ("1/3", "1/4", False),
    ("1/4", "1/5", False),
    ("1/5", "1/6", False),
    ("1/6", "1/7", False),
    ("1/7", "1/8", False),
    ("1/8", "1/9", False),
    ("1/9", "1/10", False),
    ("1/10", "1/11", False),
    ("2/1", "1/2", True),
    ("3/1", "1/3", True),
    ("4/1", "1/4", True),
    ("5/1", "1/5", True),
    ("6/1", "1/6", True),
    ("7/1", "1/7", True),
    ("8/1", "1/8", True),
    ("9/1", "1/9", True),
    ("10/1", "1/10", True),
    ("1/1", "2/1", True),
    ("1/1", "3/1", True),
    ("1/1", "4/1", True),
    ("1/1", "5/1", True),
    ("1/1", "6/1", True),
    ("1/1", "7/1", True),
    ("1/1", "8/1", True),
    ("1/1", "9/1", True),
    ("1/1", "10/1", True),
])
def test_boundary_values(x, n, expected):
    assert simplify(x, n) == expected

# Focus: Equivalence Partitioning
import pytest

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
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    result = (x_num * n_num) / (x_den * n_den)
    return result == int(result)

@pytest.mark.parametrize("x, n, expected", [
    ("1/1", "1/1", True),  # Whole number * Whole number
    ("1/2", "2/1", True),  # Half * Whole number
    ("1/3", "3/1", True),  # Third * Whole number
    ("1/4", "4/1", True),
    ("1/5", "5/1", True),
    ("1/6", "6/1", True),
    ("1/2", "1/2", True),  # Half * Half
    ("1/3", "1/3", True),
    ("1/4", "1/4", True),
    ("1/2", "2/3", False), # Half * Two thirds
    ("1/3", "2/5", False), # Third * Two fifths
    ("2/3", "1/2", False),
    ("3/4", "1/3", False),
    ("7/10", "10/2", False), # Example from prompt
    ("1/6", "2/1", False), # Example from prompt
])
def test_equivalence_partitions(x, n, expected):
    assert simplify(x, n) == expected

# Focus: Error Handling (Invalid Input Format)
import pytest

def test_invalid_input_format_x():
    """Tests invalid input format for x."""
    assert simplify("1/5a", "5/1") is False  # Invalid character in numerator
    assert simplify("1.5/5", "5/1") is False  # Float in numerator
    assert simplify("1/5/", "5/1") is False  # Missing denominator
    assert simplify("1/", "5/1") is False  # Missing denominator
    assert simplify("/5", "5/1") is False  # Missing numerator
    assert simplify("1-5", "5/1") is False  # Incorrect separator
    assert simplify("1/5 ", "5/1") is False # Trailing space

def test_invalid_input_format_n():
    """Tests invalid input format for n."""
    assert simplify("1/5", "5/1a") is False  # Invalid character in numerator
    assert simplify("1/5", "5.5/1") is False  # Float in numerator
    assert simplify("1/5", "5/1/") is False  # Missing denominator
    assert simplify("1/5", "5/", "5/1") is False  # Missing denominator
    assert simplify("1/5", "/1") is False  # Missing numerator
    assert simplify("1/5", "5-1") is False  # Incorrect separator
    assert simplify("1/5", "5/1 ") is False # Trailing space

def test_invalid_input_format_both():
    """Tests invalid input format for both x and n."""
    assert simplify("1/5a", "5/1a") is False  # Invalid characters
    assert simplify("1.5/5", "5.5/1") is False  # Floats
    assert simplify("1/5/", "5/1/") is False  # Missing denominators