import pytest
import math

def test_truncate_number_zero():
    """ Test if the function correctly handles 0.0 (a very special case) """
    assert truncate_number(0.0) == 0.0

def test_truncate_number_floating_point_value():
    """ Test that decimal part is correctly truncated when given a floating point value at edge case of 1.0. """
    assert truncate_number(1.0) == 0.0, f"Expected decimal part of 1.0 to be 0.0, but got {truncate_number(1.0)}"