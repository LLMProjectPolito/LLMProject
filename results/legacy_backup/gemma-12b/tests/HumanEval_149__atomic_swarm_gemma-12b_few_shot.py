import pytest
import math

def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "bb", "ccc"]) == []

def test_sorted_list_sum_mixed_types():
    assert sorted_list_sum(["aa", "a", 123, "aaa"]) == ["aa"]