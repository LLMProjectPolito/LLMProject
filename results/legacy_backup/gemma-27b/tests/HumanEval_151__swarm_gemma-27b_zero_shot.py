import pytest

def test_empty_list():
    assert double_the_difference([]) == 0

def test_large_odd_number():
    assert double_the_difference([1000000001]) == 1000000002000000001