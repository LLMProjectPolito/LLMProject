import pytest
import math

def test_pairs_sum_to_zero_edge_cases():
    # test case for edge condition where the list contains a single zero
    assert not pairs_sum_to_zero([0])
    # test case for empty list
    assert not pairs_sum_to_zero([])
    # test case for single element list
    assert not pairs_sum_to_zero([-10])