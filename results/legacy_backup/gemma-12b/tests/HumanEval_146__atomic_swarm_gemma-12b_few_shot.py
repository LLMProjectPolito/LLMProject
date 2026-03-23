import pytest
import math

def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_all_negative():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_specialFilter_wrong_type():
    assert specialFilter([15, -73, 14, -15, "abc"]) == 1