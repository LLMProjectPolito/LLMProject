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

    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a

    common_divisor = gcd(num, den)
    simplified_num = num // common_divisor
    simplified_den = den // common_divisor

    return simplified_den == 1


class TestSimplify:
    def test_whole_number_result(self):
        assert simplify("1/2", "2/1") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("2/5", "5/2") == True

    def test_non_whole_result_different(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/4", "1/2") == False

    def test_denominator_one(self):
        assert simplify("1/1", "2/1") == True
        assert simplify("2/1", "1/1") == True
        assert simplify("1/1", "1/1") == True
        assert simplify("2/1", "3/1") == False
        assert simplify("1/1", "5/1") == True
        assert simplify("3/1", "1/1") == True
        assert simplify("1/1", "4/1") == False

    def test_zero_numerator_result(self):
        assert simplify("0/1", "1/1") == True
        assert simplify("1/1", "0/1") == True
        assert simplify("0/2", "2/3") == False
        assert simplify("0/5", "5/1") == True

    def test_large_denominators(self):
        assert simplify("1/1000000", "1000000/1") == True
        assert simplify("1/1000001", "1000001/1") == False

    def test_same_fraction(self):
        assert simplify("1/2", "1/2") == True
        assert simplify("2/3", "2/3") == True
        assert simplify("1/4", "1/4") == True
        assert simplify("3/5", "3/5") == True

    def test_one_over_one(self):
        assert simplify("1/1", "2/3") == False
        assert simplify("1/1", "3/4") == False
        assert simplify("1/1", "5/6") == False
        assert simplify("1/1", "7/8") == False
        assert simplify("1/1", "1/2") == True
        assert simplify("1/1", "1/3") == True

    def test_negative_cases(self):
        assert simplify("1/3", "2/5") == False
        assert simplify("2/7", "3/5") == False
        assert simplify("1/2", "1/3") == False

    def test_even_odd_combinations(self):
        assert simplify("2/3", "3/4") == False
        assert simplify("4/5", "5/6") == False
        assert simplify("6/7", "7/8") == False
        assert simplify("8/9", "9/10") == False