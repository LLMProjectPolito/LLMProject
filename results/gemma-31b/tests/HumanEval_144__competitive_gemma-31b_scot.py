
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

@pytest.mark.parametrize("x, n, expected", [
    # Docstring examples
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    
    # Basic True cases
    ("1/1", "1/1", True),
    ("2/1", "3/1", True),
    ("1/2", "2/1", True),
    ("3/4", "8/3", True),
    ("10/3", "3/10", True),
    ("4/5", "5/4", True),
    ("4/5", "10/4", True),
    
    # Basic False cases
    ("1/2", "1/2", False),
    ("1/3", "1/3", False),
    ("10/3", "1/10", False),
    ("4/5", "11/4", False),
    ("1/7", "6/1", False),
    
    # Edge cases: Large numbers
    ("100/1", "1/100", True),
    ("1000000/1", "1/1000000", True),
    ("1/1000000", "1/1000000", False),
    
    # Edge cases: Numerators/Denominators as 1
    ("1/1", "5/1", True),
    ("1/1", "1/5", False),
    ("5/1", "1/1", True),
    ("1/5", "1/1", False),
    
    # Cases where product is a whole number > 1
    ("5/2", "4/1", True), # 20/2 = 10
    ("3/2", "2/3", True), # 6/6 = 1
    ("3/2", "4/3", True), # 12/6 = 2
    ("7/3", "9/7", True), # 63/21 = 3
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected