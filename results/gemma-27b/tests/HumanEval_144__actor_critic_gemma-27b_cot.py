
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

# Assume simplify function is defined elsewhere.
# For test readability, include a placeholder comment:
# def simplify(x, n):
#     pass

def test_simplify_valid_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/1") == True
    assert simplify("4/5", "5/4") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "1/2") == False
    assert simplify("1/2", "1/1") == False
    assert simplify("1/3", "1/2") == False
    assert simplify("2/3", "1/2") == False
    assert simplify("1/100", "100/1") == True
    assert simplify("100/1", "1/100") == True
    assert simplify("1/1000", "1000/1") == True

def test_simplify_with_large_numbers():
    assert simplify("1000/1", "1/1000") == True
    assert simplify("12345/1", "1/12345") == True
    assert simplify("12345/6789", "6789/12345") == True

def test_simplify_identical_fractions():
    assert simplify("2/3", "2/3") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_negative_numerators():
    assert simplify("-1/2", "2/1") == False
    assert simplify("1/2", "-2/1") == False
    assert simplify("-1/2", "-2/1") == True
    assert simplify("-2/3", "3/-2") == True

def test_simplify_negative_denominators():
    assert simplify("1/-2", "2/1") == False
    assert simplify("1/2", "-2/1") == False
    assert simplify("1/-2", "-2/1") == True

def test_simplify_zero_numerators():
    assert simplify("0/5", "0/1") == True
    assert simplify("0/1", "0/2") == True

def test_simplify_invalid_input():
    with pytest.raises(ValueError):
        simplify("1a/2", "2/1")
    with pytest.raises(ValueError):
        simplify("1/2b", "2/1")
    with pytest.raises(ValueError):
        simplify("abc", "2/1")
    with pytest.raises(ValueError):
        simplify("1/2", "abc")

def test_simplify_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "1/1")
    with pytest.raises(ZeroDivisionError):
        simplify("1/1", "1/0")

def test_simplify_reciprocals():
    assert simplify("2/5", "5/2") == True
    assert simplify("3/7", "7/3") == True
    assert simplify("4/9", "9/4") == True
    assert simplify("5/11", "11/5") == True