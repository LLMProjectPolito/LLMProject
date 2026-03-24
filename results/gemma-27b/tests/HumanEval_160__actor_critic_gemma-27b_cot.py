
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

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
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 5]) == 10

def test_do_algebra_complex_expression_3():
    assert do_algebra(['**', '-', '+'], [2, 3, 4, 5]) == 13

def test_do_algebra_with_zero():
    assert do_algebra(['+', '-', '*'], [0, 1, 2, 3]) == 1

def test_do_algebra_with_large_numbers():
    assert do_algebra(['+', '*', '-'], [100, 200, 3, 50]) == 650

def test_do_algebra_mixed_operators():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5]) == 1

def test_do_algebra_mismatched_lengths():
    with pytest.raises(ValueError):
        do_algebra(['+'], [2, 3, 4])

def test_do_algebra_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_complex_expression_4():
    assert do_algebra(['*', '+', '-', '**', '//'], [2, 3, 4, 2, 5]) == 1

def test_do_algebra_complex_expression_5():
    assert do_algebra(['+', '-', '*', '//', '**'], [5, 2, 3, 6, 2]) == 1

def test_do_algebra_floor_division_negative():
    assert do_algebra(['//'], [-10, 3]) == -4

def test_do_algebra_floor_division_non_integer():
    assert do_algebra(['//'], [10, 3]) == 3

def test_do_algebra_multiple_operators():
    assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

def test_do_algebra_multiple_subtractions():
    assert do_algebra(['-', '-', '-'], [5, 2, 1, 3]) == -1

def test_do_algebra_multiple_multiplications():
    assert do_algebra(['*', '*', '*'], [2, 3, 4, 5]) == 120

def test_do_algebra_multiple_floor_divisions():
    assert do_algebra(['//', '//'], [10, 2, 4]) == 2

def test_do_algebra_multiple_exponentiations():
    assert do_algebra(['**', '**'], [2, 2, 3]) == 16

def test_do_algebra_empty_operator_list():
    with pytest.raises(ValueError):
        do_algebra([], [2, 3])

def test_do_algebra_single_number():
    with pytest.raises(ValueError):
        do_algebra(['+'], [2])

def test_do_algebra_negative_numbers_subtraction():
    assert do_algebra(['-'], [-5, 2]) == -7

def test_do_algebra_negative_numbers_multiplication():
    assert do_algebra(['*'], [-2, 3]) == -6

def test_do_algebra_negative_numbers_exponentiation():
    assert do_algebra(['**'], [-2, 3]) == 8

def test_do_algebra_input_validation_string():
    with pytest.raises(TypeError):
        do_algebra(['+'], [2, 'a'])

def test_do_algebra_input_validation_float():
    with pytest.raises(TypeError):
        do_algebra(['+'], [2, 3.5])

@pytest.mark.parametrize(
    "operators, operands, expected",
    [
        (['+'], [1, 2], 3),
        (['-'], [5, 2], 3),
        (['*'], [2, 3], 6),
        (['//'], [10, 2], 5),
        (['**'], [2, 3], 8),
        (['+', '*'], [2, 3, 4], 14),
        (['-', '//'], [10, 2, 4], 3),
        (['**', '+'], [2, 3, 2], 10),
    ],
)
def test_do_algebra_parameterized(operators, operands, expected):
    assert do_algebra(operators, operands) == expected