import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
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

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_do_algebra_addition():
    assert do_algebra(['+', '+'], [2, 3, 4]) == 9
    assert do_algebra(['+', '+'], [1, 2, 3, 4]) == 10

def test_do_algebra_subtraction():
    assert do_algebra(['-', '-'], [5, 3, 2]) == 0
    assert do_algebra(['-', '-'], [10, 5, 2, 1]) == 4

def test_do_algebra_multiplication():
    assert do_algebra(['*', '*'], [2, 3, 4]) == 24
    assert do_algebra(['*', '*'], [1, 2, 3, 4, 5]) == 120

def test_do_algebra_floor_division():
    assert do_algebra(['//', '//'], [10, 2, 5]) == 1
    assert do_algebra(['//', '//'], [15, 3, 5]) == 3

def test_do_algebra_exponentiation():
    assert do_algebra(['**', '**'], [2, 3, 2]) == 8
    assert do_algebra(['**', '**'], [2, 3, 2, 2]) == 64

def test_do_algebra_mixed():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['+', '*', '-', '//'], [2, 3, 4, 5, 2]) == 1
    assert do_algebra(['**', '+', '*'], [2, 3, 2, 1, 2]) == 16