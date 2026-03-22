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
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    result_num = x_num * n_num
    result_den = x_den * n_den

    return result_num % result_den == 0

def test_simplify_true_case1():
    assert simplify("1/5", "5/1") == True

def test_simplify_false_case1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_case2():
    assert simplify("7/10", "10/2") == False

def test_simplify_true_case2():
    assert simplify("2/3", "3/1") == True

def test_simplify_true_case3():
    assert simplify("4/5", "5/4") == True

def test_simplify_false_case3():
    assert simplify("1/2", "1/3") == False

def test_simplify_large_numbers_true():
    assert simplify("100/20", "2/1") == True

def test_simplify_large_numbers_false():
    assert simplify("100/21", "2/1") == False

def test_simplify_same_fraction():
    assert simplify("2/2", "2/2") == True

def test_simplify_one_whole_number():
    assert simplify("1/1", "2/1") == True

def test_simplify_another_whole_number():
    assert simplify("2/1", "1/1") == True

def test_simplify_complex_true():
    assert simplify("15/4", "4/3") == True

def test_simplify_complex_false():
    assert simplify("15/4", "4/5") == False

def test_simplify_with_larger_denominators():
    assert simplify("1/100", "100/1") == True

def test_simplify_with_larger_denominators_false():
    assert simplify("1/101", "100/1") == False