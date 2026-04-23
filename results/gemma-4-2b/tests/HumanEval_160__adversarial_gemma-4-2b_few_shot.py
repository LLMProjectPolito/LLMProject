
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
    
    # This is a simplified implementation for testing purposes.
    # A real-world implementation would require a more robust parsing and evaluation mechanism.
    
    expression = ""
    for i in range(len(operand) - 1):
        expression += str(operand[i])
        if i < len(operand) - 2:
            expression += " "
    
    for i in range(len(operator)):
        expression += operator[i]
        if i < len(operator) - 1:
            expression += " "
    
    try:
        return eval(expression)
    except (TypeError, ZeroDivisionError):
        return None



@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 2, 3, 4, 5], [2, 3, 4, 5], 10),
    (["*", 2, 3, 4, 5], [2, 3, 4, 5], 20),
    (["-", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["//", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["**", 2, 3, 4, 5], [2, 3, 4, 5], 16),
    (["+", 2, 3, 4, 5], [2, 3, 4, 5], 10),
    (["*", 2, 3, 4, 5], [2, 3, 4, 5], 20),
    (["-", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["//", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["**", 2, 3, 4, 5], [2, 3, 4, 5], 16),
    (["+", 2, 3, 4, 5], [2, 3, 4, 5], 10),
    (["*", 2, 3, 4, 5], [2, 3, 4, 5], 20),
    (["-", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["//", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["**", 2, 3, 4, 5], [2, 3, 4, 5], 16),
    (["+", 2, 3, 4, 5], [2, 3, 4, 5], 10),
    (["*", 2, 3, 4, 5], [2, 3, 4, 5], 20),
    (["-", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["//", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["**", 2, 3, 4, 5], [2, 3, 4, 5], 16),
    (["+", 2, 3, 4, 5], [2, 3, 4, 5], 10),
    (["*", 2, 3, 4, 5], [2, 3, 4, 5], 20),
    (["-", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["//", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["**", 2, 3, 4, 5], [2, 3, 4, 5], 16),
])
def test_do_algebra_basic(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 2, 3, 4, 5], [2, 3, 4, 5], 10),
    (["*", 2, 3, 4, 5], [2, 3, 4, 5], 20),
    (["-", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["//", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["**", 2, 3, 4, 5], [2, 3, 4, 5], 16),
])
def test_do_algebra_edge_cases(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 2, 3, 4, 5], [2, 3, 4, 5], 10),
    (["*", 2, 3, 4, 5], [2, 3, 4, 5], 20),
    (["-", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["//", 2, 3, 4, 5], [2, 3, 4, 5], 1),
    (["**", 2, 3, 4, 5], [2, 3, 4, 5], 16),
])
def test_do_algebra_invalid_input(operator, operand, expected):
    with pytest.raises(TypeError):
        do_algebra(operator, operand)
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)