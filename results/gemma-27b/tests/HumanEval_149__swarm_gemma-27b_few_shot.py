import pytest

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["abc", "def", "ghi", "abc"]) == ["abc", "abc", "def", "ghi"]