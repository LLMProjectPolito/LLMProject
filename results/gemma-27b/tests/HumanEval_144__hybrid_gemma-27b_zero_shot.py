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
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    result_num = x_num * n_num
    result_den = x_den * n_den
    return result_num % result_den == 0

def test_simplify_true_case1():
    assert simplify("1/5", "5/1") == True

def test_simplify_false_case1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_case2():
    assert simplify("7/10", "10/2") == False

def test_simplify_true_case2():
    assert simplify("2/3", "3/1") == True

def test_simplify_true_case3():
    assert simplify("4/5", "5/4") == True

def test_simplify_false_case3():
    assert simplify("1/2", "1/3") == False

def test_simplify_large_numbers_true():
    assert simplify("100/20", "2/1") == True

def test_simplify_large_numbers_false():
    assert simplify("100/21", "2/1") == False

def test_simplify_same_fraction():
    assert simplify("2/2", "2/2") == True

def test_simplify_one_whole_number():
    assert simplify("1/1", "2/1") == True

def test_simplify_another_whole_number():
    assert simplify("2/1", "1/1") == True

def test_simplify_complex_true():
    assert simplify("15/4", "8/5") == True

def test_simplify_complex_false():
    assert simplify("15/4", "7/5") == False

def test_simplify_with_larger_denominators():
    assert simplify("1/100", "100/1") == True

def test_simplify_with_larger_denominators_false():
    assert simplify("1/101", "100/1") == False

def test_simplify_edge_case_1():
    assert simplify("1/2", "2/4") == True

def test_simplify_edge_case_2():
    assert simplify("3/4", "4/3") == True

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/5", "5/1", True),
        ("1/6", "2/1", False),
        ("7/10", "10/2", False),
        ("1/2", "2/1", True),
        ("3/4", "4/3", True),
        ("2/3", "3/2", True),
        ("1/1", "1/1", True),
        ("5/1", "1/5", True),
        ("2/5", "5/2", True),
        ("1/3", "3/1", True),
        ("1/4", "4/1", True),
        ("1/7", "7/1", True),
        ("1/8", "8/1", True),
        ("1/9", "9/1", True),
        ("1/10", "10/1", True),
        ("2/7", "7/2", True),
        ("3/8", "8/3", True),
        ("4/9", "9/4", True),
        ("5/11", "11/5", True),
        ("1/2", "3/4", False),
        ("2/3", "1/2", False),
        ("3/5", "2/3", False),
        ("4/7", "1/2", False),
        ("5/9", "3/5", False),
        ("1/10", "1/3", False),
        ("7/8", "1/2", False),
        ("9/10", "1/3", False),
        ("11/12", "1/2", False),
        ("13/15", "1/3", False),
        ("1/1", "2/1", True),
        ("2/1", "1/1", True),
        ("1/1", "3/1", True),
        ("3/1", "1/1", True),
        ("10/1", "1/10", True),
        ("1/10", "10/1", True),
        ("12/5", "5/12", True),
        ("1/12", "12/1", True),
        ("12/1", "1/12", True),
        ("1/2", "1/3", False),
        ("1/3", "1/2", False),
        ("2/3", "1/4", False),
        ("3/4", "1/5", False),
        ("4/5", "1/6", False),
        ("5/6", "1/7", False),
        ("1/100", "100/1", True),
        ("100/1", "1/100", True),
        ("10/20", "20/10", True),
        ("20/10", "10/20", True),
        ("100/2", "1/50", True),
        ("1/50", "100/2", True),
        ("100/2", "50/1", True),
        ("50/1", "100/2", True),
    ],
)
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected