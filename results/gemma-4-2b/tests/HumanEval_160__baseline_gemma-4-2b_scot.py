
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

# STEP 1: REASONING
# The function `do_algebra` takes an operator list and an operand list as input.
# It needs to evaluate an algebraic expression based on the operators and operands.
# The operators are used to combine the operands.
# The function should handle addition, subtraction, multiplication, floor division, and exponentiation.
# The test suite should cover various scenarios, including:
# - Basic arithmetic operations (addition, subtraction, multiplication)
# - Order of operations (parentheses are not explicitly handled, so we'll test with simple expressions)
# - Floor division
# - Exponentiation
# - Edge cases: empty operator list, empty operand list, invalid operator/operand values.
# - Test cases with different combinations of operators and operands.

# STEP 2: PLAN
# Test functions:
# - test_addition: Test addition operation.
# - test_subtraction: Test subtraction operation.
# - test_multiplication: Test multiplication operation.
# - test_floor_division: Test floor division operation.
# - test_exponentiation: Test exponentiation operation.
# - test_empty_operator: Test with an empty operator list.
# - test_empty_operand: Test with an empty operand list.
# - test_invalid_operator: Test with an invalid operator.
# - test_invalid_operand: Test with an invalid operand.
# - test_mixed_operations: Test with a combination of different operations.
# - test_complex_expression: Test with a more complex expression.

# STEP 3: CODE
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
        return 0  # Or raise an exception, depending on desired behavior

    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        val = operand[i + 1]
        if op == '+':
            result += val
        elif op == '-':
            result -= val
        elif op == '*':
            result *= val
        elif op == '//':
            result //= val
        elif op == '**':
            result **= val
    return result

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 2, 3], 5),
    (["-", 2, 3], -1),
    (["*", 2, 3], 6),
    (["//", 2, 3], 1),
    (["**", 2, 3], 8),
    (["+", 2, 3, 4], 9),
    (["-", 2, 3, 4], -5),
    (["*", 2, 3, 4], 24),
    (["//", 2, 3, 4], 0),
    (["**", 2, 3, 4], 16),
])
def test_addition(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["-", 2, 3], -1),
    (["-", 2, 3, 4], -5),
    (["-", 2, 3, 4], -5),
    (["-", 2, 3, 4], -5),
])
def test_subtraction(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["*", 2, 3], 6),
    (["*", 2, 3, 4], 24),
    (["*", 2, 3, 4], 24),
    (["*", 2, 3, 4], 24),
])
def test_multiplication(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["//", 2, 3], 1),
    (["//", 2, 3, 4], 0),
    (["//", 2, 3, 4], 0),
    (["//", 2, 3, 4], 0),
])
def test_floor_division(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["**", 2, 3], 8),
    (["**", 2, 3, 4], 16),
    (["**", 2, 3, 4], 16),
    (["**", 2, 3, 4], 16),
])
def test_exponentiation(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    ([], 2, 0),
    ([], 2, 0),
    ([], 2, 0),
    ([], 2, 0),
])
def test_empty_operator(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (2, 2, 0),
    (2, 2, 0),
    (2, 2, 0),
    (2, 2, 0),
])
def test_empty_operand(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["invalid", 2, 3], 0),
    (["invalid", 2, 3], 0),
    (["invalid", 2, 3], 0),
    (["invalid", 2, 3], 0),
])
def test_invalid_operator(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (2, ["invalid"], 0),
    (2, ["invalid"], 0),
    (2, ["invalid"], 0),
    (2, ["invalid"], 0),
])
def test_invalid_operand(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 2, "3"], 5),
    (["*", 2, "3"], 6),
    (["//", 2, "3"], 1),
    (["**", 2, "3"], 8),
])
def test_mixed_operations(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 2, 3, 4], 9),
    (["*", 2, 3, 4], 24),
    (["//", 2, 3, 4], 0),
    (["**", 2, 3, 4], 16),
])
def test_complex_expression(operator, operand, expected):
    assert do_algebra(operator, operand) == expected