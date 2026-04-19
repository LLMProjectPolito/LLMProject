
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
    
    # Basic True cases (Product is 1)
    ("1/1", "1/1", True),
    ("1/2", "2/1", True),
    ("2/3", "3/2", True),
    ("10/7", "7/10", True),
    
    # Basic True cases (Product is whole number > 1)
    ("1/2", "4/1", True),   # 2
    ("3/4", "8/1", True),   # 6
    ("5/2", "4/1", True),   # 10
    ("10/1", "1/2", True),  # 5
    ("4/3", "6/1", True),   # 8
    
    # Basic False cases (Product is fraction)
    ("1/3", "1/3", False),  # 1/9
    ("2/5", "1/2", False),  # 1/5
    ("1/10", "5/1", False), # 1/2
    ("3/4", "1/1", False),  # 3/4
    ("1/7", "6/1", False),  # 6/7
    
    # Edge cases: Large numbers
    ("1000000/1", "1/1000000", True),
    ("1000000/1", "1/1000001", False),
    ("1/1000000", "1/1000000", False),
    
    # Edge cases: Numerators/Denominators equal
    ("5/5", "2/2", True),
    ("5/5", "1/2", False),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected