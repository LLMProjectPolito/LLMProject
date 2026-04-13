
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

def test_simplify_true_case_1():
    assert simplify("1/5", "5/1") == True

def test_simplify_false_case_1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_case_2():
    assert simplify("7/10", "10/2") == False

def test_simplify_true_case_2():
    assert simplify("2/3", "3/1") == True

def test_simplify_true_case_3():
    assert simplify("4/5", "5/4") == True

def test_simplify_false_case_3():
    assert simplify("1/2", "3/4") == False

def test_simplify_true_case_4():
    assert simplify("1/1", "1/1") == True

def test_simplify_false_case_4():
    assert simplify("1/3", "1/2") == False

def test_simplify_true_case_5():
    assert simplify("2/4", "2/1") == True

def test_simplify_false_case_5():
    assert simplify("3/5", "2/1") == False

def test_simplify_with_larger_numbers_true():
    assert simplify("10/20", "2/1") == True

def test_simplify_with_larger_numbers_false():
    assert simplify("10/21", "2/1") == False

def test_simplify_with_same_fraction():
    assert simplify("5/5", "5/5") == True

def test_simplify_with_one_as_numerator():
    assert simplify("1/7", "7/1") == True

def test_simplify_with_one_as_denominator():
    assert simplify("5/1", "1/5") == True

def test_simplify_with_different_denominators():
    assert simplify("2/3", "4/6") == True

def test_simplify_with_different_numerators():
    assert simplify("4/6", "2/3") == True