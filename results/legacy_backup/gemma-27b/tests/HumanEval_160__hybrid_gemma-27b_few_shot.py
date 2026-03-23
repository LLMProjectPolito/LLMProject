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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

# Pytest Suite
def test_do_algebra_basic():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['+', '-'], [1, 2, 3]) == 0
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['-','+','*'], [10, 5, 2, 3]) == 11

def test_do_algebra_addition():
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['+', '+'], [1, 2, 3]) == 6

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3
    assert do_algebra(['-', '-'], [10, 2, 3]) == 5

def test_do_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['*', '*'], [2, 3, 4]) == 24

def test_do_algebra_division():
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['//', '//'], [20, 2, 5]) == 2

def test_do_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['**', '**'], [2, 3, 2]) == 64

def test_do_algebra_mixed():
    assert do_algebra(['+', '*', '-', '//'], [1, 2, 3, 4, 2]) == 3
    assert do_algebra(['**', '+', '*'], [2, 3, 4, 5]) == 89

def test_do_algebra_long_expression():
    operators = ['+', '-', '*', '//', '**']
    operands = [1, 2, 3, 4, 5, 6]
    assert do_algebra(operators, operands) == 10

def test_do_algebra_zero_division():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['$'], [1, 2])
    with pytest.raises(ValueError):
        do_algebra(['$'], [2, 3])

def test_do_algebra_invalid_input_length():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3])

def test_do_algebra_empty_operator():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_do_algebra_empty_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [])

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 2]) == 1
    assert do_algebra(['*', '+', '-'], [5, 2, 1, 3]) == 8

def test_do_algebra_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '*', '-', '//'], [1, 2, 3, 4, 2]) == 1
    assert do_algebra(['**', '+', '*'], [2, 3, 4, 5]) == 8 + 20

# Palindrome Tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_case_sensitive():
    assert is_palindrome('Racecar') == False

def test_palindrome_with_spaces():
    assert is_palindrome('A man a plan a canal Panama') == False

# Max Tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4