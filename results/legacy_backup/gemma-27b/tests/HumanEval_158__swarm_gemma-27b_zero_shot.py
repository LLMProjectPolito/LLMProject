import pytest

def test_empty_string_in_list():
    words = ["", "abc", "def"]
    assert find_max(words) == "abc"