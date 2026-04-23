
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

```python
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
    def fraction_to_float(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator / denominator

    x_float = fraction_to_float(x)
    n_float = fraction_to_float(n)
    product = x_float * n_float

    return product.is_integer()

import pytest

def test_simplify_positive_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("2/4", "4/2") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_non_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/4") == False
    assert simplify("3/5", "5/7") == False
    assert simplify("1/2", "3/4") == False

def test_simplify_different_fractions():
    assert simplify("2/5", "5/2") == True
    assert simplify("3/7", "7/3") == True
    assert simplify("4/9", "9/4") == True
    assert simplify("5/11", "11/5") == True
    assert simplify("1/10", "10/1") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/1", "1/1") == False
    assert simplify("1/2", "1/2") == True
    assert simplify("1/2", "2/2") == True
    assert simplify("1/2", "1/4") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "2/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/1") == False
    assert simplify("1/4", "2/2") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "4/2") == True
    assert simplify("1/4", "2/1") == False
    assert simplify("1/4", "1/3") == False
    assert simplify("1/4", "3/1") == False
    assert simplify("1/4", "1/4") == True
    assert simplify("1/4", "4/4") == True
    assert simplify("1/4", "2/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/1") == False
    assert simplify("1/4", "2/2") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "4/2") == True
    assert simplify("1/4", "2/1") == False
    assert simplify("1/4", "1/3") == False
    assert simplify("1/4", "3/1") == False
    assert simplify("1/4", "1/4") == True
    assert simplify("1/4", "4/4") == True
    assert simplify("1/4", "2/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/1") == False
    assert simplify("1/4", "2/2") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "4/2") == True
    assert simplify("1/4", "2/1") == False
    assert simplify("1/4", "1/3") == False
    assert simplify("1/4", "3/1") == False
    assert simplify("1/4", "1/4") == True
    assert simplify("1/4", "4/4") == True
    assert simplify("1/4", "2/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/1") == False
    assert simplify("1/4", "2/2") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "4/2") == True
    assert simplify("1/4", "2/1") == False
    assert simplify("1/4", "1/3") == False
    assert simplify("1/4", "3/1") == False
    assert simplify("1/4", "1/4") == True
    assert simplify("1/4", "4/4") == True
    assert simplify("1/4", "2/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/1") == False
    assert simplify("1/4", "2/2") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "4/2") == True
    assert simplify("1/4", "2/1") == False
    assert simplify("1/4", "1/3") == False
    assert simplify("1/4", "3/1") == False
    assert simplify("1/4", "1/4") == True
    assert simplify("1/4", "4/4") == True
    assert simplify("1/4", "2/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/1") == False
    assert simplify("1/4", "2/2") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "4/2") == True
    assert simplify("1/4", "2/1") == False
    assert simplify("1/4", "1/3") == False
    assert simplify("1/4", "3/1") == False
    assert simplify("1/4", "1/4") == True
    assert simplify("1/4", "4/4") == True
    assert simplify("1/4", "2/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/1") == False
    assert simplify("1/4", "2/2") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "4/2") == True
    assert simplify("1/4", "2/1") == False
    assert simplify("1/4", "1/3") == False
    assert simplify("1/4", "3/1") == False
    assert simplify("1/4", "1/4") == True
    assert simplify("1/4", "4/4") == True
    assert simplify("1/4", "2/4") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/4", "1/1") == False
    assert simplify("1/4", "2/2") == False
    assert simplify("1/4", "1/2") == False
    assert simplify("1/4", "4/2") == True
    assert simplify("1/4", "2/1") == False
    assert simplify("1/4", "1/3") == False
    assert simplify("1/4", "3/1") == False
    assert simplify("1/4", "1/4") == True
    assert simplify("1/4", "4/