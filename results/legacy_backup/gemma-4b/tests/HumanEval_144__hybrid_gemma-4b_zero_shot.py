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
    
    return product_num % product_den == 0

class TestSimplify:

    def test_simple_true(self):
        assert simplify("1/5", "5/1") == True

    def test_simple_false(self):
        assert simplify("1/6", "2/1") == False

    def test_complex_true(self):
        assert simplify("7/10", "10/2") == False

    def test_large_numbers_true(self):
        assert simplify("100/10", "10/1") == True

    def test_large_numbers_false(self):
        assert simplify("100/10", "11/1") == False

    def test_equal_numerator(self):
        assert simplify("5/5", "5/1") == True

    def test_equal_denominator(self):
        assert simplify("1/1", "5/5") == True

    def test_one_over_one(self):
        assert simplify("1/1", "1/1") == True

    def test_one_over_two(self):
        assert simplify("1/1", "2/1") == False

    def test_fraction_with_one_numerator(self):
        assert simplify("1/3", "1/1") == True

    def test_fraction_with_one_denominator(self):
        assert simplify("3/1", "1/1") == True

    def test_zero_denominator_should_fail(self):
        with pytest.raises(ZeroDivisionError):
            simplify("1/0", "1/1")

    def test_zero_numerator_should_fail(self):
        with pytest.raises(ZeroDivisionError):
            simplify("0/1", "1/1")

    def test_negative_numbers_should_fail(self):
        assert simplify("1/2", "2/1") == False

    def test_negative_numbers_complex(self):
        assert simplify("-1/2", "2/1") == False

    def test_fraction_with_large_numbers(self):
        assert simplify("12345/67890", "67890/1") == True

    def test_fraction_with_large_numbers_false(self):
        assert simplify("12345/67890", "67891/1") == False