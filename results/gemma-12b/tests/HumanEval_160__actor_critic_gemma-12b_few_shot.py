
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
                return float('inf')  # Handle division by zero
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result


@pytest.mark.parametrize("operator, operand, expected", [
    (['+'], [2, 3], 5),  # Basic addition
    (['*'], [2, 3], 6),  # Basic multiplication
    (['-'], [5, 2], 3),  # Basic subtraction
    (['//'], [10, 2], 5), # Basic floor division
    (['**'], [2, 3], 8),  # Basic exponentiation
    (['+', '*', '-'], [2, 3, 4, 5], 9),  # Mixed operations
    (['+', '-', '*'], [1, 2, 3, 4], -3), # Mixed operations different order
    (['//', '+'], [10, 2, 5], 5), # Floor division then addition
    (['+', '//'], [5, 2, 3], 8), # Addition then floor division
    (['+', '*', '//'], [2, 3, 4, 5], 11), # Mixed operations
    (['+'], [1000, 2000], 3000), # Large numbers
    (['*'], [1000, 1000], 1000000), # Large numbers
    (['**'], [2, 10], 1024), # Exponentiation with larger exponent
    (['//'], [10, 0], float('inf')),  # Division by zero
    (['**'], [2, 0], 1),  # Exponentiation with zero exponent
    (['-'], [2, -3], 5), # Negative operand
    (['*'], [2, -3], -6), # Negative operand
    (['//'], [10, -3], -4), # Floor division with negative numbers
    (['+', '-'], [5, 2, 1], 4), # Multiple operators
    (['*','+'], [2,3,4], 14), # Multiple operators
])
def test_do_algebra(operator, operand, expected):
    """Tests the do_algebra function with various scenarios."""
    assert do_algebra(operator, operand) == expected

def test_do_algebra_single_operator():
    """Tests the do_algebra function with only one operator."""
    assert do_algebra(['+'], [1, 2]) == 3

# The following tests are commented out because the problem description states that the lists won't be empty.
# However, they are included to demonstrate how to test these boundary conditions.
# def test_do_algebra_empty_operator():
#     """Tests the do_algebra function with an empty operator list."""
#     with pytest.raises(IndexError):
#         do_algebra([], [1])
#
# def test_do_algebra_empty_operand():
#     """Tests the do_algebra function with an empty operand list."""
#     with pytest.raises(IndexError):
#         do_algebra(['+'], [])