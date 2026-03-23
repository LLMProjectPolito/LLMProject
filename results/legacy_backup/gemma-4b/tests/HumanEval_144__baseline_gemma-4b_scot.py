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
# 1. Basic positive integer fractions that result in an integer product.
# 2. Basic positive integer fractions that result in a non-integer product.
# 3. Fractions with larger numerators and denominators.
# 4. Edge cases: x = "1/1", n = "1/1"
# 5. Edge cases: x = "1/2", n = "2/1"
# 6. Edge cases: x = "1/2", n = "3/1"

### STEP 3: CODE
def test_simplify_integer_fractions_integer_product():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("5/1", "1/5") == True

def test_simplify_integer_fractions_non_integer_product():
    assert simplify("1/2", "2/1") == False
    assert simplify("1/3", "3/1") == False
    assert simplify("1/5", "5/1") == False
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False

def test_simplify_larger_fractions_integer_product():
    assert simplify("10/2", "2/1") == True
    assert simplify("12/3", "3/1") == True
    assert simplify("25/5", "5/1") == True

def test_simplify_larger_fractions_non_integer_product():
    assert simplify("10/3", "3/1") == False
    assert simplify("12/4", "4/1") == False
    assert simplify("25/6", "6/1") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/2", "3/1") == False

def test_simplify_complex_fractions_integer_product():
    assert simplify("3/4", "4/3") == True
    assert simplify("6/8", "8/6") == True

def test_simplify_complex_fractions_non_integer_product():
    assert simplify("3/4", "4/2") == False
    assert simplify("6/8", "8/3") == False