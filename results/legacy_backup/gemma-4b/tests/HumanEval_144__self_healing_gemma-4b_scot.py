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
# STEP 1: REASONING - The function `simplify` checks if the product of two fractions `x` and `n` is a whole number. It splits the input strings into numerator and denominator, converts them to integers, calculates the product, and then checks if the product is an integer using `is_integer()`. The function should handle various cases, including simple multiplications and cases where the product is not an integer.

# STEP 2: PLAN -
# Test cases:
# 1. Simple multiplication resulting in an integer.
# 2. Simple multiplication resulting in a non-integer.
# 3. Different denominators.
# 4. Larger numbers.
# 5. Edge cases (e.g., small numbers).

# Test functions:
# test_simple_integer
# test_simple_non_integer
# test_different_denominators
# test_larger_numbers
# test_edge_cases

# STEP 3: CODE -
def test_simple_integer():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "6/1") == True
    assert simplify("1/2", "2/1") == True

def test_simple_non_integer():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "5/1") == False

def test_different_denominators():
    assert simplify("1/2", "3/4") == False
    assert simplify("2/5", "7/10") == False
    assert simplify("1/3", "4/5") == False

def test_larger_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("123/45", "67/89") == False
    assert simplify("1000/100", "10/1") == True

def test_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/1", "1/1") == True
    assert simplify("1/1", "1/2") == False