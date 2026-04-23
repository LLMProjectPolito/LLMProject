
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
    if not operator or not operand or len(operator) != len(operand) - 1:
        raise ValueError("Invalid input lists.")

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
                raise ZeroDivisionError("Division by zero.")
            result //= num
        elif op == '**':
            result **= num
        else:
            raise ValueError(f"Invalid operator: {op}")

    return result

# Pytest Suite - Consolidated
def test_do_algebra_basic():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['+', '-'], [1, 2, 3]) == 0
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['-','+','*'], [10, 5, 2, 3]) == 11
    assert do_algebra(['+','+'], [1, 2, 3]) == 6

def test_do_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['+', '**'], [2, 3, 2]) == 11
    assert do_algebra(['+', '**'], [1, 2, 3]) == 10

def test_do_algebra_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['+', '//'], [10, 2, 3]) == 8

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 2]) == 1
    assert do_algebra(['*', '+', '-', '**', '//'], [2, 3, 4, 2, 2]) == 2
    assert do_algebra(['*', '+', '//', '-'], [2, 3, 4, 5, 2]) == 5
    assert do_algebra(['+', '*', '-', '**', '//'], [1, 2, 3, 2, 4]) == -1

def test_do_algebra_long_expression():
    operators = ['+', '-', '*', '+', '//', '**']
    operands = [1, 2, 3, 4, 5, 2]
    assert do_algebra(operators, operands) == 1

def test_do_algebra_single_operation():
    assert do_algebra(['+'], [5, 3]) == 8
    assert do_algebra(['-'], [10, 2]) == 8
    assert do_algebra(['*'], [4, 5]) == 20
    assert do_algebra(['//'], [10, 5]) == 2
    assert do_algebra(['**'], [2, 4]) == 16

def test_do_algebra_zero_division():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['$'], [2, 3])
    with pytest.raises(ValueError):
        do_algebra(['%'], [5, 2])

def test_do_algebra_invalid_input_length():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3])
    with pytest.raises(ValueError):
        do_algebra(['+', '*'], [1, 2])

def test_do_algebra_empty_lists():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])
    with pytest.raises(ValueError):
        do_algebra(['+'], [])

def test_do_algebra_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000
    assert do_algebra(['+'], [10**9, 10**9]) == 2 * 10**9

# --- Palindrome Tests ---
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# --- Max Tests ---
def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None