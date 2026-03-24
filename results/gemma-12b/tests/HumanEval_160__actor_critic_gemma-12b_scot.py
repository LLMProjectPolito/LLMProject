
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
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of operand list.")
    if not operator:
        raise ValueError("Operator list cannot be empty.")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands.")

    valid_operators = ['+', '-', '*', '//', '**']
    for op in operator:
        if op not in valid_operators:
            raise ValueError("Invalid operator: {}".format(op))

    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            if operand[i+1] == 0:
                raise ZeroDivisionError("Division by zero")
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

class TestDoAlgebra:
    def test_addition(self):
        assert do_algebra(['+'], [2, 3]) == 5
        assert do_algebra(['+', '+'], [1, 2, 3]) == 6

    def test_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3
        assert do_algebra(['-', '-'], [10, 5, 2]) == 3

    def test_multiplication(self):
        assert do_algebra(['*'], [2, 3]) == 6
        assert do_algebra(['*', '*',], [1, 2, 3]) == 6

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5
        assert do_algebra(['//', '//'], [20, 4, 2]) == 2
        assert do_algebra(['//'], [10, 3]) == 3
        assert do_algebra(['//'], [-10, 3]) == -4
        assert do_algebra(['//'], [10, -3]) == -4
        assert do_algebra(['//'], [-10, -3]) == 3

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8
        assert do_algebra(['**', '**'], [2, 2, 2]) == 16

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
        assert do_algebra(['-', '+', '*'], [10, 2, 3, 4]) == 14
        assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 4
        assert do_algebra(['//', '*', '+'], [10, 2, 3, 5]) == 5
        assert do_algebra(['+', '*',], [2, 3, 4]) == 14

    def test_exponentiation_with_multiplication(self):
        assert do_algebra(['*','**'], [2, 3, 2]) == 32

    def test_large_numbers(self):
        assert do_algebra(['+'], [1000000, 2000000]) == 3000000
        assert do_algebra(['*'], [100, 1000]) == 100000

    def test_empty_operator_list(self):
        with pytest.raises(ValueError) as excinfo:
            do_algebra([], [1, 2])
        assert "Operator list cannot be empty." in str(excinfo.value)

    def test_empty_operand_list(self):
        with pytest.raises(ValueError) as excinfo:
            do_algebra(['+'], [])
        assert "Operand list must have at least two operands." in str(excinfo.value)

    def test_mismatched_lengths(self):
        with pytest.raises(ValueError) as excinfo:
            do_algebra(['+', '*'], [1, 2])
        assert "Length of operator list must be one less than the length of operand list." in str(excinfo.value)

    def test_invalid_operator(self):
        with pytest.raises(ValueError) as excinfo:
            do_algebra(['$'], [1, 2])
        assert "Invalid operator: $" in str(excinfo.value)

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError) as excinfo:
            do_algebra(['//'], [10, 0])
        assert "Division by zero" in str(excinfo.value)

    def test_negative_numbers(self):
        assert do_algebra(['+'], [-2, 3]) == 1
        assert do_algebra(['-'], [5, -2]) == 7
        assert do_algebra(['*'], [-2, 3]) == -6
        assert do_algebra(['//'], [10, -3]) == -4

    def test_exponentiation_with_negative_base(self):
        assert do_algebra(['**'], [-2, 3]) == -8

    def test_exponentiation_with_zero_exponent(self):
        assert do_algebra(['**'], [5, 0]) == 1

    def test_floor_division_with_negative_numbers(self):
        assert do_algebra(['//'], [-10, 3]) == -4

    def test_single_operator(self):
        assert do_algebra(['+'], [1, 2]) == 3

    def test_exponentiation_with_negative_exponent(self):
        with pytest.raises(ValueError) as excinfo:
            do_algebra(['**'], [2, -3])
        assert "Invalid operator: **" in str(excinfo.value)

    def test_exponentiation_with_non_integer_exponent(self):
        with pytest.raises(ValueError) as excinfo:
            do_algebra(['**'], [2, 2.5])
        assert "Invalid operator: **" in str(excinfo.value)