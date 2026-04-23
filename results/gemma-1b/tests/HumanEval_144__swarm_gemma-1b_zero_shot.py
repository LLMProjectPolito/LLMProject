
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

import pytest
import math

def simplify(expression, num_str):
    """
    Simplifies a mathematical expression.

    Args:
        expression (str): The expression to simplify.
        num_str (str): The number string to use for simplification.

    Returns:
        bool: True if the expression is valid, False otherwise.
    """
    try:
        result = eval(expression, {'num': num_str})
        return result == num_str
    except Exception as e:
        return False

def test_simplify_with_edge_case():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/1") == True

    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "6/1") == False
    assert simplify("1/7", "7/1") == True
    assert simplify("1/8", "8/1") == True
    assert simplify("1/9", "9/1") == True
    assert simplify("1/10", "10/1") == True
    assert simplify("1/10", "10/1") == True
    assert simplify("1/10", "10/2") == False
    assert simplify("1/10", "20/1") == False

    # Add more tests as needed
    print("All tests passed!")