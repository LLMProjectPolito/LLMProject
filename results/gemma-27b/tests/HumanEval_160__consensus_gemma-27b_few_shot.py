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
    assert do_algebra(['+', '*', '-', '//'], [2, 3, 4, 5, 2]) == 2 + 3 * 4 - 5 // 2
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8
    assert do_algebra(['**', '-', '+'], [2, 3, 1, 4]) == 13

def test_algebra_multiple_operators():
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == (1 + 2 - 3) * 4
    assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10
    assert do_algebra(['-', '-', '-'], [5, 2, 1, 3]) == -1
    assert do_algebra(['*', '*', '*'], [2, 3, 4, 5]) == 120
    assert do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]) == 15
    assert do_algebra(['-', '-', '-', '-'], [5, 1, 1, 1, 1]) == 1

def test_algebra_long_expression():
    assert do_algebra(['+', '*', '-', '+', '//'], [1, 2, 3, 4, 5, 2]) == (1 + 2 * 3 - 4 + 5) // 2
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5, 2]) == -1

def test_algebra_zero_operand():
    assert do_algebra(['*'], [0, 5]) == 0

def test_algebra_zero_result():
    assert do_algebra(['+', '-'], [5, 5]) == 0

def test_algebra_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_algebra_division_by_one():
    assert do_algebra(['//'], [10, 1]) == 10

def test_algebra_exponentiation_one():
    assert do_algebra(['**'], [5, 1]) == 5

def test_algebra_exponentiation_zero():
    assert do_algebra(['**'], [5, 0]) == 1

def test_algebra_mixed_operators():
    assert do_algebra(['+', '*', '-', '//'], [1, 2, 3, 4, 2]) == 3
    assert do_algebra(['**', '+', '*', '-'], [2, 3, 2, 1, 1]) == 15
    assert do_algebra(['//', '-', '+', '*'], [10, 2, 3, 4, 1]) == 15

def test_algebra_exponentiation_first():
    assert do_algebra(['**', '+'], [2, 3, 2]) == 10
    assert do_algebra(['+', '**'], [2, 2, 3]) == 10

def test_algebra_floor_division():
    assert do_algebra(['//', '+'], [10, 2, 3]) == 8
    assert do_algebra(['+', '//'], [3, 10, 2]) == 8
    assert do_algebra(['//', '//'], [10, 2, 2]) == 2

def test_algebra_exponentiation_multiple():
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512