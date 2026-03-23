# STEP 1: REASONING
# The function `simplify(x, n)` takes two string representations of fractions, x and n,
# and returns True if their product is a whole number, and False otherwise.
# The fractions are in the format "<numerator>/<denominator>".
# The core logic involves converting the fractions to their numerical values,
# multiplying them, and checking if the result is an integer.
# We need to test various scenarios, including:
# 1. Simple fractions that result in whole numbers.
# 2. Fractions that result in non-whole numbers.
# 3. Fractions with denominators of 1.
# 4. Fractions with large numerators and denominators.
# 5. Edge cases (though the prompt states that invalid inputs are not expected).

# STEP 2: PLAN
# Test functions:
# - test_simplify_whole_number: Tests cases where the product is a whole number.
# - test_simplify_non_whole_number: Tests cases where the product is not a whole number.
# - test_simplify_denominator_one: Tests cases where one or both denominators are 1.
# - test_simplify_large_numbers: Tests cases with larger numerators and denominators.

# STEP 3: CODE
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
    return product == int(product)


class TestSimplify:
    def test_simplify_whole_number(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("2/4", "2/2") == True
        assert simplify("3/3", "1/1") == True
        assert simplify("1/1", "5/5") == True

    def test_simplify_non_whole_number(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/2", "1/3") == False
        assert simplify("2/5", "3/7") == False

    def test_simplify_denominator_one(self):
        assert simplify("1/1", "2/1") == True
        assert simplify("2/1", "1/1") == True
        assert simplify("1/1", "3/1") == True
        assert simplify("4/1", "1/1") == True
        assert simplify("1/2", "1/1") == False
        assert simplify("1/1", "1/2") == False

    def test_simplify_large_numbers(self):
        assert simplify("12345/67890", "67890/12345") == True
        assert simplify("12345/67890", "1/2") == False
        assert simplify("1000/1000", "2000/2000") == True
        assert simplify("1000/1001", "1001/1000") == False