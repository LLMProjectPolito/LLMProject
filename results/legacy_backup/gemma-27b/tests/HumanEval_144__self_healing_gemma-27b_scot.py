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
# We need to test various scenarios, including:
# - Fractions that result in a whole number when multiplied.
# - Fractions that do not result in a whole number when multiplied.
# - Fractions with different numerators and denominators.
# - Edge cases like fractions equal to 1.
# - Cases where the result is a large number.

# STEP 2: PLAN
# Test function names and scenarios:
# - test_simplify_whole_number: Tests fractions that result in a whole number.
# - test_simplify_not_whole_number: Tests fractions that do not result in a whole number.
# - test_simplify_one: Tests fractions equal to 1.
# - test_simplify_large_numbers: Tests fractions with large numerators and denominators.
# - test_simplify_simple_fractions: Tests simple fractions like 1/2, 1/3, etc.
# - test_simplify_equal_fractions: Tests when x and n are the same fraction.

# STEP 3: CODE
def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/1", "1/4") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "1/2") == False
    assert simplify("2/5", "5/3") == False

def test_simplify_one():
    assert simplify("1/1", "2/2") == True
    assert simplify("2/2", "1/1") == True
    assert simplify("3/3", "4/4") == True

def test_simplify_large_numbers():
    assert simplify("100/2", "2/1") == True
    assert simplify("1000/3", "3/1") == True
    assert simplify("1000/7", "7/1") == True
    assert simplify("1000/11", "11/1") == True

def test_simplify_simple_fractions():
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/2", "1/2") == True

def test_simplify_equal_fractions():
    assert simplify("2/3", "2/3") == True
    assert simplify("5/7", "5/7") == True
    assert simplify("10/11", "10/11") == True

def test_simplify_mixed_cases():
    assert simplify("3/4", "8/3") == False
    assert simplify("5/6", "6/5") == True
    assert simplify("7/8", "8/7") == True
    assert simplify("9/10", "10/9") == True