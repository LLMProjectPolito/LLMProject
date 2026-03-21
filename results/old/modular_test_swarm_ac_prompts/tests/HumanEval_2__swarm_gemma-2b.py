import pytest
import math

def test_truncate_number_zero():
    """ Test that the decimal part is correctly calculated for zero. """
    assert truncate_number(0.0) == 0.0

def test_truncate_number_edge_case():
    """ Test edge case: number is exactly 1.0 """
    assert truncate_number(1.0) == 0.0