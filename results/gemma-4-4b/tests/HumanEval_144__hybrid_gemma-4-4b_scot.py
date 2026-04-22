
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
    def fraction_to_float(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator / denominator

    x_float = fraction_to_float(x)
    n_float = fraction_to_float(n)
    product = x_float * n_float
    return product == int(product)

class TestSimplify:
    def test_simplify_true_case1(self):
        assert simplify("1/5", "5/1") == True

    def test_simplify_false_case1(self):
        assert simplify("1/6", "2/1") == False

    def test_simplify_false_case2(self):
        assert simplify("7/10", "10/2") == False

    def test_simplify_true_case2(self):
        assert simplify("2/3", "3/2") == True

    def test_simplify_true_case3(self):
        assert simplify("1/2", "2/1") == True

    def test_simplify_false_case3(self):
        assert simplify("1/3", "2/5") == False

    def test_simplify_large_numbers(self):
        assert simplify("100/2", "2/5") == True

    def test_simplify_small_numbers(self):
        assert simplify("1/100", "100/1") == True

    def test_simplify_equal_fractions(self):
        assert simplify("1/1", "1/1") == True

    def test_simplify_different_denominators(self):
        assert simplify("2/7", "7/2") == True

    def test_simplify_complex_fractions(self):
        assert simplify("3/4", "4/3") == True

    def test_simplify_another_true_case(self):
        assert simplify("4/5", "5/4") == True

    def test_simplify_another_false_case(self):
        assert simplify("1/8", "3/4") == False