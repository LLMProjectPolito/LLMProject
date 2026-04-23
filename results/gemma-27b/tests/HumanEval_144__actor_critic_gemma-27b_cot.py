
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

def test_simplify_valid_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/1") == True
    assert simplify("4/5", "5/4") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True
    assert simplify("2/3", "2/3") == True  # Identical fractions

def test_simplify_unit_fractions():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "3/1") == False
    assert simplify("4/1", "2/1") == True

def test_simplify_invalid_input():
    with pytest.raises(ValueError):
        simplify("1/a", "5/1")
    with pytest.raises(ValueError):
        simplify("abc", "5/1")
    with pytest.raises(ValueError):
        simplify("1", "5/1")
    with pytest.raises(ValueError):
        simplify("1/2/3", "5/1")

def test_simplify_zero_numerator():
    assert simplify("0/1", "1/1") == False
    assert simplify("1/1", "0/1") == False
    assert simplify("0/5", "5/1") == False
    assert simplify("0/1", "0/1") == False # Both zero

def test_simplify_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "1/1")
    with pytest.raises(ZeroDivisionError):
        simplify("1/1", "0/1")

def test_simplify_negative_numbers():
    assert simplify("-1/5", "5/1") == False
    assert simplify("1/5", "-5/1") == False
    assert simplify("-1/5", "-5/1") == True
    assert simplify("-2/3", "3/-2") == True

def test_simplify_large_numbers():
    assert simplify("100/1", "1/100") == True
    assert simplify("1000/1", "1/1000") == True
    assert simplify("100/2", "2/100") == True
    assert simplify("1000/2", "2/1000") == True

def test_simplify_non_reciprocal_fractions():
    assert simplify("2/5", "5/2") == True
    assert simplify("3/7", "7/3") == True
    assert simplify("4/9", "9/4") == True
    assert simplify("11/13", "13/11") == True
    assert simplify("100/101", "101/100") == True

def test_simplify_mixed_whole_and_fraction():
    assert simplify("2/1", "1/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("3/1", "1/3") == False
    assert simplify("1/3", "3/1") == True

def test_simplify_complex_fractions():
    assert simplify("12/15", "15/12") == True
    assert simplify("24/36", "36/24") == True
    assert simplify("10/25", "25/10") == True

def test_simplify_same_value_different_form():
    assert simplify("2/4", "1/2") == True

def test_simplify_zero_numerator_first():
    assert simplify("0/1", "2/3") == False

def test_simplify_negative_zero():
    with pytest.raises(ZeroDivisionError):
        simplify("-0/1", "1/1")
    with pytest.raises(ZeroDivisionError):
        simplify("1/1", "0/-1")