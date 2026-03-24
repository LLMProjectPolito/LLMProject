from fractions import Fraction

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
    x_frac = Fraction(x)
    n_frac = Fraction(n)

    result = x_frac * n_frac
    return result.denominator == 1

### Tests (Pytest):
def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("2/4", "4/2") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False

def test_simplify_gcd_simplification():
    assert simplify("2/4", "3/6") == True  # Tests GCD simplification
    assert simplify("4/6", "3/9") == True  # More GCD simplification
    assert simplify("2/3", "3/4") == False

def test_simplify_equal_fractions():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "2/2") == True
    assert simplify("3/3", "1/1") == True

def test_simplify_multiplication_required():
    assert simplify("4/2", "3/1") == True
    assert simplify("6/3", "2/1") == True
    assert simplify("2/3", "6/1") == True

def test_simplify_large_prime_numbers():
    assert simplify("7/11", "11/7") == True
    assert simplify("13/17", "17/13") == True
    assert simplify("7/11", "12/7") == False

def test_simplify_complex_fractions():
    assert simplify("12/15", "25/10") == False
    assert simplify("12/15", "15/10") == True

def test_simplify_large_numbers():
    assert simplify("1000/2", "2/1") == True
    assert simplify("1000/3", "2/1") == False