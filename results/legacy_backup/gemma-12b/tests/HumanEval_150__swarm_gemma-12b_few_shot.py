import pytest
import math

def test_x_or_y_edge_case_n_is_one():
    assert x_or_y(1, 5, 10) == 10