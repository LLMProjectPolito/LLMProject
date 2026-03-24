import pytest

def test_do_algebra_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_do_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6

def test_do_algebra_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_do_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_complex_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_complex_expression_2():
    assert do_algebra(['*', '-', '+'], [2, 3, 4, 5]) == 11

def test_do_algebra_complex_expression_3():
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -1

def test_do_algebra_with_zero():
    assert do_algebra(['+', '-', '*'], [0, 1, 2, 3]) == 1

def test_do_algebra_with_large_numbers():
    assert do_algebra(['+', '*', '-'], [100, 200, 3, 50]) == 650

def test_do_algebra_floor_division_with_remainder():
    assert do_algebra(['//'], [7, 2]) == 3

def test_do_algebra_exponentiation_with_zero_exponent():
    assert do_algebra(['**'], [5, 0]) == 1

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

def test_do_algebra_multiple_subtractions():
    assert do_algebra(['-', '-', '-'], [5, 1, 2, 3]) == -1

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '*', '-', '//'], [2, 3, 4, 8]) == 5

def test_do_algebra_long_expression():
    assert do_algebra(['+', '-', '*', '+', '//', '**'], [1, 2, 3, 4, 8, 2]) == 9