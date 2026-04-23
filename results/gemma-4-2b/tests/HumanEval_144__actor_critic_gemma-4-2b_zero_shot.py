
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
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    try:
        num1, den1 = map(int, x.split('/'))
        num2, den2 = map(int, n.split('/'))
        result = num1 * num2 / den1 / den2
        return result == int(result)
    except ValueError:
        return False


def test_simplify_positive_fractions_equal():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/2", "2/1") == True

def test_simplify_positive_fractions_unequal():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/3") == False

def test_simplify_fractions_with_different_denominators():
    assert simplify("1/2", "1/3") == False
    assert simplify("2/5", "3/4") == False

def test_simplify_fractions_with_large_numbers():
    assert simplify("100/100", "100/100") == True
    assert simplify("1000/1000", "1000/1000") == True

def test_simplify_fractions_with_small_numbers():
    assert simplify("1/10", "10/10") == True
    assert simplify("1/100", "100/100") == True

def test_simplify_fractions_with_mixed_denominators():
    assert simplify("1/2", "2/5") == False
    assert simplify("3/4", "2/3") == False

def test_simplify_fractions_with_negative_numbers():
    assert simplify("-1/2", "2/1") == False
    assert simplify("1/2", "-2/1") == False
    assert simplify("-1/2", "-2/1") == True

def test_simplify_fractions_with_numerator_greater_than_denominator():
    assert simplify("5/2", "2/1") == True
    assert simplify("5/2", "1/2") == False

def test_simplify_fractions_with_denominator_greater_than_numerator():
    assert simplify("2/5", "5/2") == False
    assert simplify("2/5", "2/5") == True

def test_simplify_fractions_with_same_numerator_and_denominator():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "2/2") == True
    assert simplify("5/5", "5/5") == True

def test_simplify_fractions_with_large_numerator_and_denominator():
    assert simplify("1000000/1000000", "1000000/1000000") == True
    assert simplify("1000000/1000000", "1000000/1000000") == False

def test_simplify_fractions_with_one_as_numerator_or_denominator():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_fractions_with_one_as_denominator():
    assert simplify("1/2", "1/1") == True
    assert simplify("2/1", "1/1") == False
    assert simplify("1/1", "1/1") == True

def test_simplify_fractions_with_one_as_numerator():
    assert simplify("1/2", "1/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/1") == True