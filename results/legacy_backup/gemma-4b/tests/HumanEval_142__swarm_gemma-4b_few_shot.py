import pytest
import math

def test_sum_squares_edge_case():
    lst = [1, 2, 3, 4, 5, 6]
    expected_sum = 1 + 4 + 9 + 64 + 25 + 36
    assert sum_squares(lst) == expected_sum