import pytest
import math


# Focus: Boundary Values
def simplify(x, n):
    try:
        x_int = int(x)
        n_int = int(n)
        if x_int == 0 or n_int == 0:
            return False
        
        numerator = x_int
        denominator = n_int
        
        if denominator == 0:
            return False
        
        common_divisor = gcd(numerator, denominator)
        
        return numerator // common_divisor == denominator // common_divisor
    except:
        return False

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Focus: Type Scenarios
def simplify(x, n):
    try:
        x_int = int(x)
        n_int = int(n)
        if x_int == 0 or n_int == 0:
            return False
        return x_int * n_int == int(x_int * n_int)
    except:
        return False

# Focus: Logic Branches
def simplify(x, n):
    """Simplifies the expression x * n."""
    try:
        x_val = int(x)
        n_val = int(n)
        if x_val == 0 or n_val == 0:
            return False
        return x_val * n_val == 0
    except ValueError:
        return False