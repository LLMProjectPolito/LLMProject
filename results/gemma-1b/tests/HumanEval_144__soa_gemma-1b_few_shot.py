
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
import pytest

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
    try:
        numerator, denominator = x.split('/')
        if denominator == "":
            denominator = 1
        
        x_num = int(numerator)
        n_num = int(denominator)
        
        return math.gcd(x_num, n_num) == 1
    except ValueError:
        return False

def test_simplify_valid_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/10", "10/2") == False
    assert simplify("1/10", "2/10") == True
    assert simplify("1/10", "10/2") == False
    assert simplify("1/10", "10/1") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/10") == True
    assert simplify