import pytest

def test_algebra_basic():
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

def test_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_algebra_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_algebra_complex():
    assert do_algebra(['+', '*', '-', '//'], [2, 3, 4, 5]) == 9

def test_algebra_long():
    assert do_algebra(['+', '-', '*', '+', '//', '**'], [1, 2, 3, 4, 5, 2]) == 16

def test_algebra_multiple_operators():
    assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

def test_algebra_zero_operand():
    assert do_algebra(['*'], [5, 0]) == 0

def test_algebra_division_by_one():
    assert do_algebra(['//'], [5, 1]) == 5

def test_algebra_exponentiation_zero():
    assert do_algebra(['**'], [2, 0]) == 1

def test_algebra_exponentiation_one():
    assert do_algebra(['**'], [5, 1]) == 5