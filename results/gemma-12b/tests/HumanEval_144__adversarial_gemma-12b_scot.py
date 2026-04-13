
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
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))

    product = (num_x / den_x) * (num_n / den_n)

    return product.is_integer()


class TestSimplify:
    def test_whole_number_result(self):
        assert simplify("1/2", "2/1") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("2/4", "2/1") == True
        assert simplify("7/10", "10/7") == True
        assert simplify("1/1", "1/1") == True

    def test_non_whole_number_result(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("1/3", "1/2") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/5", "2/3") == False

    def test_edge_cases(self):
        assert simplify("1/1", "1/2") == False
        assert simplify("2/1", "1/1") == True
        assert simplify("1/2", "1/1") == False

    def test_larger_numbers(self):
        assert simplify("12/15", "15/12") == True
        assert simplify("25/30", "30/25") == True
        assert simplify("100/200", "200/100") == True
        assert simplify("101/200", "200/101") == False

    def test_simplification(self):
        assert simplify("2/4", "4/2") == True
        assert simplify("3/6", "6/3") == True
        assert simplify("4/8", "8/4") == True
        assert simplify("5/10", "10/5") == True