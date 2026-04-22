
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
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += operator[i] + str(operand[i+1])

    return eval(expression)


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "-"], [2, 3, 4, 5], 9),
        (["*", "+", "//"], [10, 2, 4, 5], 20),
        (["**", "+"], [2, 3], 9),
        (["-", "*", "/"], [10, 2, 5], 0),  # Added test case for division
        (["+", "-", "*", "//"], [5, 2, 3, 4], 11),  # More complex expression
        (["**", "+", "*"], [2, 3, 2, 4], 28), #Another complex expression
        (["+", "*"], [1, 2, 3], 7),
        (["-", "+"], [5, 2, 3], 6),

    ],
)
def test_do_algebra_basic(operator, operand, expected):
    assert do_algebra(operator, operand) == expected


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "-"], [1, 2], -1),
        (["*", "/"], [10, 2], 5),
        (["**"], [2, 3], 8),
        (["//"], [10, 3], 3),
    ],
)
def test_do_algebra_negative_results(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "//", "**"], [1, 2, 3, 4, 5], 35),
        (["-", "/", "**"], [10, 2, 3, 4, 5], 1),
    ],
)
def test_do_algebra_complex_expression(operator, operand, expected):
    assert do_algebra(operator, operand) == expected


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+", "*", "//", "**"], [1, 2, 0, 4, 5], 0),
        (["-", "/", "**"], [10, 0, 3, 4, 5], float('inf')),
    ],
)
def test_do_algebra_edge_cases(operator, operand, expected):
    assert do_algebra(operator, operand) == expected


def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_case_insensitive():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == False #Needs preprocessing to handle spaces and punctuation

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_number():
    assert is_palindrome('121') == True

def test_palindrome_number_not():
    assert is_palindrome('123') == False


def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_single_element():
    assert get_max([5]) == 5