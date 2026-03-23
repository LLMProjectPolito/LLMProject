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
# It needs to handle different cases where the numerator and denominator of the fractions are different.
# The function should return True if the product is an integer and False otherwise.
# The input strings are expected to be in the format "numerator/denominator".

### STEP 2: PLAN
# Test cases:
# 1. Basic case where the product is an integer.
# 2. Basic case where the product is not an integer.
# 3. Different numerators and denominators.
# 4. Edge cases (e.g., simple fractions).
# 5. Cases where the denominator is 1.
# 6. Cases where the numerator is 1.

### STEP 3: CODE
def test_simplify_basic_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_basic_false():
    assert simplify("1/6", "2/1") == False

def test_simplify_different_numbers():
    assert simplify("7/10", "10/2") == False

def test_simplify_numerator_one():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "6/1") == True

def test_simplify_denominator_one():
    assert simplify("5/1", "1/5") == True
    assert simplify("6/1", "1/6") == True

def test_simplify_complex_true():
    assert simplify("2/3", "3/2") == True

def test_simplify_complex_false():
    assert simplify("2/3", "4/5") == False

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True

def test_simplify_large_numbers_false():
    assert simplify("100/10", "11/1") == False

def test_simplify_edge_case():
    assert simplify("1/1", "1/1") == True

def test_simplify_edge_case_2():
    assert simplify("2/2", "2/2") == True

def test_simplify_edge_case_3():
    assert simplify("3/2", "2/3") == True

def test_simplify_edge_case_4():
    assert simplify("3/2", "3/2") == True