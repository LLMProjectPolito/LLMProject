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
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    if not operator or not operand:
        raise ValueError("Operator and operand lists cannot be empty.")
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than operand list.")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands.")
    for num in operand:
        if num < 0:
            raise ValueError("Operand list must contain non-negative integers.")

    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i + 1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            if num == 0:
                raise ZeroDivisionError("Floor division by zero is not allowed.")
            result //= num
        elif op == '**':
            result **= num
        else:
            raise ValueError("Invalid operator: {}".format(op))
    return result

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (['+'], [2, 3], 5),
        (['-'], [5, 2], 3),
        (['*'], [2, 3], 6),
        (['//'], [10, 2], 5),
        (['**'], [2, 3], 8),
    ],
)
def test_basic_operations(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

def test_complex_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_multiple_operations():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 1

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_empty_operator_list():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_empty_operand_list():
    with pytest.raises(ValueError):
        do_algebra(['+'], [])

def test_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['%'], [1, 2])

def test_negative_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [-1, 2])

def test_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_exponentiation_with_zero():
    assert do_algebra(['**'], [2, 0]) == 1

def test_floor_division_with_remainder():
    assert do_algebra(['//'], [7, 3]) == 2

def test_floor_division_with_one():
    assert do_algebra(['//'], [5, 1]) == 5

def test_multiple_floor_divisions():
    assert do_algebra(['//', '//'], [10, 2, 3]) == 1

def test_multiple_exponentiations():
    assert do_algebra(['**', '**'], [2, 2, 3]) == 16

def test_complex_expression_2():
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 7

def test_operator_precedence():
    assert do_algebra(['*', '+'], [2, 3, 2]) == 10

def test_floor_division_with_negative_numbers():
    assert do_algebra(['//'], [-7, 3]) == -3

def test_exponentiation_with_negative_base():
    assert do_algebra(['**'], [-2, 3]) == -8

def test_long_operator_operand_lists():
    operators = ['+'] * 99
    operands = [1] * 100
    assert do_algebra(operators, operands) == 100

def test_type_error():
    with pytest.raises(TypeError):
        do_algebra(['+'], [1, '2'])