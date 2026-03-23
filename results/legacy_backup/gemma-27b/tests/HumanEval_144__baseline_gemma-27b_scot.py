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

    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a

    common_divisor = gcd(result_num, result_den)
    simplified_den = result_den // common_divisor

    return simplified_den == 1

def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/1", "1/4") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "1/2") == False

def test_simplify_denominator_one():
    assert simplify("1/1", "1/1") == True
    assert simplify("5/2", "2/1") == True
    assert simplify("3/4", "1/2") == False

def test_simplify_large_numbers():
    assert simplify("100/5", "5/1") == True
    assert simplify("1000/3", "1/2") == False
    assert simplify("1234/2", "2/1") == True

def test_simplify_simplified_fractions():
    assert simplify("1/2", "1/2") == False
    assert simplify("2/3", "3/4") == False
    assert simplify("3/5", "5/3") == False

def test_simplify_complex_fractions():
    assert simplify("4/6", "9/12") == True
    assert simplify("6/8", "4/10") == False
    assert simplify("10/15", "3/6") == True

def test_simplify_edge_case():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "3/3") == True
    assert simplify("4/4", "5/5") == True