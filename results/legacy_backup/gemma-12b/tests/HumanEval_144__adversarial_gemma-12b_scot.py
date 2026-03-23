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
        assert simplify("1/2", "2/1") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("2/5", "5/2") == True
        assert simplify("3/4", "4/3") == True

    def test_non_whole_number_result(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/5", "2/3") == False
        assert simplify("2/7", "3/5") == False

    def test_fraction_equals_one(self):
        assert simplify("1/1", "1/1") == True
        assert simplify("2/2", "3/3") == True
        assert simplify("4/4", "5/5") == True

    def test_fraction_equals_zero(self):
        assert simplify("0/1", "1/1") == True
        assert simplify("1/1", "0/1") == True
        assert simplify("0/2", "2/3") == True

    def test_large_numbers(self):
        assert simplify("123/456", "456/123") == True
        assert simplify("100/200", "300/100") == True
        assert simplify("1000/2000", "3000/1000") == True
        assert simplify("1234/5678", "9012/3456") == False

    def test_mixed_numbers(self):
        assert simplify("1/2", "3/4") == False
        assert simplify("2/3", "1/2") == False
        assert simplify("1/4", "5/2") == False
        assert simplify("3/5", "2/3") == False