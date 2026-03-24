
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
# The function `simplify(x, n)` checks if the product of two fractions, represented as strings, is a whole number.
# It needs to handle different denominators and ensure that the result of the multiplication is an integer.
# The function should return True if the product is an integer and False otherwise.
# We need to test various scenarios including cases where the denominators are the same, different, and where the product is an integer or not.

# STEP 2: PLAN
# Test functions:
# - test_same_denominator: Tests cases where the denominators of x and n are the same.
# - test_different_denominator: Tests cases where the denominators of x and n are different.
# - test_integer_result: Tests cases where the product of x and n is an integer.
# - test_non_integer_result: Tests cases where the product of x and n is not an integer.
# - test_edge_cases: Tests edge cases like simple fractions and cases that might expose potential errors.

# STEP 3: CODE
#

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# STEP 2: PLAN - List test functions names and scenarios.
# STEP 3: CODE - Write the high-quality pytest suite.

def test_same_denominator():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("1/2", "2/1") == True

def test_different_denominator():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "4/5") == False

def test_integer_result():
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("4/5", "5/1") == True

def test_non_integer_result():
    assert simplify("1/2", "2/2") == False
    assert simplify("3/4", "4/3") == False
    assert simplify("5/6", "6/2") == False

def test_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "1/1") == False
    assert simplify("1/1", "1/2") == False
    assert simplify("1/1", "2/1") == True
    assert simplify("2/1", "1/1") == True