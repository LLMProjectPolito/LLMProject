import pytest

def simplify(x, n):
    """
    Simplifies the expression x * n.
    Returns True if x * n evaluates to a whole number and False otherwise.
    Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    try:
        numerator, denominator = x.split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        
        if denominator == 0:
            return False
        
        return numerator * denominator == int(numerator * denominator)
    except ValueError:
        return False

def test_simplify_valid_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/1", "1/2") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/4") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/10", "10/2") == False
    assert simplify("1/10", "2/10") == False
    assert simplify("1/10", "10/1") == False
    assert simplify("1/10", "10/1") == False
    assert simplify("1/10", "1/10") == True
    assert simplify("1/10", "10/1") == False
    assert simplify("1/10", "10/2") == False
    assert simplify("1/10", "2/10") == False
    assert simplify("1/10", "10/2") == False
    assert simplify("1/10", "2/10") == False
    assert simplify("1/10", "10/2") == False
    assert simplify("1/10", "10/1") == False
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    print("All tests passed")