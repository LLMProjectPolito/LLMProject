
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
    expression = ""
    for i in range(len(operator)):
        expression += operator[i] + str(operand[i])
    return eval(expression)


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (
            ["+", "*"],
            [2, 3],
            5,
        ),
        (
            ["-", "/"],
            [10, 2],
            4,
        ),
        (
            ["**"],
            [2, 3],
            8,
        ),
        (
            ["+", "-", "*"],
            [1, 2, 3],
            4,
        ),
        (
            ["*", "+", "-"],
            [5, 2, 1],
            9,
        ),
        (
            ["//"],
            [10, 3],
            3,
        ),
        (
            ["+", "*", "//"],
            [10, 2, 3],
            10,
        ),
        (
            ["-", "**"],
            [2, 3],
            1,
        ),
        (
            ["+", "*", "//", "**"],
            [10, 2, 3, 4],
            20,
        ),
        (
            ["+", "*", "//", "**", "-"],
            [10, 2, 3, 4, 5],
            40,
        ),
    ],
)
def test_do_algebra(operator: List[str], operand: List[int], expected: int):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (
            ["+", "*"],
            [2],
            0,
        ),
        (
            ["-", "/"],
            [10],
            0,
        ),
        (
            ["**"],
            [2],
            0,
        ),
    ],
)
def test_invalid_operand_length(operator: List[str], operand: List[int], expected: int):
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (
            ["+", "*"],
            [2, 3, 4],
            10,
        ),
        (
            ["-", "/"],
            [10, 2, 3],
            4,
        ),
    ],
)
def test_invalid_operator_length(operator: List[str], operand: List[int], expected: int):
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (
            ["+", "*"],
            [2, 3, 4, 5],
            10,
        ),
        (
            ["-", "/"],
            [10, 2, 3, 4],
            4,
        ),
    ],
)
def test_invalid_operand_values(operator: List[str], operand: List[int], expected: int):
    with pytest.raises(TypeError):
        do_algebra(operator, operand)