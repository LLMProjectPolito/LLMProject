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
    
    return product_num % product_den == 0

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `simplify` checks if the product of two fractions, represented as strings, is a whole number.
# It needs to handle string splitting, integer conversion, and modulo operation.
# The input strings are guaranteed to be valid fractions with positive integer numerators and denominators.
# The function should return True if the product is a whole number and False otherwise.

# STEP 2: PLAN - List test functions names and scenarios.
# test_simplify_true_cases: Tests cases where the product is a whole number.
# test_simplify_false_cases: Tests cases where the product is not a whole number.
# test_simplify_edge_cases: Tests edge cases like simple fractions and larger numbers.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_simplify_true_cases():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("10/2", "2/1") == True
    assert simplify("100/5", "5/1") == True

def test_simplify_false_cases():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "3/1") == False
    assert simplify("1/3", "4/1") == False
    assert simplify("10/3", "3/1") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/1", "1/1") == True
    assert simplify("1000/1", "1/1") == True
    assert simplify("1/1000", "1/1") == False