import pytest
import math

def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["abc", "ab", "abcd", "a"]) == ["ab", "abcd"]
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange"]) == ["kiwi", "apple", "orange"]
    assert sorted_list_sum(["hello", "world", "python"]) == ["hello", "python"]

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []