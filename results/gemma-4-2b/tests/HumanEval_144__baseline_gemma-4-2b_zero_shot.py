
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
        result = num1 * num2 / den1 * den2
        return result == int(result)
    except ValueError:
        return False


def test_simplify_true_case_1():
    assert simplify("1/5", "5/1") == True

def test_simplify_true_case_2():
    assert simplify("1/6", "2/1") == False

def test_simplify_true_case_3():
    assert simplify("7/10", "10/2") == False

def test_simplify_true_case_4():
    assert simplify("1/2", "2/1") == True

def test_simplify_true_case_5():
    assert simplify("2/3", "3/1") == True

def test_simplify_true_case_6():
    assert simplify("1/1", "1/1") == True

def test_simplify_true_case_7():
    assert simplify("1/1", "2/1") == False

def test_simplify_false_case_1():
    assert simplify("1/2", "3/1") == False

def test_simplify_false_case_2():
    assert simplify("1/3", "2/1") == False

def test_simplify_false_case_3():
    assert simplify("1/4", "2/1") == False

def test_simplify_invalid_input():
    assert simplify("1/a", "1/1") == False

def test_simplify_invalid_input_2():
    assert simplify("1/1", "1/a") == False

def test_simplify_large_numbers():
    assert simplify("1000/1000", "1000/1000") == True

def test_simplify_small_numbers():
    assert simplify("1/10", "10/10") == True