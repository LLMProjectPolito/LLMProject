import pytest

def test_empty_list():
    assert sum_squares([]) == 0

def test_edge_case_multiple_of_3_and_4():
    assert sum_squares([2, 4, 6, 8, 10, 12]) == 2**2 + 4**2 + 6**2 + 8**2 + 10**2 + 12**2