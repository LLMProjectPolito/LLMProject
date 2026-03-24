
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
        Operand is a list of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    if not operator or not operand or len(operator) != len(operand) - 1:
        raise ValueError("Invalid input: operator and operand lists are not valid.")

    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i+1]

        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            if num == 0:
                raise ZeroDivisionError("Division by zero")
            result //= num
        elif op == '**':
            result **= num
        else:
            raise ValueError(f"Invalid operator: {op}")

    return result

# Pytest tests
@pytest.mark.parametrize("operator, operand, expected", [
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['-', '+', '*'], [10, 5, 2, 3], 11),
    (['+'], [1, 2], 3),
    (['-', '-'], [10, 2, 3], 5),
    (['*'], [2, 3], 6),
    (['//', '//'], [20, 2, 5], 2),
    (['**'], [2, 3], 8),
    (['**', '**'], [2, 3, 2], 64),
    (['**'], [2, 0], 1),
    (['**'], [2, -1], 0.5),
    (['+', '*', '-', '//'], [1, 2, 3, 4, 2], 3),
    (['*', '+', '**'], [2, 3, 2, 2], 16),
])
def test_algebra_parametrized(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

def test_algebra_zero_division():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_algebra_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['$'], [1, 2])

def test_algebra_invalid_input_length():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3])
    with pytest.raises(ValueError):
        do_algebra(['+', '+'], [1, 2])

def test_algebra_empty_lists():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])
    with pytest.raises(ValueError):
        do_algebra(['+'], [])

def test_algebra_large_numbers():
    assert do_algebra(['+', '*'], [1000, 1000, 1000]) == 1001000

def test_algebra_consecutive_operators():
    assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

# New tests based on review
def test_algebra_zero_exponentiation():
    assert do_algebra(['**'], [0, 2]) == 0

def test_algebra_floor_division_negative():
    assert do_algebra(['//'], [-10, 3]) == -4

def test_algebra_negative_exponentiation():
    assert do_algebra(['**'], [-2, -3]) == 0.125

def test_algebra_empty_operator_nonempty_operand():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_algebra_complex_mixed_operations():
    assert do_algebra(['+', '*', '-', '**', '//'], [1, 2, 3, 2, 4]) == -1