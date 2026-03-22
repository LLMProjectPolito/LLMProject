import pytest
import math


# Focus: Prime Number Determination
import pytest

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 7) == 5
    assert x_or_y(5, 1, 2) == 1
    assert x_or_y(11, 99, 100) == 99

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 3, 4) == 4
    assert x_or_y(9, 100, 1) == 1

def test_x_or_y_one():
    assert x_or_y(1, 5, 10) == 10

# Focus: Value Assignment Logic
def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(1, 9, 0) == 0

def test_x_or_y_one():
    assert x_or_y(1, 10, 20) == 20

# Focus: Input Data Types
def test_x_or_y_int_inputs():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(4, 100, 200) == 200

def test_x_or_y_float_inputs():
    assert x_or_y(7.0, 34.0, 12.0) == 34.0
    assert x_or_y(15.0, 8.0, 5.0) == 5.0

def test_x_or_y_mixed_inputs():
    assert x_or_y(7, 34.0, 12) == 34.0
    assert x_or_y(15.0, 8, 5.0) == 5.0