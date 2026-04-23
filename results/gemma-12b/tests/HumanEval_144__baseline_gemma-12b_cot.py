
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

    num = num_x * num_n
    den = den_x * den_n

    return num % den == 0

class TestSimplify:
    def test_whole_number_result(self):
        assert simplify("1/5", "5/1") == True

    def test_non_whole_number_result(self):
        assert simplify("1/6", "2/1") == False

    def test_another_non_whole_number_result(self):
        assert simplify("7/10", "10/2") == False

    def test_simple_whole_number(self):
        assert simplify("1/1", "1/1") == True

    def test_larger_numbers_whole(self):
        assert simplify("4/6", "3/2") == True

    def test_larger_numbers_not_whole(self):
        assert simplify("4/7", "7/3") == False

    def test_one_is_one(self):
        assert simplify("1/2", "1/1") == False

    def test_one_is_two(self):
        assert simplify("1/3", "2/1") == False

    def test_edge_case_1(self):
        assert simplify("2/3", "3/2") == True

    def test_edge_case_2(self):
        assert simplify("1/4", "4/1") == True

    def test_edge_case_3(self):
        assert simplify("3/4", "4/3") == False

    def test_large_numbers_whole(self):
        assert simplify("12/18", "18/12") == True

    def test_large_numbers_not_whole(self):
        assert simplify("13/18", "18/12") == False