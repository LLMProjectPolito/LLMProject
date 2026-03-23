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

    num = num_x * num_n
    den = den_x * den_n

    return num % den == 0

class TestSimplify:
    def test_basic_true(self):
        assert simplify("1/5", "5/1") == True

    def test_basic_false(self):
        assert simplify("1/6", "2/1") == False

    def test_another_false(self):
        assert simplify("7/10", "10/2") == False

    def test_whole_numbers(self):
        assert simplify("1/1", "1/1") == True

    def test_larger_numbers_true(self):
        assert simplify("2/3", "3/2") == True

    def test_larger_numbers_false(self):
        assert simplify("2/3", "3/4") == False

    def test_mixed_numbers_true(self):
        assert simplify("1/2", "2/1") == True

    def test_mixed_numbers_false(self):
        assert simplify("1/3", "2/1") == False

    def test_same_numerator_different_denominator_true(self):
        assert simplify("2/4", "4/2") == True

    def test_same_denominator_different_numerator_false(self):
        assert simplify("2/4", "3/4") == False

    def test_complex_fractions_true(self):
        assert simplify("3/7", "14/3") == True

    def test_complex_fractions_false(self):
        assert simplify("3/7", "14/5") == False

    def test_edge_case_1(self):
        assert simplify("1/100", "100/1") == True

    def test_edge_case_2(self):
        assert simplify("1/101", "101/1") == True

    def test_edge_case_3(self):
        assert simplify("1/101", "100/1") == False