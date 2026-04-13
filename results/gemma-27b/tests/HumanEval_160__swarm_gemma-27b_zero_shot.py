
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

def test_empty_operator_list_with_two_operands():
    """Test case for an empty operator list with only two operands."""
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
    
    operator = []
    operand = [5, 2]
    assert do_algebra(operator, operand) == 5

def test_empty_operator_list():
    """Test case for an empty operator list with two operands."""
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
    
    with pytest.raises(IndexError):
        do_algebra([], [5, 2])