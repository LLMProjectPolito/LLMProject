
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

import pytest

def test_simplify_valid_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_valid_false():
    assert simplify("1/6", "2/1") == False

def test_simplify_valid_false2():
    assert simplify("7/10", "10/2") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "1/2") == True

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True

def test_simplify_small_numbers():
    assert simplify("1/1", "1/1") == True

def test_simplify_one_is_one():
    assert simplify("1/2", "1/1") == True

def test_simplify_one_is_two():
    assert simplify("1/2", "2/1") == False

def test_simplify_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "5/1")

def test_simplify_negative_numbers():
    assert simplify("-1/2", "2/1") == False

def test_simplify_negative_numerator():
    assert simplify("-1/2", "2/1") == False

def test_simplify_negative_denominator():
    assert simplify("1/-2", "2/1") == False

def test_simplify_mixed_negative():
    assert simplify("-1/2", "-2/1") == True

def test_simplify_complex_fraction():
    assert simplify("2/3", "3/4") == True

def test_simplify_complex_fraction_false():
    assert simplify("2/3", "4/5") == False

def test_simplify_large_denominator():
    assert simplify("1/1000", "1000/1") == True

def test_simplify_large_numerator():
    assert simplify("1000/1", "1/1000") == True