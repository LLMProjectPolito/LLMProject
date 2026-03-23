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
        assert simplify("1/2", "2/2") == True

    def test_simplify_9(self):
        assert simplify("3/4", "12/1") == True

    def test_simplify_10(self):
        assert simplify("5/8", "40/1") == True

    def test_simplify_11(self):
        assert simplify("9/11", "99/1") == True

    def test_simplify_12(self):
        assert simplify("1/3", "9/1") == False

    def test_simplify_13(self):
        assert simplify("2/5", "10/1") == True

    def test_simplify_14(self):
        assert simplify("1/7", "7/1") == True

    def test_simplify_15(self):
        assert simplify("3/5", "15/1") == True

    def test_simplify_16(self):
        assert simplify("4/9", "36/1") == True

    def test_simplify_17(self):
        assert simplify("5/11", "55/1") == True

    def test_simplify_18(self):
        assert simplify("6/13", "78/1") == False

    def test_simplify_19(self):
        assert simplify("7/14", "14/2") == True

    def test_simplify_20(self):
        assert simplify("8/15", "120/1") == True