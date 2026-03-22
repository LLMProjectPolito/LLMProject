import pytest
import math

def test_sum_squares_mixed_signs_and_zero():
    assert sum_squares([-1, 0, 2, -3, 4, -5]) == -125