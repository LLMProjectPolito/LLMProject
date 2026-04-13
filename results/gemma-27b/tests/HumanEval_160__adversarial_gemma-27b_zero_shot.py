
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
        raise ValueError("Operator and operand lists cannot be empty.")
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of operand list.")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands.")
    for num in operand:
        if not isinstance(num, int) or num < 0:
            raise ValueError("Operand list must contain non-negative integers.")

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
                raise ZeroDivisionError("Floor division by zero is not allowed.")
            result //= num
        elif op == '**':
            result **= num
        else:
            raise ValueError(f"Invalid operator: {op}")
    return result

class TestDoAlgebra:

    def test_addition(self):
        assert do_algebra(['+'], [2, 3]) == 5

    def test_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3

    def test_multiplication(self):
        assert do_algebra(['*'], [4, 5]) == 20

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5
        assert do_algebra(['//'], [11, 2]) == 5

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8

    def test_complex_expression(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    def test_multiple_operations(self):
        assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [5, 0])

    def test_empty_operator_list(self):
        with pytest.raises(ValueError):
            do_algebra([], [1, 2])

    def test_empty_operand_list(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [])

    def test_invalid_operator_length(self):
        with pytest.raises(ValueError):
            do_algebra(['+', '+'], [1, 2, 3])

    def test_invalid_operand_length(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [1])

    def test_negative_operand(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [-1, 2])

    def test_non_integer_operand(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [1.5, 2])

    def test_invalid_operator(self):
        with pytest.raises(ValueError):
            do_algebra(['$'], [1, 2])