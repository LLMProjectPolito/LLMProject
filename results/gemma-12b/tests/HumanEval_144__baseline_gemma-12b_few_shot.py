
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

def test_simplify_basic_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_basic_false():
    assert simplify("1/6", "2/1") == False

def test_simplify_fraction_false():
    assert simplify("7/10", "10/2") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "1/2") == True

def test_simplify_one_is_one():
    assert simplify("1/1", "2/3") == False
    assert simplify("2/3", "1/1") == False

def test_simplify_large_numbers_true():
    assert simplify("100/200", "200/100") == True

def test_simplify_large_numbers_false():
    assert simplify("100/201", "201/100") == False

def test_simplify_decimal_result_false():
    assert simplify("1/3", "2/1") == False

def test_simplify_zero_numerator_true():
    assert simplify("0/1", "1/1") == True
    assert simplify("1/1", "0/1") == True

def test_simplify_zero_numerator_false():
    assert simplify("0/1", "1/2") == False
    assert simplify("1/2", "0/1") == False

def test_simplify_complex_fractions_true():
    assert simplify("2/4", "4/2") == True

def test_simplify_complex_fractions_false():
    assert simplify("2/5", "3/4") == False