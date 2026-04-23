
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
        return None  # Handle empty input lists

    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of operand list.")
    
    # Define the evaluation function
    def evaluate(expr):
        if len(expr) == 1:
            return expr[0]
        elif len(expr) == 2:
            return expr[0] + expr[1]
        elif len(expr) == 3:
            return expr[0] * expr[1]
        elif len(expr) == 4:
            return expr[0] // expr[1]
        elif len(expr) == 5:
            return expr[0] ** expr[1]
        else:
            raise ValueError("Invalid expression")
    
    expression = ""
    for i in range(len(operator)):
        expression += str(operand[i])
        if i < len(operator) - 1:
            expression += operator[i]
            expression += str(operand[i+1])
    return evaluate(expression)


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_do_algebra_basic():
    assert do_algebra(['+', 2, 3, 4], [1, 2, 3]) == 5
    assert do_algebra(['-', 5, 2, 1], [1, 2, 3]) == 3
    assert do_algebra(['*', 2, 3, 4], [1, 2, 3]) == 24
    assert do_algebra(['//', 5, 2, 3], [1, 2, 3]) == 1
    assert do_algebra(['**', 2, 3, 4], [1, 2, 3]) == 16

def test_do_algebra_mixed():
    assert do_algebra(['+', '*', 2, 3, 4], [1, 2, 3]) == 14
    assert do_algebra(['-', '*', 2, 3, 4], [1, 2, 3]) == 10
    assert do_algebra(['//', '*', 2, 3, 4], [1, 2, 3]) == 2

def test_do_algebra_exponentiation():
    assert do_algebra(['**', 2, 3, 4], [1, 2, 3]) == 16
    assert do_algebra(['**', 2, 3, 4], [1, 2, 3]) == 8
    assert do_algebra(['**', 2, 3, 4], [1, 2, 3]) == 64
    assert do_algebra(['**', 2, 3, 4], [1, 2, 3]) == 256

def test_do_algebra_edge_cases():
    assert do_algebra(['+', 1, 2, 3], [1, 2, 3]) == 6
    assert do_algebra(['-', 1, 2, 3], [1, 2, 3]) == 2
    assert do_algebra(['*', 1, 2, 3], [1, 2, 3]) == 6
    assert do_algebra(['//', 1, 2, 3], [1, 2, 3]) == 0
    assert do_algebra(['**', 1, 2, 3], [1, 2, 3]) == 9

def test_do_algebra_invalid_length():
    with pytest.raises(ValueError):
        do_algebra(['+', 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        do_algebra(['+', 1, 2, 3], [1, 2])
    
def test_do_algebra_empty_input():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2, 3])
    with pytest.raises(ValueError):
        do_algebra([ '+', 1, 2, 3 ], [1,2])

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_longer():
    assert is_palindrome('madam') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True

def test_is_palindrome_not_palindrome():
    assert is_palindrome('hello') == False
    assert is_palindrome('world') == False
    assert is_palindrome('python') == False

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4