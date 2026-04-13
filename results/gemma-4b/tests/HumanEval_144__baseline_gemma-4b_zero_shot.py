
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
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))

    product_num = num_x * num_n
    product_den = den_x * den_n

    if product_num % product_den == 0:
        return True
    else:
        return False

### Tests (Pytest):
def test_simplify_1():
    assert simplify("1/5", "5/1") == True

def test_simplify_2():
    assert simplify("1/6", "2/1") == False

def test_simplify_3():
    assert simplify("7/10", "10/2") == False

def test_simplify_4():
    assert simplify("1/1", "1/1") == True

def test_simplify_5():
    assert simplify("2/3", "3/2") == True

def test_simplify_6():
    assert simplify("3/4", "4/3") == True

def test_simplify_7():
    assert simplify("4/3", "3/4") == True

def test_simplify_8():
    assert simplify("10/3", "3/10") == True

def test_simplify_9():
    assert simplify("1/2", "2/3") == False

def test_simplify_10():
    assert simplify("5/7", "7/5") == True

def test_simplify_11():
    assert simplify("1/1", "2/1") == False

def test_simplify_12():
    assert simplify("1/2", "1/2") == True

def test_simplify_13():
    assert simplify("100/10", "10/1") == True

def test_simplify_14():
    assert simplify("10/10", "10/1") == True

def test_simplify_15():
    assert simplify("1/10", "10/1") == False