
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
from your_module import simplify  # Replace your_module

def test_simplify_true_case1():
    assert simplify("1/5", "5/1") == True

def test_simplify_true_case2():
    assert simplify("2/3", "3/2") == True

def test_simplify_true_case3():
    assert simplify("1/2", "2/1") == True

def test_simplify_false_case1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_case2():
    assert simplify("7/10", "10/2") == False

def test_simplify_false_case3():
    assert simplify("1/3", "4/1") == False

def test_simplify_large_numbers():
    assert simplify("100/200", "200/100") == True

def test_simplify_different_order():
    assert simplify("5/1", "1/5") == True

def test_simplify_single_fraction():
    assert simplify("1/1", "1/1") == True

def test_simplify_another_true_case():
    assert simplify("3/4", "4/3") == True

def test_simplify_another_false_case():
    assert simplify("2/5", "5/2") == False

def test_simplify_edge_case_small_numbers():
    assert simplify("1/2", "2/1") == True

def test_simplify_edge_case_small_numbers2():
    assert simplify("1/3", "3/1") == True

def test_simplify_edge_case_small_numbers3():
    assert simplify("1/4", "4/1") == True

def test_simplify_edge_case_small_numbers4():
    assert simplify("2/3", "3/2") == True

def test_simplify_edge_case_small_numbers5():
    assert simplify("3/4", "4/3") == True