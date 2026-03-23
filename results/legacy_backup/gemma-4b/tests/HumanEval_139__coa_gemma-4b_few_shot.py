import pytest
import math


# Focus: Boundary Values
def test_special_factorial_zero():
    assert special_factorial(0) == 1

def test_special_factorial_one():
    assert special_factorial(1) == 1

def test_special_factorial_small():
    assert special_factorial(4) == 288

# Focus: Type Scenarios
def test_special_factorial_positive():
    assert special_factorial(4) == 288

def test_special_factorial_one():
    assert special_factorial(1) == 1

# Focus: Logic Branches
def test_special_factorial_positive():
    assert special_factorial(4) == 288

def test_special_factorial_one():
    assert special_factorial(1) == 1

def test_special_factorial_zero():
    assert special_factorial(0) == 1