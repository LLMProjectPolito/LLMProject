
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
from sympy import Rational

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
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    result = Rational(num1, den1) * Rational(num2, den2)
    return result.is_integer()

@pytest.fixture
def valid_fractions():
    yield ("1/5", "5/1")

@pytest.fixture
def invalid_fractions():
    yield ("1/6", "2/1")

@pytest.fixture
def another_invalid_fractions():
    yield ("7/10", "10/2")

def test_valid_fractions(valid_fractions):
    assert simplify(*valid_fractions) == True

def test_invalid_fractions(invalid_fractions):
    assert simplify(*invalid_fractions) == False

def test_another_invalid_fractions(another_invalid_fractions):
    assert simplify(*another_invalid_fractions) == False

def test_simple_valid(capsys):
    assert simplify("1/2", "2/1") == True
    captured = capsys.readouterr()
    assert captured.err == ""

def test_simple_invalid(capsys):
    assert simplify("1/3", "2/1") == False
    captured = capsys.readouterr()
    assert captured.err == ""

def test_different_numbers(capsys):
    assert simplify("3/4", "2/3") == True
    captured = capsys.readouterr()
    assert captured.err == ""

def test_larger_numbers(capsys):
    assert simplify("12/25", "5/4") == True
    captured = capsys.readouterr()
    assert captured.err == ""

def test_edge_case_one(capsys):
    assert simplify("1/1", "1/1") == True
    captured = capsys.readouterr()
    assert captured.err == ""

def test_edge_case_negative_numerator(capsys):
    with pytest.raises(ValueError):
        simplify("-1/2", "2/1")
    
def test_edge_case_negative_denominator(capsys):
    with pytest.raises(ValueError):
        simplify("1/2", "-2/1")

def test_edge_case_zero_denominator(capsys):
    with pytest.raises(ValueError):
        simplify("1/0", "1/1")

def test_large_numerator_denominator(capsys):
    assert simplify("1000000/2000000", "2000000/1000000") == True
    captured = capsys.readouterr()
    assert captured.err == ""

def test_numerator_equals_denominator(capsys):
    assert simplify("5/5", "5/5") == True
    captured = capsys.readouterr()
    assert captured.err == ""