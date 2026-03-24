
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

# Pytest Suite - Combined and Superior
class TestDoAlgebra:

    def test_basic_addition(self):
        assert do_algebra(['+'], [1, 2]) == 3

    def test_basic_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3

    def test_basic_multiplication(self):
        assert do_algebra(['*'], [3, 4]) == 12

    def test_basic_division(self):
        assert do_algebra(['//'], [10, 2]) == 5

    def test_basic_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8

    def test_complex_expression(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    def test_longer_expression(self):
        assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2]) == 1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [5, 0])

    def test_invalid_operator(self):
        with pytest.raises(ValueError):
            do_algebra(['%'], [5, 2])

    def test_empty_operator_list(self):
        with pytest.raises(ValueError):
            do_algebra([], [1, 2])

    def test_empty_operand_list(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [])

    def test_operator_length_mismatch(self):
        with pytest.raises(ValueError):
            do_algebra(['+', '-'], [1, 2, 3])

    def test_large_numbers(self):
        assert do_algebra(['*'], [1000, 1000]) == 1000000

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-', '//'], [10, 2, 3, 6, 2]) == 11

    def test_exponentiation_with_zero(self):
        assert do_algebra(['**'], [0, 5]) == 0

    def test_exponentiation_with_one(self):
        assert do_algebra(['**'], [5, 0]) == 1

    def test_do_algebra_basic(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
        assert do_algebra(['+', '-'], [1, 2, 3]) == 0
        assert do_algebra(['*'], [2, 3]) == 6

    def test_do_algebra_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8
        assert do_algebra(['+', '**'], [2, 3, 2]) == 11

    def test_do_algebra_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5
        assert do_algebra(['+', '//'], [10, 2, 3]) == 8

    def test_do_algebra_multiple_operations(self):
        assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 2]) == 1
        assert do_algebra(['*', '+', '-'], [5, 2, 1, 3]) == 8

    def test_do_algebra_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [10, 0])

    def test_do_algebra_invalid_operator(self):
        with pytest.raises(ValueError):
            do_algebra(['$'], [2, 3])

    def test_do_algebra_empty_operator(self):
        with pytest.raises(ValueError):
            do_algebra([], [2, 3])

    def test_do_algebra_empty_operand(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [])

    def test_do_algebra_invalid_length(self):
        with pytest.raises(ValueError):
            do_algebra(['+', '*'], [2, 3, 4])

    def test_do_algebra_large_numbers(self):
        assert do_algebra(['*'], [1000, 1000]) == 1000000

    def test_do_algebra_with_zero(self):
        assert do_algebra(['+', '*'], [0, 5, 2]) == 10
        assert do_algebra(['-', '*'], [10, 0, 2]) == 10
        assert do_algebra(['*'], [0, 5]) == 0

class TestPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None