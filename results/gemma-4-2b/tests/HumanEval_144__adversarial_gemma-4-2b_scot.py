
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
        product_num = num1 * num2
        product_den = den1 * den2
        if product_den == 0:
            return False
        return product_num % product_den == 0
    except ValueError:
        return False # Handle invalid input format



def test_basic_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("3/2", "2/1") == True
    assert simplify("1/1", "1/1") == True

def test_different_numerators_denominators():
    assert simplify("1/2", "2/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("1/100", "100/1") == True

def test_larger_numbers():
    assert simplify("10/3", "3/10") == True
    assert simplify("3/10", "10/3") == True

def test_invalid_input():
    assert simplify("1/abc", "2/1") == False #invalid format
    assert simplify("1/5", "5/0") == False #zero denominator
    assert simplify("1/5", "abc/1") == False #invalid format