import pytest
import math

def test_special_factorial_basic():
    assert special_factorial(4) == 288

def test_special_factorial_one():
    assert special_factorial(1) == 1

import pytest

def test_special_factorial_negative():
    with pytest.raises(ValueError):
        special_factorial(-1)