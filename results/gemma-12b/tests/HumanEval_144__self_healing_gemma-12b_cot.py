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
        assert simplify("2/3", "3/2") == True
        assert simplify("1/2", "2/1") == True
        assert simplify("1/1", "1/1") == True
        assert simplify("4/2", "2/4") == True
        assert simplify("1/7", "7/1") == True

    def test_non_whole_number_result(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/3", "2/5") == False
        assert simplify("2/5", "3/7") == False
        assert simplify("1/4", "3/5") == False

    def test_large_numbers(self):
        assert simplify("100/2", "2/100") == True
        assert simplify("100/3", "3/100") == True
        assert simplify("1000/7", "7/1000") == True
        assert simplify("100/11", "11/100") == True

    def test_edge_cases(self):
        assert simplify("1/1", "1/1") == True
        assert simplify("1/2", "1/2") == False
        assert simplify("2/1", "1/2") == False
        assert simplify("1/1000", "1000/1") == True
        assert simplify("1000/1", "1/1000") == False

    def test_mixed_numbers(self):
        assert simplify("1/2", "3/4") == False
        assert simplify("2/3", "1/2") == False
        assert simplify("3/4", "1/2") == False