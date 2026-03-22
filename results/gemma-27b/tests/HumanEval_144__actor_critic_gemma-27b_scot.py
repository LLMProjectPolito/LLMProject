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


def test_simplify_valid_whole():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/1", "1/4") == True

def test_simplify_invalid_whole():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False

def test_simplify_large_numbers():
    assert simplify("100/1", "1/100") == True
    assert simplify("1000/1", "1/1000") == True
    assert simplify("100/2", "2/100") == True
    assert simplify("123456789/1", "1/123456789") == True  # Added large number test

def test_simplify_large_whole():
    assert simplify("1000/1", "1000/1") == True

def test_simplify_zero_numerator():
    assert simplify("0/5", "5/1") == True
    assert simplify("5/1", "0/2") == True
    assert simplify("0/1", "0/1") == True

def test_simplify_invalid_input():
    with pytest.raises(TypeError):
        simplify("1a/2", "2/1")
    with pytest.raises(TypeError):
        simplify("1/2", "2b/1")

def test_simplify_positive_numbers():
    with pytest.raises(TypeError):
        simplify("-1/2", "2/1")
    with pytest.raises(TypeError):
        simplify("1/2", "-2/1")
    with pytest.raises(TypeError):
        simplify("1/-2", "2/1")
    with pytest.raises(TypeError):
        simplify("1/2", "2/-1")