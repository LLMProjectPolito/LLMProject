import pytest

def test_algebra_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6

def test_algebra_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_algebra_complex_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_algebra_complex_expression_2():
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8

def test_algebra_complex_expression_3():
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -1

def test_algebra_long_expression():
    assert do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]) == 15

def test_algebra_mixed_operations():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5]) == 1

def test_algebra_zero_operand():
    assert do_algebra(['+'], [0, 5]) == 5

def test_algebra_zero_result():
    assert do_algebra(['-', '+'], [5, 5, 10]) == 0

def test_algebra_division_by_one():
    assert do_algebra(['//'], [10, 1]) == 10

def test_algebra_exponentiation_one():
    assert do_algebra(['**'], [2, 1]) == 2

def test_algebra_exponentiation_zero():
    assert do_algebra(['**'], [2, 0]) == 1