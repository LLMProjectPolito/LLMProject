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
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    result_num = x_num * n_num
    result_den = x_den * n_den

    return result_num % result_den == 0

# STEP 1: REASONING
# The function `simplify` takes two string fractions as input and determines if their product is a whole number.
# We need to test various scenarios:
# - Whole number results (True cases)
# - Non-whole number results (False cases)
# - Fractions that simplify to whole numbers after multiplication
# - Edge cases with small numerators/denominators (e.g., 1/1, 1/2)
# - Cases where the result is a large number.

# STEP 2: PLAN
# Test function names and scenarios:
# - test_whole_number_result: Tests cases where the product is a whole number.
# - test_non_whole_number_result: Tests cases where the product is not a whole number.
# - test_simplifying_fraction: Tests cases where the fraction simplifies to a whole number after multiplication.
# - test_edge_cases: Tests edge cases with small numerators/denominators.
# - test_large_numbers: Tests cases with larger numbers to ensure no overflow issues.
# - test_one_over_one: Tests the case where both fractions are 1/1.
# - test_fraction_times_whole: Tests a fraction multiplied by a whole number represented as a fraction.

# STEP 3: CODE
def test_whole_number_result():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/1", "1/4") == True
    assert simplify("1/1", "1/1") == True

def test_non_whole_number_result():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "1/2") == False
    assert simplify("2/5", "1/3") == False

def test_simplifying_fraction():
    assert simplify("2/4", "4/2") == True
    assert simplify("3/6", "6/3") == True
    assert simplify("5/10", "10/5") == True

def test_edge_cases():
    assert simplify("1/1", "1/2") == False
    assert simplify("1/2", "1/1") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("2/1", "1/2") == True

def test_large_numbers():
    assert simplify("100/1", "1/100") == True
    assert simplify("1000/1", "1/1000") == True
    assert simplify("10000/1", "1/10000") == True
    assert simplify("100/2", "2/100") == True

def test_one_over_one():
    assert simplify("1/1", "1/1") == True

def test_fraction_times_whole():
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("3/4", "4/1") == True