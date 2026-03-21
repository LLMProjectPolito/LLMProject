import pytest

def test_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_multiplication():
    assert do_algebra(['*'], [4, 3]) == 12

def test_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['//'], [7, 2]) == 3

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['**'], [3, 2]) == 9
    assert do_algebra(['**'], [2, 0]) == 1
    assert do_algebra(['**'], [0, 2]) == 0

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -4

def test_long_sequence():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2]) == 1

def test_zero_operand():
    assert do_algebra(['+', '*', '-'], [0, 3, 4, 5]) == 7
    assert do_algebra(['//', '+'], [0, 5]) == 0
    assert do_algebra(['**', '+'], [0, 5]) == 1

def test_large_numbers():
    assert do_algebra(['+'], [1000000, 2000000]) == 3000000
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_combination():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 2, 2]) == -1

def test_single_operator():
    assert do_algebra(['-'], [10, 5]) == 5

def test_edge_case_floor_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])