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
    def get_numerator(fraction):
        return int(fraction.split('/')[0])

    def get_denominator(fraction):
        return int(fraction.split('/')[1])

    num_x = get_numerator(x)
    den_x = get_denominator(x)
    num_n = get_numerator(n)
    den_n = get_denominator(n)

    product_num = num_x * num_n
    product_den = den_x * den_n

    if product_num % product_den == 0:
        return True
    else:
        return False

def test_simplify_edge_case_large_numbers():
    assert simplify("1000/1001", "1001/1") == True

def test_simplify_basic_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_basic_false():
    assert simplify("1/6", "2/1") == False

def test_simplify_basic_false2():
    assert simplify("7/10", "10/2") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "1/2") == True

def test_simplify_zero_denominator():
    assert simplify("1/0", "0/1") == False