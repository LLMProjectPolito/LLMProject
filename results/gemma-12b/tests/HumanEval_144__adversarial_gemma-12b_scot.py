
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
        num, den = map(int, fraction.split('/'))
        return num / den

    x_float = fraction_to_float(x)
    n_float = fraction_to_float(n)
    product = x_float * n_float
    return product.is_integer()


class TestSimplify:
    def test_whole_number_result(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("2/4", "4/1") == True
        assert simplify("3/6", "6/3") == True

    def test_non_whole_number_result(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/3", "2/1") == False

    def test_edge_case_one(self):
        assert simplify("1/1", "1/1") == True

    def test_large_numbers_whole(self):
        assert simplify("12/4", "4/3") == True
        assert simplify("24/8", "8/6") == True

    def test_large_numbers_non_whole(self):
        assert simplify("3/7", "7/2") == False
        assert simplify("5/9", "9/4") == False