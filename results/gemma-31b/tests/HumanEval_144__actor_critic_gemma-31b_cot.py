
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
    
    # Basic integer results
    ("1/2", "2/1", True),   # 1/1 = 1
    ("1/2", "4/1", True),   # 4/2 = 2
    ("3/4", "8/3", True),   # 24/12 = 2
    ("10/3", "3/10", True), # 30/30 = 1
    ("5/1", "2/1", True),   # 10/1 = 10
    
    # Basic non-integer results
    ("3/4", "2/1", False),  # 6/4 = 1.5
    ("1/3", "2/1", False),  # 2/3 = 0.66...
    ("1/5", "1/2", False),  # 1/10 = 0.1
    ("10/3", "1/1", False), # 10/3 = 3.33...
    
    # Edge cases: Identity and Unity
    ("1/1", "1/1", True),   # 1 * 1 = 1
    ("1/1", "2/1", True),   # 1 * 2 = 2
    ("1/1", "1/2", False),  # 1 * 0.5 = 0.5
    
    # Edge cases: Large numbers
    ("1000000/1", "1/1000000", True), # 1
    ("1000000/1", "1000000/1", True), # 10^12
    ("1/1000000", "1/1000000", False), # 1/10^12
    
    # Edge cases: Fractions that simplify to integers
    ("123/456", "456/123", True), # 1
    ("123/456", "912/123", True), # (123*912)/(456*123) = 912/456 = 2
    ("123/456", "456/246", False), # (123*456)/(456*246) = 123/246 = 0.5
    
    # Edge Case: Zero Numerators
    ("0/1", "1/1", True),   # 0 * 1 = 0
    ("1/1", "0/5", True),   # 1 * 0 = 0
    ("0/5", "0/5", True),   # 0 * 0 = 0
    
    # Edge Case: Negative Numbers (Numerators and Denominators)
    ("-1/2", "2/1", True),   # -1
    ("-1/2", "-2/1", True),  # 1
    ("1/-2", "2/1", True),   # -1
    ("1/-2", "-2/1", True),  # 1
    ("-1/3", "1/1", False),  # -0.33...
    ("1/3", "-1/1", False),  # -0.33...
    ("1/-3", "1/1", False),  # -0.33...
    
    # Whitespace Handling
    (" 1/5 ", " 5/1 ", True),
    (" 1 / 2 ", " 2 / 1 ", True),
    ("1/ 2", " 2/1", True),
    
    # Precision Risk: Values exceeding 2^53
    ("2305843009213693951/1", "1/2305843009213693951", True), 
    ("2305843009213693951/1", "1/1", True),
    ("2305843009213693951/1", "1/2", False),
    ("100000000000000000000/1", "1/100000000000000000000", True),
])
def test_simplify_logic(x, n, expected):
    """
    Tests the simplify function with various combinations of fractions
    to ensure it correctly identifies if the product is an integer.
    """
    assert simplify(x, n) == expected

@pytest.mark.parametrize("x, n", [
    ("a/b", "1/1"),       # Non-numeric
    ("1/c", "1/1"),       # Non-numeric
    ("5", "1/1"),         # Missing slash
    ("100", "1/1"),       # Missing slash
    ("1/2/3", "1/1"),     # Multiple slashes
    ("", "1/1"),          # Empty string
    (" ", "1/1"),         # Whitespace only
])
def test_simplify_malformed_strings(x, n):
    """
    Verifies that the function raises ValueError for malformed fraction strings.
    """
    with pytest.raises(ValueError):
        simplify(x, n)

@pytest.mark.parametrize("x, n", [
    (None, "1/1"),
    ("1/1", None),
    (123, "1/1"),
])
def test_simplify_invalid_types(x, n):
    """
    Verifies that the function raises TypeError for non-string inputs.
    """
    with pytest.raises(TypeError):
        simplify(x, n)

def test_simplify_division_by_zero():
    """
    Verifies that the function handles invalid denominators (division by zero)
    by raising a ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "1/1")
    with pytest.raises(ZeroDivisionError):
        simplify("1/1", "1/0")
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "1/0")