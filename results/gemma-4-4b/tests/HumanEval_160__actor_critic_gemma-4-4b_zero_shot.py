
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
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    if not operator or not operand:
        raise ValueError("Operator and operand lists cannot be empty.")
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of operand list.")
    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand list must contain non-negative integers.")

    expression = ""
    for i in range(len(operator)):
        expression += str(operand[i])
        expression += operator[i]
        expression += str(operand[i+1])

    try:
        result = eval(expression)
        return result
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")


@pytest.fixture
def test_do_algebra():
    yield

def test_addition_and_subtraction():
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == 11
    assert do_algebra(['+', '-', '*', '/'], [10, 2, 3, 4]) == 14
    assert do_algebra(['+', '-', '*', '**'], [2, 3, 4, 5]) == 29
    assert do_algebra(['+', '-', '*', '//'], [10, 2, 3, 4]) == 14
    assert do_algebra(['+', '-', '*', '%'], [10, 2, 3, 4]) == 2

def test_multiplication_and_division():
    assert do_algebra(['*', '//', '+'], [2, 3, 4, 5]) == 14
    assert do_algebra(['*', '+', '/'], [2, 3, 4, 5]) == 11
    assert do_algebra(['*', '-', '+'], [2, 3, 4, 5]) == 14

def test_exponentiation():
    assert do_algebra(['**', '+'], [2, 3, 4]) == 17
    assert do_algebra(['**', '-', '+'], [2, 3, 4]) == 13
    assert do_algebra(['**', '*', '+'], [2, 3, 4]) == 50

def test_edge_cases():
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['-'], [5, 2]) == 3
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['**'], [2, 3]) == 8

def test_large_numbers():
    assert do_algebra(['+', '*'], [1000, 2000, 3000]) == 9000
    assert do_algebra(['**', '+'], [10, 2, 3]) == 1009

def test_zero_values():
    assert do_algebra(['+', '*'], [0, 2, 3]) == 6
    assert do_algebra(['-', '/'], [10, 0, 5]) == 2
    assert do_algebra(['**', '+'], [0, 2, 3]) == 1

def test_invalid_input_empty_lists():
    with pytest.raises(ValueError) as e:
        do_algebra([], [1, 2, 3])
    assert "Operator and operand lists cannot be empty." in str(e.value)

def test_invalid_input_length_mismatch():
    with pytest.raises(ValueError) as e:
        do_algebra(['+', '*'], [1, 2, 3])
    assert "Length of operator list must be one less than the length of operand list." in str(e.value)

def test_invalid_input_non_integer_operand():
    with pytest.raises(ValueError) as e:
        do_algebra(['+', '*'], [1, 2, 3.5])
    assert "Operand list must contain non-negative integers." in str(e.value)

def test_invalid_input_negative_operand():
    with pytest.raises(ValueError) as e:
        do_algebra(['+', '*'], [1, 2, -3])
    assert "Operand list must contain non-negative integers." in str(e.value)