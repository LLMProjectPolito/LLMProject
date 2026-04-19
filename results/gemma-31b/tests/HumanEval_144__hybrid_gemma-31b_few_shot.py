
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
    # --- Docstring & Basic Examples ---
    ("1/5", "5/1", True),    # 1
    ("1/6", "2/1", False),   # 1/3
    ("7/10", "10/2", False), # 3.5
    
    # --- Cases resulting in Whole Numbers (True) ---
    ("3/1", "2/1", True),    # 6
    ("2/3", "9/2", True),    # 3
    ("7/10", "10/7", True),  # 1
    ("1/1", "1/1", True),    # 1
    ("10/3", "3/10", True),  # 1
    ("10/3", "6/10", True),  # 2
    ("100/1", "1/100", True),# 1
    ("5/2", "4/5", True),    # 2
    ("1/2", "2/1", True),    # 1
    ("3/4", "8/3", True),    # 2
    ("10/1", "10/1", True),  # 100
    ("4/2", "1/2", True),    # 1
    ("100/3", "3/100", True),# 1
    ("1/7", "49/1", True),   # 7
    
    # --- Cases resulting in Fractions (False) ---
    ("1/3", "1/3", False),   # 1/9
    ("4/5", "6/5", False),   # 24/25
    ("10/3", "1/10", False), # 1/3
    ("5/2", "1/5", False),   # 1/2
    ("1/2", "1/2", False),   # 1/4
    ("3/2", "1/1", False),   # 1.5
    ("2/3", "4/3", False),   # 8/9
    ("7/3", "2/1", False),   # 4.66...
    ("1/10", "1/10", False), # 0.01
    ("11/13", "1/1", False), # 11/13
    
    # --- Cases where inputs are already reducible to integers ---
    ("4/2", "6/2", True),    # 2 * 3 = 6
    ("4/2", "3/2", True),    # 2 * 1.5 = 3
    ("4/2", "1/3", False),   # 2 * 1/3 = 2/3
])
def test_simplify_logic(x, n, expected):
    """Tests a comprehensive range of fraction combinations including docstring examples."""
    assert simplify(x, n) == expected

def test_simplify_precision():
    """Tests the function with larger integers to ensure no floating point precision loss."""
    # Exact whole number
    assert simplify("1000000/1", "1/1000000") == True
    # Slightly above a whole number
    assert simplify("1000001/1", "1/1000000") == False