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
                raise ZeroDivisionError("Floor division by zero")
            result //= num
        elif op == '**':
            result **= num
        else:
            raise ValueError(f"Invalid operator: {op}")
    return result

def test_valid_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_addition_only():
    assert do_algebra(['+'], [1, 2]) == 3

def test_subtraction_only():
    assert do_algebra(['-'], [5, 2]) == 3

def test_multiplication_only():
    assert do_algebra(['*'], [2, 3]) == 6

def test_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_mixed_operators():
    assert do_algebra(['+', '-', '*', '//'], [1, 2, 3, 4, 2]) == 1

def test_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['%'], [1, 2])

def test_invalid_length():
    with pytest.raises(IndexError):
        do_algebra(['+'], [1])
    with pytest.raises(IndexError):
        do_algebra(['+', '+'], [1, 2, 3])

def test_negative_operand():
    with pytest.raises(TypeError):
        do_algebra(['+'], [-1, 2])

def test_empty_operator_operand():
    with pytest.raises(IndexError):
        do_algebra([], [1, 2])
    with pytest.raises(IndexError):
        do_algebra(['+'], [1])

def test_large_numbers():
    assert do_algebra(['*'], [100000, 100000]) == 10000000000