
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

    # Calculate GCD to simplify the fraction
    gcd = math.gcd(result_num, result_den)
    result_num //= gcd
    result_den //= gcd

    return result_den == 1

### Tests (Pytest):
def test_simplify_whole():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole():
    assert simplify("1/6", "2/1") == False

def test_simplify_complex():
    assert simplify("7/10", "10/2") == False

def test_simplify_gcd_needed():
    assert simplify("2/4", "1/2") == True

def test_simplify_large_numbers():
    assert simplify("1000/2", "2/1") == True

def test_simplify_another_gcd():
    assert simplify("4/6", "3/2") == True

def test_simplify_no_gcd():
    assert simplify("1/2", "1/3") == False

def test_simplify_denominator_one():
    assert simplify("1/1", "1/1") == True

def test_simplify_numerator_one():
    assert simplify("1/2", "1/1") == False

def test_simplify_both_one():
    assert simplify("1/1", "1/1") == True

def test_simplify_large_gcd():
    assert simplify("12345/6", "6/1") == True