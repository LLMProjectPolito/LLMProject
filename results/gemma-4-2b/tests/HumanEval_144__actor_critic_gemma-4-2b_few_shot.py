
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
        return False  # Handle cases where input strings are not valid fractions


import pytest

def test_simplify_basic():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/1", "1/1") == True
    assert simplify("2/1", "2/1") == True
    assert simplify("1/1", "1/2") == False
    assert simplify("1/2", "1/1") == False

def test_simplify_different_numbers():
    assert simplify("1/2", "3/4") == False
    assert simplify("2/3", "4/6") == False
    assert simplify("1/3", "2/6") == True
    assert simplify("3/2", "1/2") == True

def test_simplify_large_numbers():
    assert simplify("100/200", "200/100") == True
    assert simplify("100/200", "100/200") == False

def test_simplify_same_numerator():
    assert simplify("5/5", "5/1") == True
    assert simplify("5/5", "1/5") == False

def test_simplify_same_denominator():
    assert simplify("1/5", "5/5") == True
    assert simplify("1/5", "5/5") == False

def test_simplify_mixed_numbers():
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == False

def test_simplify_edge_case_1_1():
    assert simplify("1/1", "1/1") == True

def test_simplify_edge_case_1_2():
    assert simplify("1/2", "1/1") == False

def test_simplify_edge_case_2_1():
    assert simplify("2/1", "1/1") == True