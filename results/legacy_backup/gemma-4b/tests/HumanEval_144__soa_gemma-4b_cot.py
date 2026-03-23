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

def test_simplify_positive_whole_numbers():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "6/1") == True
    assert simplify("4/7", "14/1") == False

def test_simplify_with_larger_numbers():
    assert simplify("10/2", "2/1") == True
    assert simplify("12/3", "3/1") == True
    assert simplify("15/4", "4/1") == False

def test_simplify_with_different_denominators():
    assert simplify("1/2", "3/4") == False
    assert simplify("2/5", "7/10") == False
    assert simplify("3/4", "5/6") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/1", "1/1") == True
    assert simplify("0/1", "1/1") == True
    assert simplify("1/0", "1/1") == False # Should handle invalid denominator

def test_simplify_with_equal_numerators_and_denominators():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "2/2") == True
    assert simplify("3/3", "3/3") == True
    assert simplify("4/4", "4/4") == True
    assert simplify("5/5", "5/5") == True

def test_simplify_with_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("1000/100", "10/1") == True
    assert simplify("10000/1000", "10/1") == True
    assert simplify("100000/10000", "10/1") == True
    assert simplify("1000000/100000", "10/1") == True
    assert simplify("1000001/100000", "10/1") == False