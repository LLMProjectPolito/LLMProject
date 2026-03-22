def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") == False
    """
    def fraction_to_float(fraction):
        num, den = map(int, fraction.split('/'))
        return num / den

    float_x = fraction_to_float(x)
    float_n = fraction_to_float(n)

    product = float_x * float_n

    return product.is_integer()


def test_simplify_basic_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_basic_false():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_false():
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

def test_simplify_zero_numerator():
    assert simplify("0/1", "1/1") == True

def test_simplify_zero_numerator_false():
    assert simplify("0/1", "1/2") == True

def test_simplify_complex_fractions_true():
    assert simplify("2/4", "4/2") == True

def test_simplify_complex_fractions_false():
    assert simplify("2/5", "5/3") == False