
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
    if len(operand) != 2:
        raise ValueError("Operand must be a list of two integers.")
    
    if operator == '+':
        return operand[0] + operand[1]
    elif operator == '-':
        return operand[0] - operand[1]
    elif operator == '*':
        return operand[0] * operand[1]
    elif operator == '//':
        return operand[0] // operand[1]
    elif operator == '**':
        return operand[0] ** operand[1]
    else:
        return 0  # Default value for unknown operators


def test_do_algebra():
    assert do_algebra('+ 2 3') == 5
    assert do_algebra('- 2 3') == 1
    assert do_algebra('* 2 3') == 6
    assert do_algebra('/') 2 3 == 1
    assert do_algebra('2 ** 3') == 8
    assert do_algebra('2 + 3 * 4') == 9
    assert do_algebra('2 - 3 * 4') == 1
    assert do_algebra('2 * 3 ** 2') == 9
    assert do_algebra('2 / 3') == 0.6666666666666666
    assert do_algebra('2 ** 3') == 8
    assert do_algebra('2 + 3 * 4') == 9
    assert do_algebra('2 - 3 * 4') == 1
    assert do_algebra('2 * 3 ** 2') == 9
    assert do_algebra('2 / 3') == 0.6666666666666666
    
    # Edge cases
    assert do_algebra('') == 0
    assert do_algebra([1, 2]) == 3
    assert do_algebra([1, 2, 3]) == 6
    assert do_algebra([1, 2, 3, 4]) == 24
    assert do_algebra([1, 2, 3, 4, 5]) == 120
    
    #Error handling
    try:
        do_algebra('1 2')
    except ValueError:
        pass
    
    try:
        do_algebra('+ 2')
    except ValueError:
        pass
    
    try:
        do_algebra('2 3')
    except ValueError:
        pass