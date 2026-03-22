import pytest
from typing import List

def simplify(x: str, n: str) -> bool:
    """
    Simplifies the expression x * n.

    Args:
        x: A string representing a fraction.
        n: A string representing a fraction.

    Returns:
        True if x * n evaluates to a whole number, False otherwise.
    """
    try:
        numerator, denominator = x.split('/')
        if denominator == "":
            denominator = 1
        numerator = int(numerator)
        denominator = int(denominator)
        return numerator * denominator == int(numerator)
    except ValueError:
        return False

def test_simplify_valid_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/10", "10/2") == True
    assert simplify("1/10", "2/10") == True
    assert simplify("1/10", "10/2") == True
    assert simplify("1/10", "2/10") == True
    assert simplify("1/10", "10/2") == True
    assert simplify("1/10", "2/10") == True
    assert simplify("1/10", "10/2") == True
    assert simplify("1/10", "2/10") == True
    assert simplify("1/10", "10/2") == True
    assert simplify("1/10", "2/10") == True
    print("All tests passed")