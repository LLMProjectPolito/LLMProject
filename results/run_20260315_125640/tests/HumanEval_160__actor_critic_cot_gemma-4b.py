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
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

def test_basic_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '//'], [2, 3, 4]) == 2
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['-', '*'], [5, 2, 3]) == 1
    assert do_algebra(['+', '**'], [1, 2, 3]) == 10

def test_zero_operands():
    assert do_algebra(['+', '-'], [0, 0]) == 0
    assert do_algebra(['*', '//'], [0, 0]) == 0
    assert do_algebra(['**'], [0, 0]) == 0

def test_empty_operator():
    assert do_algebra([], [1, 2, 3]) == 1

def test_empty_operand():
    assert do_algebra(['+', '*'], []) == 0

def test_single_element_operator():
    assert do_algebra(['+'], [1, 2, 3]) == 1

def test_single_element_operand():
    assert do_algebra(['+', '*'], [1]) == 1

def test_zero_operands_with_operations():
    assert do_algebra(['+', '*'], [0, 0, 0]) == 0

def test_invalid_input_length():
    with pytest.raises(ValueError):
        do_algebra(['+', '*'], [1, 2])
    with pytest.raises(ValueError):
        do_algebra(['+', '*'], [1, 2, 3])

def test_invalid_operator_length():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3])

def test_negative_operands():
    assert do_algebra(['+', '-'], [-2, 3, 4, 5]) == 0
    assert do_algebra(['*', '//'], [-2, 3, 4]) == -2

def test_mixed_operands():
    assert do_algebra(['+', '*', '-'], [1, -2, 3, 4, 5]) == 0
    assert do_algebra(['*', '//'], [1, -2, 3, 4]) == -2
    assert do_algebra(['**'], [1, -2]) == 1
    assert do_algebra(['+', '**'], [1, -2, 3]) == 2
    assert do_algebra(['-', '*'], [5, -2, 3]) == -1

def test_large_numbers():
    assert do_algebra(['+', '*'], [1000000, 2000000]) == 3000000
    assert do_algebra(['//'], [1000000, 2000000]) == 4
    assert do_algebra(['**'], [2, 1000]) == 1024

def test_exponentiation_with_large_base():
    assert do_algebra(['**'], [2, 10]) == 1024
    assert do_algebra(['**'], [3, 2]) == 9

def test_floor_division_with_large_numbers():
    assert do_algebra(['//'], [1000000, 3]) == 333333
    assert do_algebra(['//'], [1000001, 3]) == 333334