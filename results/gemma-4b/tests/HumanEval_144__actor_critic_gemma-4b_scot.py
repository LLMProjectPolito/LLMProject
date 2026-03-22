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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `simplify` takes two fractions (strings) as input and returns True if their product is a whole number, and False otherwise.
# The input fractions are in the format "numerator/denominator". The function should handle cases where the product is an integer and also cases where it is not.
# Edge cases include:
# 1. Simple multiplication where the result is an integer.
# 2. Simple multiplication where the result is not an integer.
# 3. Fractions with different denominators.
# 4. Fractions where the numerator and denominator are 1.
# 5. Fractions where the numerator and denominator are large.

# STEP 2: PLAN - List test functions names and scenarios.
# test_simplify_integer_result
# test_simplify_non_integer_result
# test_simplify_fraction_with_one
# test_simplify_different_denominators
# test_simplify_large_numbers
# test_simplify_edge_case_1
# test_simplify_edge_case_2
# test_simplify_negative_input

# STEP 3: CODE - Write the high-quality pytest suite.
def test_simplify_integer_result():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/7", "7/4") == True

def test_simplify_non_integer_result():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "5/2") == False

def test_simplify_fraction_with_one():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "1/1") == True
    assert simplify("2/1", "1/1") == True

def test_simplify_different_denominators():
    assert simplify("1/2", "2/3") == False
    assert simplify("3/4", "4/5") == False
    assert simplify("5/6", "6/7") == False

def test_simplify_large_numbers():
    assert simplify("1000/1001", "1001/1000") == True
    assert simplify("12345/67890", "67890/12345") == False

def test_simplify_edge_case_1():
    assert simplify("1/1", "1/1") == True

def test_simplify_edge_case_2():
    assert simplify("1/2", "2/1") == False

def test_simplify_negative_input():
    assert simplify("1/2", "-2/1") == False
    assert simplify("-1/2", "2/1") == False