
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

def test_do_algebra_modulo():
    assert do_algebra(['%'], [10, 3]) == 1

def test_do_algebra_complex_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_with_zero():
    assert do_algebra(['+', '-', '*'], [0, 1, 2, 3]) == 1

def test_do_algebra_with_large_numbers():
    assert do_algebra(['+', '*', '-'], [100, 200, 3, 50]) == 650

def test_do_algebra_mismatched_lengths():
    with pytest.raises(ValueError):
        do_algebra(['+'], [2, 3, 4])

def test_do_algebra_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_operator_precedence():
    assert do_algebra(['+', '*'], [2, 3, 4]) == pytest.approx(14)  # (2 + 3) * 4
    assert do_algebra(['*', '+'], [2, 3, 4]) == pytest.approx(20)  # 2 * (3 + 4)
    assert do_algebra(['**', '+', '*'], [2, 3, 4, 5]) == pytest.approx(23)
    assert do_algebra(['+', '**', '*'], [2, 3, 4, 5]) == pytest.approx(26)
    assert do_algebra(['**', '*', '+'], [2, 3, 4, 5]) == pytest.approx(38)

def test_do_algebra_negative_numbers():
    assert do_algebra(['+', '-'], [-2, 3]) == 1
    assert do_algebra(['*'], [-2, 3]) == -6

def test_do_algebra_floating_point_numbers():
    assert do_algebra(['+'], [2.5, 3.5]) == pytest.approx(6.0)
    assert do_algebra(['*'], [2.5, 3.5]) == pytest.approx(8.75)

def test_do_algebra_mixed_operators_and_numbers():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5]) == pytest.approx(1)

def test_do_algebra_edge_case_1():
    assert do_algebra(['*','+'], [1,2,3]) == 5

def test_do_algebra_edge_case_2():
    assert do_algebra(['-','*'], [5,2,3]) == -1

@pytest.mark.parametrize(
    "operators, operands, expected",
    [
        (['+', '+', '+'], [1, 2, 3, 4], 10),
        (['-', '-', '-'], [5, 2, 1, 3], -1),
        (['*', '*', '*'], [2, 3, 4, 5], 120),
        (['//', '//'], [10, 2, 4], 2),
        (['**', '**'], [2, 3, 2], 16),
        (['+', '+'], [1, 1], 2),
        (['-', '-'], [5, 2], 3),
        (['*', '*'], [2, 3], 6),
        (['//', '//'], [10, 2], 5),
        (['**', '**'], [2, 2], 4),
        (['**', '+'], [2, 3, 2], 10),
        (['+', '**'], [2, 3, 2], 10),
        (['**', '*'], [2, 3, 4], 72),
        (['*', '**'], [2, 3, 4], 72),
        (['//', '*'], [10, 2, 3], 15),
        (['*', '//'], [10, 2, 3], 15),
    ],
)
def test_do_algebra_only_one_operator(operators, operands, expected):
    assert do_algebra(operators, operands) == pytest.approx(expected)

def test_do_algebra_empty_operators():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_do_algebra_empty_operands():
    with pytest.raises(ValueError):
        do_algebra(['+'], [])