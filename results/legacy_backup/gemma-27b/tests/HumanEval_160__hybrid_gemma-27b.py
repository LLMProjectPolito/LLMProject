import pytest
from typing import List

def do_algebra(operator: List[str], operand: List[int]) -> int:
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
        if num < 0:
            raise ValueError("Operand list must contain non-negative integers.")

    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i + 1]
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

    def test_valid_expression(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
        assert do_algebra(['-','+','*'], [10, 5, 2, 3]) == 11
        assert do_algebra(['*','+','//'], [2, 3, 4, 2]) == 8
        assert do_algebra(['**','-','+'], [2, 3, 4, 5]) == 3
        assert do_algebra(['+'], [1, 2]) == 3
        assert do_algebra(['-'], [5, 2]) == 3
        assert do_algebra(['*'], [3, 4]) == 12
        assert do_algebra(['//'], [10, 2]) == 5
        assert do_algebra(['**'], [2, 3]) == 8

    def test_multiple_operations(self):
        assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10
        assert do_algebra(['*', '*', '*'], [2, 2, 2, 2]) == 16
        assert do_algebra(['-', '-', '-'], [5, 1, 1, 1]) == 2

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-', '//'], [1, 2, 3, 4, 2]) == 3
        assert do_algebra(['**', '+', '*'], [2, 2, 3, 4]) == 20

    def test_zero_operand(self):
        assert do_algebra(['+', '*'], [0, 5, 2]) == 0
        assert do_algebra(['-', '*'], [10, 0, 2]) == 10
        assert do_algebra(['*','+'], [0, 5, 2]) == 0

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 3]) == 3
        assert do_algebra(['+', '//'], [10, 3, 2]) == 5
        assert do_algebra(['//', '+'], [10, 2, 3]) == 8

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8
        assert do_algebra(['+', '**'], [2, 3, 2]) == 11
        assert do_algebra(['**', '+'], [2, 2, 3]) == 7

    def test_invalid_input_empty_lists(self):
        with pytest.raises(ValueError):
            do_algebra([], [1, 2])
        with pytest.raises(ValueError):
            do_algebra(['+'], [])

    def test_invalid_input_length_mismatch(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [1, 2, 3])
        with pytest.raises(ValueError):
            do_algebra(['+', '*'], [1, 2])

    def test_invalid_input_operand_length_less_than_2(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [1])

    def test_invalid_input_negative_operand(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [-1, 2])
        with pytest.raises(ValueError):
            do_algebra(['+', '*'], [1, -2, 3])

    def test_invalid_operator(self):
        with pytest.raises(ValueError):
            do_algebra(['$'], [1, 2])

    def test_floor_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [10, 0])

    def test_valid_input_addition(self):
        assert do_algebra(['+'], [2, 3]) == 5

    def test_valid_input_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3

    def test_valid_input_multiplication(self):
        assert do_algebra(['*'], [4, 5]) == 20

    def test_valid_input_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5

    def test_valid_input_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8

    def test_valid_input_complex_expression(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    def test_valid_input_multiple_operations(self):
        assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 1

    def test_valid_input_zero_operand(self):
        assert do_algebra(['+'], [0, 5]) == 5
        assert do_algebra(['*'], [0, 10]) == 0

    def test_valid_input_large_numbers(self):
        assert do_algebra(['+'], [1000000, 2000000]) == 3000000

    def test_valid_input_mixed_operations(self):
        assert do_algebra(['*', '+', '-'], [2, 3, 4, 1]) == 7

    def test_floor_division_by_one(self):
        assert do_algebra(['//'], [10, 1]) == 10

    def test_exponentiation_with_zero(self):
        assert do_algebra(['**'], [2, 0]) == 1

    def test_exponentiation_with_one(self):
        assert do_algebra(['**'], [5, 1]) == 5

    def test_multiple_exponentiations(self):
        assert do_algebra(['**', '**'], [2, 2, 3]) == 16

    def test_mixed_exponentiation_and_addition(self):
        assert do_algebra(['**', '+'], [2, 3, 4]) == 12

    def test_negative_result(self):
        assert do_algebra(['-', '+'], [10, -5, 2]) == 7

    def test_zero_division_error(self):
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
            do_algebra(['+', '-'], [1, 2, 3])

    def test_invalid_operand_length(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [1])

    def test_negative_operand(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [1, -2])

    def test_invalid_operator(self):
        with pytest.raises(ValueError):
            do_algebra(['$'], [1, 2])