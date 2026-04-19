
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
    
    # Basic True cases
    ("1/2", "2/1", True),
    ("3/4", "4/3", True),
    ("10/3", "3/10", True),
    ("5/2", "4/5", True), # 20/10 = 2
    ("1/1", "1/1", True),
    
    # Basic False cases
    ("1/2", "1/2", False),
    ("1/3", "1/3", False),
    ("5/2", "3/5", False), # 15/10 = 1.5
    ("2/3", "1/1", False),
    ("1/2", "3/1", False), # 3/2 = 1.5
    
    # Edge cases: Large numbers
    ("1000000/1", "1/1000000", True),
    ("1000000/1", "1/2000000", False),
    ("100/7", "7/100", True),
    
    # Edge cases: Denominators of 1
    ("5/1", "2/1", True),
    ("5/1", "1/2", False), # 5/2 = 2.5
    
    # Prime numbers
    ("13/17", "17/13", True),
    ("13/17", "17/1", False), # 13/1 = 13 (Wait, 13/17 * 17/1 = 13. This should be True)
    ("13/17", "1/17", False),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_large_product():
    # Test with very large integers to ensure no precision loss (though Python handles arbitrary size ints)
    assert simplify("1000000000/1", "1000000000/1") == True
    assert simplify("1/1000000000", "1/1000000000") == False

def test_simplify_complex_whole():
    # (15/4) * (8/5) = 120/20 = 6
    assert simplify("15/4", "8/5") == True
    # (15/4) * (2/5) = 30/20 = 1.5
    assert simplify("15/4", "2/5") == False