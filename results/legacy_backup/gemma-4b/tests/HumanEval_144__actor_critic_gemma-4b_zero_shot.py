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

# Tests (Pytest):
def test_simplify_basic():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "1/2") == True
    assert simplify("5/7", "5/7") == True

def test_simplify_larger_numbers():
    assert simplify("10/3", "3/2") == True
    assert simplify("12/5", "5/4") == False

def test_simplify_edge_case_1():
    assert simplify("1/1", "1/1") == True

def test_simplify_edge_case_2():
    assert simplify("1/1", "2/1") == False

def test_simplify_edge_case_3():
    assert simplify("1/2", "1/1") == True

def test_simplify_edge_case_4():
    assert simplify("2/3", "3/2") == True

def test_simplify_edge_case_5():
    assert simplify("1/3", "2/1") == False

def test_simplify_edge_case_6():
    assert simplify("100/1", "1/1") == True

def test_simplify_edge_case_7():
    assert simplify("1/100", "1/1") == False

def test_simplify_large_numerator_denominator():
    assert simplify("12345/67890", "67890/12345") == True
    assert simplify("12345/67890", "67890/12346") == False