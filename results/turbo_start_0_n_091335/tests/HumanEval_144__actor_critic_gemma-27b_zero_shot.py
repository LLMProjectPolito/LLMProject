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
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    result_num = x_num * n_num
    result_den = x_den * n_den

    gcd = math.gcd(result_num, result_den)
    simplified_num = result_num // gcd
    simplified_den = result_den // gcd

    return simplified_num % simplified_den == 0

def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("4/5", "5/4") == True

def test_simplify_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False

def test_simplify_edge_case():
    assert simplify("1/1", "1/1") == True

def test_simplify_simplifies_to_one():
    assert simplify("2/2", "1/1") == True
    assert simplify("4/4", "2/2") == True

def test_simplify_large_numbers_true():
    assert simplify("100/10", "10/1") == True

def test_simplify_large_numbers_false():
    assert simplify("100/3", "1/2") == False

def test_simplify_large_numbers_overflow():
    assert simplify("999999999999999999/1", "1/1") == True
    assert simplify("999999999999999999/2", "1/1") == False

def test_simplify_different_denominators():
    assert simplify("2/4", "4/2") == True
    assert simplify("1/3", "2/5") == False

def test_simplify_numerator_larger():
    assert simplify("5/2", "2/1") == True

def test_simplify_both_larger():
    assert simplify("5/2", "3/1") == False

def test_simplify_gcd_significant():
    assert simplify("6/8", "4/2") == True  # GCD is important here

# Negative test cases (handling invalid input - though prompt states valid input is assumed)
def test_simplify_invalid_input_format():
    with pytest.raises(ValueError):
        simplify("1", "2/3")

def test_simplify_invalid_input_format2():
    with pytest.raises(ValueError):
        simplify("1/2", "3")