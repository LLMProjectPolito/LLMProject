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
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `do_algebra` evaluates an algebraic expression given lists of operators and operands.
# Constraints:
# - Operators are basic arithmetic operations (+, -, *, //, **).
# - Operands are non-negative integers.
# - The number of operators is one less than the number of operands.
# - Operator list has at least one operator, and operand list has at least two operands.

# STEP 2: PLAN - List test functions names and scenarios.
# Test Cases:
# 1. Basic addition: ['+'], [1, 2] -> 3
# 2. Basic subtraction: ['-'], [5, 3] -> 2
# 3. Basic multiplication: ['*'], [2, 4] -> 8
# 4. Basic floor division: ['//'], [10, 2] -> 5
# 5. Basic exponentiation: ['**'], [2, 3] -> 8
# 6. Combined operations: ['+', '*', '-'], [2, 3, 4, 5] -> 9
# 7. Multiple additions: ['+', '+'], [1, 2, 3] -> 6
# 8. Multiple subtractions: ['-', '-'], [5, 2, 1] -> 2
# 9. Mixed operations with floor division: ['+', '//'], [10, 2, 3] -> 6
# 10. Mixed operations with exponentiation: ['*', '**'], [2, 3, 2] -> 18
# 11. Zero operand: ['+'], [0, 5] -> 5
# 12. Zero as result: ['-', '+'], [5, 2, -7] -> 0
# 13. Edge case: ['//'], [5, 0] -> ZeroDivisionError (handled with pytest.raises)
# 14. Edge case: ['**'], [2, 0] -> 1
# 15. Longer expression: ['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5, 2] -> 1

# STEP 3: CODE - Write the high-quality pytest suite.
def test_basic_addition():
    assert do_algebra(['+'], [1, 2]) == 3

def test_basic_subtraction():
    assert do_algebra(['-'], [5, 3]) == 2

def test_basic_multiplication():
    assert do_algebra(['*'], [2, 4]) == 8

def test_basic_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_basic_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_combined_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_multiple_additions():
    assert do_algebra(['+', '+'], [1, 2, 3]) == 6

def test_multiple_subtractions():
    assert do_algebra(['-', '-'], [5, 2, 1]) == 2

def test_mixed_operations_floor_division():
    assert do_algebra(['+', '//'], [10, 2, 3]) == 6

def test_mixed_operations_exponentiation():
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18

def test_zero_operand():
    assert do_algebra(['+'], [0, 5]) == 5

def test_zero_as_result():
    assert do_algebra(['-', '+'], [5, 2, -7]) == 0

def test_floor_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_exponentiation_zero_exponent():
    assert do_algebra(['**'], [2, 0]) == 1

def test_longer_expression():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5, 2]) == 1