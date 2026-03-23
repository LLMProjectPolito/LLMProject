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
        num_str = str(num)
        den_str = str(den)
        
        if den_str == "0":
            return False
        
        numerator = int(num_str)
        denominator = int(den_str)
        
        if denominator == 0:
            return False
        
        return num * den == int(numerator * den)
    except ValueError:
        return False

def test_simplify_empty_input():
    assert simplify("", 5) == False
    assert simplify("1/5", "") == False
    assert simplify("", 0) == False
    assert simplify("1/5", "5/1") == False
    assert simplify("1/5", "5/1") == False
    assert simplify("1/5", "1/5") == False

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
    
    return numerator // common_divisor == denominator // common_divisor

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)