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
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    product_num = num_x * num_n
    product_den = den_x * den_n
    
    return product_num % product_den == 0

def test_edge_case():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/1", "1/1") == True
    assert simplify("1/2", "1/1") == False

def test_basic_true():
    assert simplify("1/5", "5/1") == True

def test_basic_false():
    assert simplify("1/6", "2/1") == False

def test_basic_false2():
    assert simplify("7/10", "10/2") == False

def test_large_numbers():
    assert simplify("100/10", "10/1") == True

def test_large_numbers_false():
    assert simplify("100/10", "11/1") == False