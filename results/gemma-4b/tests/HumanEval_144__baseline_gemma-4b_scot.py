
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

### STEP 1: REASONING
# The function `simplify(x, n)` checks if the product of two fractions, represented as strings, is a whole number.
# We need to test various scenarios with different numerators and denominators to ensure the function returns the correct boolean value.
# The function should handle cases where the product is an integer and cases where it is not.
# We should test edge cases like simple fractions and more complex fractions.

### STEP 2: PLAN
# Test cases:
# 1. Basic case: x * n is an integer.
# 2. x * n is not an integer.
# 3. Simple fractions.
# 4. Fractions with larger numbers.
# 5. Cases where the denominator of x is a factor of the denominator of n.
# 6. Cases where the denominator of x is not a factor of the denominator of n.

### STEP 3: CODE
def test_simplify_basic_integer():
    assert simplify("1/5", "5/1") == True

def test_simplify_basic_non_integer():
    assert simplify("1/6", "2/1") == False

def test_simplify_complex_integer():
    assert simplify("7/10", "10/2") == False

def test_simplify_simple_fractions():
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("3/4", "4/1") == True

def test_simplify_complex_fractions():
    assert simplify("1/2", "3/4") == False
    assert simplify("2/3", "4/5") == False
    assert simplify("5/6", "10/1") == False

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("100/10", "11/1") == False

def test_simplify_denominator_factor():
    assert simplify("1/2", "2/2") == True
    assert simplify("2/3", "3/3") == True

def test_simplify_denominator_not_factor():
    assert simplify("1/2", "3/4") == False
    assert simplify("2/3", "5/6") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/1", "1/1") == True