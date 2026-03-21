import pytest

def test_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_multiplication():
    assert do_algebra(['*'], [4, 3]) == 12

def test_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_long_sequence():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2]) == 1

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_exponentiation_zero_exponent():
    assert do_algebra(['**'], [5, 0]) == 1

def test_exponentiation_one_base():
    assert do_algebra(['**'], [1, 5]) == 1

def test_large_numbers():
    assert do_algebra(['+'], [10**9, 10**9]) == 2 * (10**9)

def test_operands_close_to_zero():
    assert do_algebra(['-'], [0.1, 0.05]) == pytest.approx(0.05)

def test_empty_operator_list():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_mismatched_operator_operand_count():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3])

def test_operator_precedence_multiplication_addition():
    assert do_algebra(['*', '+'], [2, 3, 4]) == 14

def test_complex_mixed_operations():
    assert do_algebra(['+', '*', '-', '//'], [1, 2, 3, 4, 2]) == 1

def test_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['%'], [5, 2])

def test_non_numeric_operands():
    with pytest.raises(TypeError):
        do_algebra(['+'], [1, 'a'])

def test_negative_addition():
    assert do_algebra(['+'], [-2, 3]) == 1

def test_negative_subtraction():
    assert do_algebra(['-'], [5, -2]) == 7

def test_negative_multiplication():
    assert do_algebra(['*'], [-4, 3]) == -12

def test_negative_exponentiation():
    assert do_algebra(['**'], [2, -2]) == 0.25

def test_zero_base_negative_exponent():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['**'], [0, -1])

def test_complex_precedence():
    assert do_algebra(['+', '*', '-', '/', '**'], [1, 2, 3, 4, 2]) == pytest.approx(1.5)