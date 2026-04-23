
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

    product = (num_x * num_n) / (den_x * den_n)

    return product.is_integer()


### SCoT Steps:

# STEP 1: REASONING
# The function `simplify` checks if the product of two fractions `x` and `n` is an integer.
# It needs to handle different cases where the numerator and denominator of the fractions are different.
# The function should return True if the product is an integer and False otherwise.
# We need to test various scenarios including simple cases, cases where the denominator is a factor of the numerator, and cases where the product is not an integer.

# STEP 2: PLAN
# Test functions:
# - test_simple_true: Tests a simple case where the product is an integer.
# - test_simple_false: Tests a simple case where the product is not an integer.
# - test_denominator_factor: Tests a case where the denominator of `n` is a factor of the numerator of `x`.
# - test_denominator_not_factor: Tests a case where the denominator of `n` is not a factor of the numerator of `x`.
# - test_large_numbers: Tests with larger numbers to ensure no overflow issues.
# - test_edge_case_1: Tests with edge case where numerator and denominator are equal.

# STEP 3: CODE
#

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# STEP 2: PLAN - List test functions names and scenarios.
# STEP 3: CODE - Write the high-quality pytest suite.

def test_simple_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True

def test_simple_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "4/3") == False

def test_denominator_factor():
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True

def test_denominator_not_factor():
    assert simplify("1/3", "2/1") == False
    assert simplify("2/5", "5/1") == False

def test_large_numbers():
    assert simplify("1000/1001", "1001/1") == True
    assert simplify("1000/1002", "1002/1") == False

def test_edge_case_one():
    assert simplify("1/5", "5/1") == True
    assert simplify("5/1", "1/5") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "1/2") == True
    assert simplify("2/1", "1/2") == True