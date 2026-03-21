import pytest

@pytest.mark.parametrize("string, substring, expected_count", [
    ("", "a", 0),
    ("aaa", "a", 3),
    ("aaaa", "aa", 3),
    ("ababab", "ab", 3),
    ("aaaaaa", "aaa", 4),
    ("abcdefg", "ab", 1),
    ("abcdefg", "xyz", 0),
    ("abcabcabc", "abc", 3),
    ("abcdef", "abcdef", 1),
    ("abcdef", "abcdefg", 0),
])
def test_how_many_times(string, substring, expected_count):
    assert how_many_times(string, substring) == expected_count

def test_how_many_times_empty_substring():
    with pytest.raises(ValueError):
        how_many_times("abc", "")

def test_how_many_times_none_input():
    with pytest.raises(TypeError):
        how_many_times(None, "abc")
    with pytest.raises(TypeError):
        how_many_times("abc", None)

def test_how_many_times_non_string_input():
    with pytest.raises(TypeError):
        how_many_times(123, "abc")
    with pytest.raises(TypeError):
        how_many_times("abc", 123)

def test_how_many_times_non_string_substring():
    with pytest.raises(TypeError):
        how_many_times("abc", 123)