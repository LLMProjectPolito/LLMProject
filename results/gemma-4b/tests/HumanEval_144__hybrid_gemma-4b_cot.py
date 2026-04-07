
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

    def test_basic_true(self):
        assert simplify("1/5", "5/1") == True

    def test_basic_false(self):
        assert simplify("1/6", "2/1") == False

    def test_basic_false_2(self):
        assert simplify("7/10", "10/2") == False

    def test_large_numbers_true(self):
        assert simplify("100/10", "10/1") == True

    def test_large_numbers_false(self):
        assert simplify("100/10", "11/1") == False

    def test_equal_numbers_true(self):
        assert simplify("5/5", "5/5") == True

    def test_equal_numbers_false(self):
        assert simplify("5/5", "6/5") == False

    def test_numerator_one(self):
        assert simplify("1/2", "2/1") == True

    def test_denominator_one(self):
        assert simplify("1/2", "1/1") == True

    def test_numerator_and_denominator_one(self):
        assert simplify("1/1", "1/1") == True

    def test_numerator_and_denominator_equal(self):
        assert simplify("2/2", "2/2") == True

    def test_numerator_greater_than_denominator(self):
        assert simplify("3/2", "2/1") == False

    def test_numerator_equal_denominator(self):
        assert simplify("3/3", "3/3") == True

    def test_complex_fraction_true(self):
        assert simplify("2/3", "3/2") == True

    def test_complex_fraction_false(self):
        assert simplify("2/3", "4/1") == False

    def test_zero_denominator(self):
        with pytest.raises(ZeroDivisionError):
            simplify("1/0", "1/1")

def test_simplify_valid():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("10/3", "3/2") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_invalid():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/4") == False
    assert simplify("1/2", "3/1") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/2") == False
    assert simplify("1/2", "1/1") == True
    assert simplify("1/1", "2/1") == True
    assert simplify("2/1", "1/1") == True

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("100/10", "11/1") == False
    assert simplify("12345/10", "10/1") == False

def test_simplify_equal_fractions():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "2/2") == True
    assert simplify("3/3", "3/3") == True

def test_simplify_different_order():
    assert simplify("5/1", "1/5") == True
    assert simplify("10/2", "2/10") == True