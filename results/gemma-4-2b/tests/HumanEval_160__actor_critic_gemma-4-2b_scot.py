
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
        raise ValueError("The length of operator list must be one less than the length of operand list.")
    if any(op not in ['+', '-', '*', '//', '**'] for op in operator):
        raise ValueError("Invalid operator.")
    if any(x < 0 for x in operand):
        raise ValueError("Operands must be non-negative integers.")

    try:
        result = eval(" ".join(map(str, operand[1:])) + " " + operator[0] + " " + str(operand[0]))
        return result
    except (TypeError, ZeroDivisionError):
        raise ValueError("Invalid expression.")



def test_basic_addition():
    assert do_algebra(['+', 2, 3, 4], [1, 2, 3, 4]) == 9

def test_basic_subtraction():
    assert do_algebra(['-', 2, 3, 4], [1, 2, 3, 4]) == 1

def test_basic_multiplication():
    assert do_algebra(['*', 2, 3, 4], [1, 2, 3, 4]) == 24

def test_basic_floor_division():
    assert do_algebra(['//', 2, 3, 4], [1, 2, 3, 4]) == 0

def test_basic_exponentiation():
    assert do_algebra(['**', 2, 3, 4], [1, 2, 3, 4]) == 16

def test_mixed_operations():
    assert do_algebra(['+', '-', '*', 2, 3, 4], [1, 2, 3, 4]) == 11

def test_empty_operator_list():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2, 3, 4])

def test_empty_operand_list():
    with pytest.raises(ValueError):
        do_algebra(['+', 2, 3, 4], [])

def test_single_operand():
    with pytest.raises(ValueError):
        do_algebra(['+', 2, 3, 4], [1])

def test_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['%', 2, 3, 4], [1, 2, 3, 4])

def test_large_numbers():
    assert do_algebra(['+', 10**9, 2, 3], [1, 2, 3]) == 1000000005

def test_exponentiation_with_zero():
    assert do_algebra(['**', 2, 3, 4], [1, 2, 3, 4]) == 16

def test_negative_numbers():
    assert do_algebra(['+', -2, 3, 4], [1, 2, 3, 4]) == 5

def test_mixed_positive_and_negative_numbers():
    assert do_algebra(['+', -2, 3, 4], [1, 2, 3, 4]) == 5

def test_operator_at_beginning():
    assert do_algebra(['+', 2, 3, 4], [1, 2, 3, 4]) == 9

def test_different_operand_lengths():
    assert do_algebra(['+', 2, 3, 4], [1, 2, 3]) == 9