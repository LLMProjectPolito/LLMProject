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

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `simplify` takes two fractions as strings, `x` and `n`, and returns `True` if their product is an integer, and `False` otherwise.
# The fractions are in the format "numerator/denominator". The numerator and denominator are positive integers.
# The function should handle cases where the product is an integer and cases where it is not.
# The function should handle different denominators.

# STEP 2: PLAN - List test functions names and scenarios.
# test_simplify_integer_result
# test_simplify_non_integer_result
# test_simplify_simple_fractions
# test_simplify_larger_fractions
# test_simplify_edge_cases

# STEP 3: CODE - Write the high-quality pytest suite.
def test_simplify_integer_result():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "3/3") == True
    assert simplify("10/5", "2/1") == True

def test_simplify_non_integer_result():
    assert simplify("1/2", "2/1") == False
    assert simplify("1/3", "2/1") == False
    assert simplify("7/10", "10/2") == False

def test_simplify_simple_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False

def test_simplify_larger_fractions():
    assert simplify("12/16", "16/8") == True
    assert simplify("12/16", "16/9") == False
    assert simplify("100/100", "101/1") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/2") == False
    assert simplify("1/2", "1/1") == False
    assert simplify("1000/1000", "1001/1") == False