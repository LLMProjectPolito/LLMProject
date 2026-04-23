
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

def gcd(a, b):
    """Calculates the greatest common divisor of two integers."""
    while(b):
        a, b = b, a % b
    return a

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

    # Simplify fractions before multiplication
    x_gcd = gcd(x_num, x_den)
    x_num //= x_gcd
    x_den //= x_gcd

    n_gcd = gcd(n_num, n_den)
    n_num //= n_gcd
    n_den //= n_gcd

    # Simplify during multiplication
    result_num = (x_num * n_num)
    result_den = (x_den * n_den)

    result_gcd = gcd(result_num, result_den)
    result_num //= result_gcd
    result_den //= result_gcd

    return result_num % result_den == 0

### Tests (Pytest):
def test_simplify_basic():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False

def test_simplify_whole_number():
    assert simplify("2/1", "3/1") == True
    assert simplify("4/2", "1/1") == True

def test_simplify_already_simplified():
    assert simplify("1/2", "1/3") == False
    assert simplify("1/2", "2/4") == False

def test_simplify_larger_numbers():
    assert simplify("12/5", "5/12") == True
    assert simplify("100/3", "3/100") == False

def test_simplify_edge_case():
    assert simplify("1/1", "1/1") == True

def test_simplify_gcd_crucial():
    assert simplify("2/4", "3/6") == False  # 1/2 * 1/2 = 1/4
    assert simplify("4/6", "6/4") == True # 2/3 * 3/2 = 1

def test_simplify_non_whole_result():
    assert simplify("15/8", "4/5") == False

def test_simplify_whole_result():
    assert simplify("21/10", "5/7") == True

def test_simplify_large_numbers():
    assert simplify("1000/1", "1/1000") == True
    assert simplify("1000/2", "1/1000") == False

def test_simplify_zero_numerator():
    assert simplify("0/5", "5/1") == True

def test_simplify_large_numbers_overflow():
    assert simplify("999999999/1", "999999999/1") == True