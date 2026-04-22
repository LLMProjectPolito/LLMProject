
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
    # Provided examples
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),

    # Identity and simple whole numbers
    ("1/1", "1/1", True),
    ("2/1", "3/1", True),
    ("1/1", "5/1", True),

    # Reciprocals resulting in 1
    ("2/3", "3/2", True),
    ("5/7", "7/5", True),
    ("123/456", "456/123", True),

    # Resulting in whole numbers > 1
    ("4/1", "2/1", True),
    ("1/2", "4/1", True),
    ("10/3", "3/1", True),
    ("10/3", "6/1", True),  # (10/3) * 6 = 20

    # Resulting in non-whole numbers (decimals/fractions)
    ("1/2", "1/2", False),
    ("3/5", "2/5", False),
    ("10/3", "1/1", False),
    ("1/10", "1/10", False),
    ("5/4", "1/2", False),

    # Large numbers
    ("1000000/1", "1/1000000", True),
    ("1000000/3", "3/1", True),
    ("1000000/3", "1/1", False),
    ("999999/1000000", "1000000/999999", True),
])
def test_simplify(x, n, expected):
    """
    Tests the simplify function with various fraction combinations to ensure
    it correctly identifies if the product is a whole number.
    """
    assert simplify(x, n) == expected

def test_simplify_type_consistency():
    """
    Ensures the function returns a boolean type.
    """
    assert isinstance(simplify("1/1", "1/1"), bool)
    assert isinstance(simplify("1/2", "1/2"), bool)