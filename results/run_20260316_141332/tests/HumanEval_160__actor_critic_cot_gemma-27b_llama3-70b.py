import pytest

def test_empty_operators():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_empty_operands():
    with pytest.raises(ValueError):
        do_algebra(['+'], [])

def test_operators_longer_than_operands():
    with pytest.raises(ValueError):
        do_algebra(['+', '+'], [1, 2])

def test_operands_longer_than_operators():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3])

def test_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['$'], [1, 2])

def test_non_number_operand():
    with pytest.raises(TypeError):
        do_algebra(['+'], [1, 'a'])

def test_division_by_small_number():
    assert do_algebra(['//'], [10, 0.0000001]) == 0

def test_large_exponent():
    with pytest.raises(OverflowError):
        do_algebra(['**'], [2, 1000])

def test_negative_exponent():
    with pytest.raises(ValueError):
        do_algebra(['**'], [2, -1])

def test_non_list_operators():
    with pytest.raises(TypeError):
        do_algebra("+", [1, 2])

def test_non_list_operands():
    with pytest.raises(TypeError):
        do_algebra(['+'], 1)

def test_duplicate_operators():
    with pytest.raises(ValueError):
        do_algebra(['+', '+'], [1, 2, 3])

def test_duplicate_operands():
    assert do_algebra(['+'], [1, 1]) == 2

def test_type_error_operator():
    with pytest.raises(TypeError):
        do_algebra([1], [1, 2])

def test_type_error_operand():
    with pytest.raises(TypeError):
        do_algebra(['+'], [1, [2]])

def test_basic_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_basic_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_basic_multiplication():
    assert do_algebra(['*'], [4, 3]) == 12

def test_basic_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_basic_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 5

def test_mixed_operations_2():
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 5]) == 7

def test_mixed_operations_3():
    assert do_algebra(['**', '-', '+'], [2, 3, 4, 5]) == 13

def test_single_operator():
    assert do_algebra(['+'], [10, 5]) == 15

def test_large_numbers():
    assert do_algebra(['+'], [1000000, 2000000]) == 3000000

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_exponentiation_zero_exponent():
    assert do_algebra(['**'], [5, 0]) == 1

def test_exponentiation_one_exponent():
    assert do_algebra(['**'], [5, 1]) == 5

def test_exponentiation_large_exponent():
    assert do_algebra(['**'], [2, 10]) == 1024

def test_operands_close_to_zero():
    assert do_algebra(['+'], [0.1, 0.2]) == 0.3

def test_multiple_operations():
    with pytest.raises(ValueError):
        do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5])

def test_long_expression():
    with pytest.raises(ValueError):
        do_algebra(['+', '*', '-', '//', '**', '+'], [1, 2, 3, 4, 5, 6])

def test_zero_operand():
    assert do_algebra(['+', '*'], [0, 2, 3]) == 6

def test_zero_as_first_operand():
    assert do_algebra(['+', '*'], [0, 2, 3]) == 6

def test_none_operators():
    with pytest.raises(TypeError):
        do_algebra(None, [1, 2])

def test_none_operands():
    with pytest.raises(TypeError):
        do_algebra(['+'], None)

def test_float_operands():
    assert do_algebra(['+'], [2.5, 3.5]) == 6.0

def test_negative_operands():
    assert do_algebra(['+'], [-2, 3]) == 1

def test_mixed_positive_negative_operands():
    assert do_algebra(['-', '+'], [-2, 3, 4]) == 5

def test_very_large_numbers():
    assert do_algebra(['+'], [1e10, 2e10]) == 3e10

def test_very_small_numbers():
    assert do_algebra(['+'], [1e-10, 2e-10]) == 3e-10

def test_input_lists_modified():
    operators = ['+']
    operands = [1, 2]
    original_operators = operators[:]
    original_operands = operands[:]
    do_algebra(operators, operands)
    assert operators == original_operators
    assert operands == original_operands

def test_return_non_number():
    with pytest.raises(TypeError):
        def dummy_do_algebra(operator, operand):
            return "not a number"
        dummy_do_algebra(['+'], [1, 2])