
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

    product_num = num_x * num_n
    product_den = den_x * den_n

    if product_num % product_den == 0:
        return True
    else:
        return False

class TestSimplify:

    def test_simplify_1(self):
        assert simplify("1/5", "5/1") == True

    def test_simplify_2(self):
        assert simplify("1/6", "2/1") == False

    def test_simplify_3(self):
        assert simplify("7/10", "10/2") == False

    def test_simplify_4(self):
        assert simplify("2/3", "6/1") == True

    def test_simplify_5(self):
        assert simplify("4/7", "14/1") == False

    def test_simplify_6(self):
        assert simplify("10/1", "5/1") == True

    def test_simplify_7(self):
        assert simplify("1/1", "1/1") == True

    def test_simplify_8(self):
        assert simplify("100/10", "10/1") == True

    def test_simplify_9(self):
        assert simplify("12/18", "6/1") == True

    def test_simplify_10(self):
        assert simplify("5/2", "10/2") == False