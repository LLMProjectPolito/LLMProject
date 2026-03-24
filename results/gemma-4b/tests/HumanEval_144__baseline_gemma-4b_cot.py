
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

### Test Cases
def test_simplify_valid():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("10/3", "3/1") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_invalid():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False
    assert simplify("1/4", "3/1") == False

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("100/11", "10/1") == False

def test_simplify_equal_fractions():
    assert simplify("1/2", "1/2") == True
    assert simplify("5/7", "5/7") == True

def test_simplify_one_is_one():
    assert simplify("1/5", "1/1") == True
    assert simplify("5/1", "1/1") == True

def test_simplify_zero_denominator():
    # This test case is not explicitly mentioned in the problem description,
    # but it's good to consider edge cases.  The problem states that x and n
    # are valid fractions, and do not have zero as denominator.
    # However, if we were to handle this case, we would need to raise an exception.
    # For this test suite, we will assume that the input is always valid.
    pass