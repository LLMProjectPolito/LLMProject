
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
    if len(operand) == 0:
        return None

    if len(operand) == 1:
        return operand[0]

    if len(operator) == 0:
        return None

    if len(operator) == 1:
        return operator[0]

    if len(operator) == 2:
        try:
            return float(operand[0]) + float(operand[1])
        except:
            return None

    if len(operator) == 3:
        try:
            return float(operand[0]) * float(operand[1]) + float(operand[2])
        except:
            return None

    if len(operator) == 4:
        try:
            return float(operand[0]) * float(operand[1]) * float(operand[2]) + float(operand[3])
        except:
            return None

    return None

def test_do_algebra():
    assert do_algebra('+ 2 3' == 5)
    assert do_algebra('- 2 3' == 1)
    assert do_algebra('* 2 3' == 6)
    assert do_algebra('-- 2 3' == 1)
    assert do_algebra('2 3' == 5)
    assert do_algebra('2 3 4' == 10)
    assert do_algebra('2 3 4 5' == 15)
    assert do_algebra('2 3 4 5 6' == 20)
    assert do_algebra('2 3 4 5 6 7' == 21)
    assert do_algebra('2 3 4 5 6 7 8' == 24)
    assert do_algebra('2 3 4 5 6 7 8 9' == 27)
    assert do_algebra('2 3 4 5 6 7 8 9 10' == 30)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11' == 33)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11 12' == 36)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11 12 13' == 39)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11 12 13 14' == 42)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11 12 13 14 15' == 45)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11 12 13 14 15 16' == 48)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17' == 51)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18' == 54)
    assert do_algebra('2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19' == 57)
    print("All tests passed!")

def test_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_longer():
    assert is_palindrome('racecar') == True
    assert is_palindrome('level') == True

def test_palindrome_short():
    assert is_palindrome('abc') == False

def test_do_algebra_basic():
    assert do_algebra('+ 2 3' == 5)
    assert do_algebra('- 2 3' == 1)
    assert do_algebra('* 2 3' == 6)
    assert do_algebra('/') 2 3 == 1
    assert do_algebra('2 3' == 5)
    assert do_algebra('2 3 4' == 10)
    assert do_algebra('2 3 4 5' == 15)
    assert do_algebra('2 3 4 5 6' == 20)
    assert do_algebra('2 3 4 5 6 7' == 21)
    assert do_algebra('2 3 4 5 6 7 8' == 24)
    assert do_algebra('2 3 4 5 6 7 8 9' == 27)
    print("All tests passed!")

def test_max():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) is None

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4