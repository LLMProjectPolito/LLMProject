import pytest

def test_find_max_tie_lexicographical():
    assert find_max(["abc", "bca", "cab"]) == "abc"