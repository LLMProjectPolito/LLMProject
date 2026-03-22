import pytest
import math


# Focus: Boundary Values
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

@pytest.mark.boundary
def test_simplify_boundary_zero_denominator():
    assert simplify("1/5", "5/0") == False

@pytest.mark.boundary
def test_simplify_boundary_numerator_zero():
    assert simplify("0/5", "5/1") == True

@pytest.mark.boundary
def test_simplify_boundary_numerator_one():
    assert simplify("1/5", "5/1") == True

@pytest.mark.boundary
def test_simplify_boundary_denominator_one():
    assert simplify("1/5", "5/1") == True

# Focus: Type Scenarios
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

def test_simplify_whole_number():
    assert simplify("1/1", "1/1") == True

def test_simplify_fraction_whole_number():
    assert simplify("2/3", "3/1") == True

def test_simplify_fraction_not_whole_number():
    assert simplify("1/2", "2/1") == False

# Focus: Logic Branches
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

def test_simplify_whole_number():
    assert simplify("1/1", "1/1") == True

def test_simplify_no_whole_number():
    assert simplify("1/2", "2/1") == False

def test_simplify_fraction_multiplication():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False