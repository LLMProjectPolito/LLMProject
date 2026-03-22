import pytest
import math


# Focus: Boundary Values
import pytest

def simplify(x, n):
    try:
        numerator, denominator = x.split('/')
        numerator, denominator = int(numerator), int(denominator)
        if denominator == 0:
            return False
        return numerator * denominator == int(numerator)
    except ValueError:
        return False

# Focus: Type Scenarios
import pytest

def simplify(x, n):
    try:
        numerator, denominator = x.split('/')
        numerator, denominator = int(numerator), int(denominator)
        if denominator == 0:
            return False
        return numerator * denominator == int(numerator)
    except ValueError:
        return False

# Focus: Logic Branches
import pytest

def simplify(x, n):
    try:
        numerator, denominator = x.split('/')
        numerator, denominator = int(numerator), int(denominator)
        if denominator == 0:
            return False
        return numerator * denominator == int(numerator)
    except ValueError:
        return False