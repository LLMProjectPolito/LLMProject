
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
    def fraction_to_float(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator / denominator

    x_float = fraction_to_float(x)
    n_float = fraction_to_float(n)

    product = x_float * n_float

    return product.is_integer()


import pytest

def test_simplify_basic():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("1/100", "100/1") == True
    assert simplify("100/1", "1/100") == True
    assert simplify("1/2", "1/4") == False
    assert simplify("1/4", "1/2") == False

def test_simplify_larger_numbers():
    assert simplify("123/456", "456/123") == True
    assert simplify("1234/5678", "5678/1234") == True
    assert simplify("12345/67890", "67890/12345") == True
    assert simplify("123456/789012", "789012/123456") == True
    assert simplify("1234567/8901234", "8901234/1234567") == True
    assert simplify("12345678/90123456", "90123456/12345678") == True
    assert simplify("123456789/987654321", "987654321/123456789") == True
    assert simplify("1234567890/9876543210", "9876543210/1234567890") == True
    assert simplify("12345678901/98765432109", "98765432109/12345678901") == True

def test_simplify_unequal_numbers():
    assert simplify("1/2", "1/3") == False
    assert simplify("2/3", "1/2") == False
    assert simplify("1/4", "1/5") == False
    assert simplify("1/10", "1/20") == False
    assert simplify("1/100", "1/101") == False