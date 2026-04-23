
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
import math

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
        x_num, x_den = map(int, x.split('/'))
        n_num, n_den = map(int, n.split('/'))

        if x_num < 0 or x_den < 0 or n_num < 0 or n_den < 0:
            raise ValueError("Numerator and denominator must be positive.")

        if x_den == 0 or n_den == 0:
            raise ValueError("Denominator cannot be zero.")

        result_num = x_num * n_num
        result_den = x_den * n_den

        return result_num % result_den == 0
    except ValueError:
        raise

def test_simplify_valid_true_case1():
    assert simplify("1/5", "5/1") == True

def test_simplify_valid_false_case1():
    assert simplify("1/6", "2/1") == False

def test_simplify_valid_false_case2():
    assert simplify("7/10", "10/2") == False

def test_simplify_valid_true_case2():
    assert simplify("2/3", "3/1") == True

def test_simplify_valid_true_case3():
    assert simplify("4/5", "5/4") == True

def test_simplify_valid_false_case3():
    assert simplify("1/2", "1/3") == False

def test_simplify_valid_true_case4():
    assert simplify("6/4", "4/6") == True

def test_simplify_valid_true_case5():
    assert simplify("1/1", "1/1") == True

def test_simplify_valid_true_case6():
    assert simplify("100/10", "10/1") == True

def test_simplify_valid_false_case4():
    assert simplify("100/3", "1/2") == False

def test_simplify_valid_false_case5():
    assert simplify("1/3", "2/5") == False

def test_simplify_zero_numerator():
    assert simplify("0/5", "5/1") == True

def test_simplify_negative_input_invalid():
    with pytest.raises(ValueError):
        simplify("-1/2", "2/1")

def test_simplify_invalid_input_non_numeric():
    with pytest.raises(ValueError):
        simplify("a/2", "2/1")

def test_simplify_invalid_input_zero_denominator():
    with pytest.raises(ValueError):
        simplify("1/0", "2/1")

def test_simplify_large_numbers():
    assert simplify("1000000/2", "2/1") == True

def test_simplify_large_numbers_false():
    assert simplify("1000000/3", "1/2") == False