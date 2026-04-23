
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
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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
    expression = ""
    for i in range(len(operator)):
        expression += str(operand[i])
        expression += operator[i]
        expression += str(operand[i+1])
    return eval(expression)



@pytest.mark.parametrize("input_string, expected", [
    ("radar", True),
    ("hello", False),
    ("", True),
    ("A man, a plan, a canal: Panama", True),
    ("Racecar", True),
    ("Was it a car or a cat I saw?", True),
    ("12321", True),
    ("12345", False),
])
def test_is_palindrome(input_string, expected):
    assert is_palindrome(input_string) == expected


@pytest.mark.parametrize("input_array, expected", [
    ([1, 2, 3], 3),
    ([], None),
    ([5, 2, 8, 1, 9], 9),
    ([-1, -5, -2], -1),
    ([0, 0, 0], 0),
])
def test_get_max(input_array, expected):
    assert get_max(input_array) == expected


@pytest.mark.parametrize("operator, operand, expected", [
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['+', '-', '*', '/'], [10, 5, 2, 1], 15),
    (['+', '*', '**', '/'], [2, 3, 2, 2], 14),
    (['-', '+', '*', '/'], [1, 2, 3, 4], 5),
    (['+', '-', '*', '**'], [5, 2, 3, 2], 17),
])
def test_do_algebra(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand", [
    (['+', '*', '-'], [1, 2, 3]),
    (['+', '-', '*', '/'], [10, 5, 2, 1]),
    (['+', '*', '**', '/'], [2, 3, 2, 2]),
    (['-', '+', '*', '/'], [1, 2, 3, 4]),
    (['+', '-', '*', '**'], [5, 2, 3, 2]),
])
def test_do_algebra_length(operator, operand):
    assert len(operator) == len(operand) - 1
    assert len(operand) >= 2
    assert len(operator) >= 1