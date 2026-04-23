
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
    expression = ""
    for i in range(len(operator)):
        expression += operator[i] + str(operand[i])
    try:
        return eval(expression)
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        return None


# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `do_algebra` takes two lists, `operator` and `operand`, representing an algebraic expression.
# It evaluates this expression using the provided operators and operands.  The constraints are:
# - Length of `operator` is one less than the length of `operand`.
# - `operand` contains non-negative integers.
# - `operator` is not empty.
# - `operand` has at least two elements.
# - The expression must be valid Python code.
# - The function should return the result of the expression, or None if an error occurs.

# STEP 2: PLAN - List test functions names and scenarios.
# 1. Basic addition: Check addition with positive integers.
# 2. Basic subtraction: Check subtraction with positive integers.
# 3. Basic multiplication: Check multiplication with positive integers.
# 4. Basic floor division: Check floor division with positive integers.
# 5. Basic exponentiation: Check exponentiation with positive integers.
# 6. Mixed operations: Check combinations of different operators (addition, subtraction, multiplication, floor division, exponentiation)
# 7. Edge cases:
#    - Zero operands: Check if the function handles zero operands gracefully (should return None).
#    - Empty operator list: Check if the function handles an empty operator list gracefully (should return None).
#    - Invalid operator list: Check if the function handles an invalid operator list gracefully (should return None).
#    - Invalid operand list (e.g., negative numbers, non-integers): Check if the function handles invalid operand lists gracefully (should return None).
#    - Division by zero: Check if the function handles division by zero gracefully (should return None).
# 8. Large numbers: Check if the function handles large numbers without overflow.
# 9. Different order of operations: Check if the order of operations is respected.

# STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (
            ["+", "*"],
            [2, 3],
            5,
        ),
        (
            ["-", "*"],
            [5, 2],
            10,
        ),
        (
            ["+", "-"],
            [10, 5],
            5,
        ),
        (
            ["*", "/"],
            [10, 2],
            5,
        ),
        (
            ["**"],
            [2, 3],
            8,
        ),
        (
            ["+", "*", "-"],
            [2, 3, 4],
            14,
        ),
        (
            ["+", "*", "//"],
            [10, 2, 3],
            6,
        ),
        (
            ["+", "*", "//"],
            [10, 2, 3],
            6,
        ),
        (
            ["+", "*", "//", "**"],
            [10, 2, 3, 4],
            42,
        ),
        (
            ["+", "*", "//", "**", "-"],
            [10, 2, 3, 4, 5],
            54,
        ),
        (
            ["+", "*", "//", "**", "-"],
            [10, 2, 3, 4, 5],
            54,
        ),
    ],
)
def test_do_algebra_basic(operator, operand, expected):
    result = do_algebra(operator, operand)
    assert result == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        ([], [2, 3], None),
        (["+", "*"], [], None),
        (["+", "*"], [2], None),
    ],
)
def test_do_algebra_invalid_input(operator, operand, expected):
    result = do_algebra(operator, operand)
    assert result == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*"], [2, -3], None),
        (["+", "*"], [2, 3.5], None),
    ],
)
def test_do_algebra_invalid_operand(operator, operand, expected):
    result = do_algebra(operator, operand)
    assert result == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*"], [2, 0], None),
        (["+", "*"], [2, 1], None),
    ],
)
def test_do_algebra_division_by_zero(operator, operand, expected):
    result = do_algebra(operator, operand)
    assert result == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*"], [1000000, 2000000], 3000000),
    ],
)
def test_do_algebra_large_numbers(operator, operand, expected):
    result = do_algebra(operator, operand)
    assert result == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "//"], [10, 2, 3], 6),
        (["+", "*", "//"], [10, 2, 3], 6),
    ],
)
def test_do_algebra_order_of_operations(operator, operand, expected):
    result = do_algebra(operator, operand)
    assert result == expected