
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

# The function signature for reference:
# def simplify(x: str, n: str) -> bool:

@pytest.mark.parametrize("x, n, expected", [
    # --- Provided Examples ---
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    
    # --- Basic Positive Cases (Result is a whole number) ---
    ("1/2", "2/1", True),      # 1
    ("1/2", "4/1", True),      # 2
    ("2/3", "3/2", True),      # 1
    ("3/4", "8/3", True),      # 2
    ("10/1", "10/1", True),    # 100
    ("1/1", "1/1", True),      # 1
    
    # --- Basic Negative Cases (Result is a fraction) ---
    ("1/3", "1/2", False),     # 1/6
    ("2/5", "1/2", False),     # 1/5
    ("3/4", "1/2", False),     # 3/8
    ("5/2", "1/2", False),     # 5/4
    
    # --- Edge Case: Unit Fractions (Numerator is 1) ---
    ("1/10", "20/1", True),    # 2
    ("1/10", "5/1", False),    # 0.5
    ("1/1", "1/1", True),      # 1
    
    # --- Edge Case: Denominator is 1 (Integer representation) ---
    ("5/1", "2/1", True),      # 10
    ("5/1", "1/2", False),     # 2.5
    
    # --- Edge Case: Large Numbers (Testing for overflow/precision issues) ---
    # Python handles arbitrarily large integers, but many implementations 
    # fail if they convert to float first.
    ("1000000000/1", "1/1000000000", True),
    ("123456789/1000000000", "1000000000/123456789", True),
    ("123456789/1", "1/123456789", True),
    ("999999999/1000000000", "1/1", False),
    
    # --- Edge Case: Complex Simplification ---
    # (3/7) * (14/3) = 2
    ("3/7", "14/3", True),
    # (3/7) * (14/5) = 6/5
    ("3/7", "14/5", False),
])
def test_simplify_logic(x, n, expected):
    """Tests various combinations of fractions to ensure correct boolean return."""
    from your_module import simplify # Replace with actual module name
    assert simplify(x, n) == expected

def test_simplify_large_integer_product():
    """
    Specific test for very large products that might cause 
    floating point precision errors if the dev used float division.
    """
    from your_module import simplify
    # (1/10^15) * (10^15/1) = 1
    x = f"1/{10**15}"
    n = f"{10**15}/1"
    assert simplify(x, n) is True

def test_simplify_precision_trap():
    """
    Tests a case where a float might incorrectly round to a whole number.
    """
    from your_module import simplify
    # A very small fraction that is NOT a whole number, 
    # but might be rounded to 0.0 or 1.0 in poorly implemented float logic.
    x = "1/3"
    n = "1/3"
    assert simplify(x, n) is False