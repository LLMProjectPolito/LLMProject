
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

def simplify(x, n):
    """
    Simplifies the expression x * n and returns True if the result is a whole number, 
    False otherwise. x and n are strings in the format "numerator/denominator".
    """
    # Split the strings to get numerators and denominators
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    # Multiplication of fractions: (a/b) * (c/d) = (a*c) / (b*d)
    final_numerator = num_x * num_n
    final_denominator = den_x * den_n
    
    # Check if the result is a whole number
    return final_numerator % final_denominator == 0

@pytest.mark.parametrize("x, n, expected", [
    # Provided examples
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    
    # Basic whole number results
    ("1/1", "1/1", True),
    ("2/1", "3/1", True),
    ("1/2", "2/1", True),
    
    # Fractions that multiply to a whole number (not just inverses)
    ("3/2", "4/3", True),   # 12/6 = 2
    ("10/3", "6/5", True),  # 60/15 = 4
    ("5/4", "8/5", True),   # 40/20 = 2
    
    # Fractions that multiply to a non-whole number
    ("1/3", "1/3", False),  # 1/9
    ("1/2", "1/2", False),  # 1/4
    ("2/3", "1/2", False),  # 2/6 = 1/3
    ("3/4", "5/6", False),  # 15/24
    
    # Edge cases: Large numbers
    ("1000000/1", "1/1000000", True),
    ("1000000/1", "1/2000000", False),
    ("1/1000000", "1000000/1", True),
    ("1000000000000/1", "1/1000000000000", True),
    ("1000000000000/3", "1/1", False),
    
    # Edge cases: Numerators/Denominators of 1
    ("1/10", "10/1", True),
    ("1/10", "1/1", False),
    ("10/1", "1/1", True),
    
    # Cases where numerator is larger than denominator
    ("5/2", "2/5", True),
    ("5/2", "4/5", True),   # 20/10 = 2
    ("5/2", "3/5", False),  # 15/10 = 1.5

    # Edge Case: Zero Numerator (0 is a whole number)
    ("0/1", "1/1", True),
    ("1/1", "0/5", True),
    ("0/5", "0/2", True),

    # Edge Case: Negative Numbers
    ("-1/2", "2/1", True),   # -1 is a whole number
    ("-1/2", "-2/1", True),  # 1 is a whole number
    ("-1/3", "1/1", False),  # -1/3 is not a whole number
    ("1/2", "-1/2", False),  # -1/4 is not a whole number
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_zero_denominator():
    """Verify that a zero denominator raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "1/1")
    with pytest.raises(ZeroDivisionError):
        simplify("1/1", "1/0")