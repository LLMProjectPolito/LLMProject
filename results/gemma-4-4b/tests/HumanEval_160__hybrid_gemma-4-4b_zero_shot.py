
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
from your_module import do_algebra  # Replace your_module


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "-"], [2, 3, 4, 5], 9),
        (["+", "-", "*"], [10, 2, 3, 4], 26),
        (["*", "/", "+"], [5, 2, 3, 4], 17),
        (["//", "*", "+"], [10, 2, 3, 4], 26),
        (["**", "+", "-"], [2, 3, 4, 5], 9),
        (["+", "*"], [1, 2, 3], 7),
        (["-", "/"], [10, 2, 3], 4),
        (["*", "+", "**"], [2, 3, 4, 5], 129),
        (["+", "*", "//"], [10, 2, 3, 4], 26),
        (["-", "**", "+"], [2, 3, 4, 5], 12),
    ],
)
def test_do_algebra_basic(operator, operand, expected):
    assert do_algebra(operator, operand) == expected


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "-"], [0, 0, 0], 0),
        (["+", "-", "*"], [0, 0, 0], 0),
        (["*", "/", "+"], [0, 0, 0], 0),
        (["//", "*", "+"], [0, 0, 0], 0),
        (["**", "+", "-"], [0, 0, 0], 0),
    ],
)
def test_do_algebra_zero_operands(operator, operand, expected):
    assert do_algebra(operator, operand) == expected


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*"], [1, 2], 3),
        (["-", "/"], [10, 2], 4),
        (["*", "+", "**"], [2, 3, 4], 129),
        (["+", "*", "//"], [10, 2, 3], 26),
    ],
)
def test_do_algebra_short_operands(operator, operand, expected):
    assert do_algebra(operator, operand) == expected


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "-"], [1, 2, 3, 4, 5], 14),
        (["+", "*", "-"], [1, 2, 3, 4, 5, 6], 20),
        (["+", "*", "-"], [1, 2, 3, 4, 5, 6, 7], 26),
    ],
)
def test_do_algebra_long_operands(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["**"], [2], 4),
        (["//"], [10, 3], 3),
        (["*"], [5, 0], 0),
        (["+", "-"], [10, 5], 5),
    ],
)
def test_do_algebra_edge_cases(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "//"], [2, 3, 0], 0),
        (["+", "*", "**"], [2, 3, 0], 0),
        (["-", "/", "+"], [10, 0, 3], 4),
    ],
)
def test_do_algebra_division_by_zero(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "-"], [2, 3, 4, 5], -9),
    ],
)
def test_do_algebra_negative_result(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

Suite 2:
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
    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand list must contain only non-negative integers.")

    expression = ""
    for i in range(len(operator)):
        expression += str(operand[i])
        expression += operator[i]
        expression += str(operand[i+1])

    return eval(expression)


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "-"], [2, 3, 4, 5], 9),
        (["*", "+", "/"], [10, 2, 5, 1], 10),
        (["+", "-", "*"], [1, 2, 3, 4], 11),
        (["**", "+"], [2, 3], 10),
        (["//", "+"], [10, 3], 4),
        (["-", "*"], [5, 2, 3], -1),
        (["+", "]", "*"], [1,2,3,4], 11), #invalid operator
    ],
)
def test_do_algebra_valid(operator, operand, expected):
    assert do_algebra(operator, operand) == expected


@pytest.mark.parametrize(
    "operator, operand",
    [
        ([], [1, 2]),
        (["+", "*"], [1, 2, 3]),
        (["+", "*", "-"], [1, 2]),
    ],
)
def test_do_algebra_invalid_length(operator, operand):
    with pytest.raises(ValueError) as excinfo:
        do_algebra(operator, operand)
    assert "Length of operator list must be one less than the length of operand list." in str(excinfo.value)


@pytest.mark.parametrize(
    "operator, operand",
    [
        (["+", "*"], [1.5, 2]),
        (["+", "*"], [-1, 2]),
    ],
)
def test_do_algebra_invalid_operand_type(operator, operand):
    with pytest.raises(ValueError) as excinfo:
        do_algebra(operator, operand)
    assert "Operand list must contain only non-negative integers." in str(excinfo.value)

@pytest.mark.parametrize(
    "operator, operand",
    [
        (["+", "*"], []),
        ([], [1, 2]),
    ],
)
def test_do_algebra_empty_list(operator, operand):
    with pytest.raises(ValueError) as excinfo:
        do_algebra(operator, operand)
    assert "Operator and operand lists cannot be empty." in str(excinfo.value)

@pytest.mark.parametrize(
    "operator, operand",
    [
        (["+", "*", "//"], [10, 2, 5, 1]),
    ],
)
def test_do_algebra_multiple_operations(operator, operand):
    assert do_algebra(operator, operand) == 10