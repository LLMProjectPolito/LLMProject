import pytest
import math

def test_sorted_list_sum_with_duplicates_and_same_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_with_duplicates_and_same_length_4():
    assert sorted_list_sum(["aa", "bb", "cc", "dd"]) == ["aa", "bb", "cc", "dd"]