
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

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "1/2") == False
    assert simplify("2/1", "1/2") == False
    assert simplify("1/100", "100/1") == True
    assert simplify("100/1", "1/100") == True
    assert simplify("0/5", "1/1") == False  # Zero numerator
    assert simplify("1/0", "1/1") == False  # Invalid input - zero denominator
    with pytest.raises(ValueError):
        simplify("a/b", "1/1")  # Invalid input - non-numeric
    assert simplify("1", "1/1") == False  # Invalid input - missing slash
    assert simplify("1/", "1/1") == False  # Invalid input - missing denominator
    assert simplify("0/0", "1/1") == False # Zero numerator and denominator

def test_simplify_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("4/7", "7/1") == True
    assert simplify("5/2", "2/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False
    assert simplify("2/5", "3/1") == False
    assert simplify("3/4", "5/1") == False

def test_simplify_large_numbers():
    assert simplify("1000/5", "5/1") == True
    assert simplify("1000/7", "7/1") == True
    assert simplify("1000/3", "3/1") == True
    assert simplify("1000/11", "11/1") == True

def test_simplify_different_denominators():
    assert simplify("2/3", "6/9") == True
    assert simplify("4/5", "8/10") == True
    assert simplify("1/2", "3/6") == True
    assert simplify("1/4", "2/8") == True

def test_simplify_common_factors():
    assert simplify("6/8", "4/1") == False
    assert simplify("9/12", "3/1") == True
    assert simplify("10/15", "2/1") == True
    assert simplify("14/28", "1/2") == True

def test_simplify_different_simplifications():
    assert simplify("12/15", "25/5") == False
    assert simplify("14/21", "3/1") == True
    assert simplify("16/24", "4/1") == True
    assert simplify("20/30", "6/1") == False

def test_simplify_negative_numbers():
    assert simplify("-1/5", "5/1") == False
    assert simplify("1/-5", "5/1") == False
    assert simplify("-1/-5", "5/1") == True
    assert simplify("5/-1", "1/5") == False
    assert simplify("-1/5", "-5/1") == True
    assert simplify("1/-5", "-5/1") == True
    assert simplify("-1/-5", "-5/1") == True
    assert simplify("5/-1", "-1/5") == True

def test_simplify_simplification_to_one():
    assert simplify("5/5", "1/1") == True
    assert simplify("10/10", "1/1") == True

def test_simplify_negative_denominator():
    assert simplify("1/-1", "1/1") == True

def test_simplify_invalid_format():
    with pytest.raises(ValueError):
        simplify("1/2/3", "1/1")
    with pytest.raises(ValueError):
        simplify("a/b/c", "1/1")