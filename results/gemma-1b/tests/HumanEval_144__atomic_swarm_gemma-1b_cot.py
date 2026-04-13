
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
    x_val = str(x)
    n_val = str(n)
    
    try:
        num, den = map(int, x_val.split("/"))
        den_val = int(den)
        
        if den_val == 0:
            return False
        
        return num * den_val == int(num * den_val)
    except ValueError:
        return False

def test_simplify():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/2", "2/2") == True
    assert simplify("1/4", "4/2") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/5", "1/5") == True
    assert simplify("1/10", "10/1") == True
    assert simplify("1/10", "10/10") == True
    assert simplify("1/10", "10/2") == False
    assert simplify("1/10", "2/10") == False
    assert simplify("1/10", "10/10") == False
    assert simplify("1/10", "10/10") == False
    assert simplify("1/10", "10/1") == False
    assert simplify("1/10", "1/1") == False
    assert simplify("1/10", "1") == False
    assert simplify("1/10", "10") == False
    assert simplify("1/10", "100") == False
    assert simplify("1/10", "1000") == False
    assert simplify("1/10", "10000") == False
    assert simplify("1/10", "100000") == False
    assert simplify("1/10", "1000000") == False
    assert simplify("1/10", "10000000") == False
    assert simplify("1/10", "100000000") == False
    assert simplify("1/10", "1000000000") == False
    assert simplify("1/10", "10000000000") == False
    assert simplify("1/10", "10000000000") == False
    assert simplify("1/10", "100000000000") == False
    assert simplify("1/10", "100000000000") == False
    assert simplify("1/10", "1000000000000") == False
    assert simplify("1/10", "10000000000000") == False
    assert simplify("1/10", "100000000000000") == False
    assert simplify("1/10", "1000000000000000") == False
    assert simplify("1/10", "10000000000000000") == False
    assert simplify("1/10", "100000000000000000") == False
    assert simplify("1/10", "1000000000000000000") == False
    assert simplify("1/10", "10000000000000000000") == False
    assert simplify("1/10", "100000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000") == False
    assert simplify("1/10", "10000000000000000000000") == False
    assert simplify("1/10", "100000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000") == False
    assert simplify("1/10", "10000000000000000000000000") == False
    assert simplify("1/10", "100000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000") == False
    assert simplify("1/10", "10000000000000000000000000000") == False
    assert simplify("1/10", "100000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000") == False
    assert simplify("1/10", "10000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000") == False
    assert simplify("1/10", "10000000000000000000000000000000000") == False
    assert simplify("1/10", "100000000000000000000000000000000000") == False
    assert simplify("1/10", "100000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000000") == False
    assert simplify("1/10", "10000000000000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000000000000000000000000000000000000") == False
    assert simplify("1/10", "1000000000000000000

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
    x_val = int(x)
    n_val = int(n)

    if x_val == 0 or n_val == 0:
        return False

    numerator = x_val
    denominator = n_val

    if denominator == 0:
        return False

    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor

    return numerator == denominator
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)