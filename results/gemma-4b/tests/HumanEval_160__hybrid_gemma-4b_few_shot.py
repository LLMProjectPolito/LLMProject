
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
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Race car') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam.') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 1, 9, 3]) == 9
    assert get_max([10, 5, 20, 15]) == 20

def test_max_empty():
    assert get_max([]) == None

def test_max_single_element():
    assert get_max([7]) == 7

def test_max_negative_and_positive():
    assert get_max([-1, 5, -3, 2]) == 5

def test_do_algebra_addition():
    assert do_algebra(['+', '+', '+'], [2, 3, 4]) == 9
    assert do_algebra(['+', '+'], [1, 2, 3]) == 3

def test_do_algebra_subtraction():
    assert do_algebra(['-', '-', '-'], [5, 3, 2]) == 0
    assert do_algebra(['-', '-'], [10, 5]) == 5

def test_do_algebra_multiplication():
    assert do_algebra(['*', '*', '*'], [2, 3, 4]) == 24
    assert do_algebra(['*', '*'], [1, 2]) == 2

def test_do_algebra_floor_division():
    assert do_algebra(['//', '//'], [10, 2]) == 5
    assert do_algebra(['//'], [15, 3]) == 5

def test_do_algebra_exponentiation():
    assert do_algebra(['**', '**'], [2, 3]) == 8
    assert do_algebra(['**'], [2, 2]) == 4

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '*', '-', '**'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 5]) == 11
    assert do_algebra(['**', '+', '*'], [2, 3, 4, 5]) == 14
    assert do_algebra(['-', '**', '*'], [5, 2, 3, 4]) == 17

def test_do_algebra_single_operand():
    assert do_algebra(['+', '*'], [1, 2, 3]) == 1 + 2 * 3

def test_do_algebra_empty_operator():
    assert do_algebra([], [1, 2, 3]) == 1

def test_do_algebra_empty_operand():
    assert do_algebra(['+', '*'], []) == None

def test_do_algebra_single_operator():
    assert do_algebra(['+'], [1, 2, 3]) == 1

def test_do_algebra_complex_expression():
    assert do_algebra(['*', '+', '//', '**'], [2, 3, 4, 5, 6]) == 144