
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

def test_simplify_true_case1():
    assert simplify("1/5", "5/1") == True

def test_simplify_false_case1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_case2():
    assert simplify("7/10", "10/2") == False

def test_simplify_true_case2():
    assert simplify("2/3", "3/2") == True

def test_simplify_true_case3():
    assert simplify("1/1", "1/1") == True

def test_simplify_false_case3():
    assert simplify("1/2", "1/3") == False

def test_simplify_with_larger_numbers_true():
    assert simplify("12/4", "3/1") == True

def test_simplify_with_larger_numbers_false():
    assert simplify("15/4", "2/1") == False

def test_simplify_different_denominators_true():
    assert simplify("2/6", "3/1") == False

def test_simplify_different_denominators_false():
    assert simplify("4/5", "5/6") == False