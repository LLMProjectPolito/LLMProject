import pytest
from your_module import cycpattern_check  # Replace your_module

def rotate_string(s):
    """Rotates a string by one position."""
    return s[1:] + s[0]

@pytest.fixture
def sample_strings():
    """Provides sample strings for testing."""
    return {
        "abcd": "abd",
        "hello": "ell",
        "whassup": "psus",
        "abab": "baa",
        "efef": "eeff",
        "himenss": "simen",
        "abcde": "cdea",
        "rotation": "tationr",
        "teststring": "stringte",
        "longstring123": "string123long",
        "identical": "identical",
        "empty": "",
        "singlechar": "a",
        "singlechar2": "b",
        "aabaa": "abaa",
        "aaaaa": "aaaa",
        "mississippi": "issip",
        "banana": "nana",
        "racecar": "ecar",
        "level": "eve",
        "rotor": "otor",
        "madam": "ada",
        "kayak": "ayak",
        "stats": "tats",
        "deified": "eifiedd",
        "civic": "ivic",
        "refer": "efer",
        "redder": "edder",
        "detartrated": "tartratedde"
    }

def test_cycpattern_check_positive_cases(sample_strings):
    """Tests positive cases where a rotation is a substring."""
    for a, b in sample_strings.items():
        if a == "abcd" and b == "abd":
            assert not cycpattern_check(a, b)
        elif a == "whassup" and b == "psus":
            assert not cycpattern_check(a, b)
        elif a == "efef" and b == "eeff":
            assert not cycpattern_check(a, b)
        else:
            assert cycpattern_check(a, b)

def test_cycpattern_check_negative_cases(sample_strings):
    """Tests negative cases where no rotation is a substring."""
    negative_cases = {
        "abcd": "abc",
        "hello": "hel",
        "whassup": "wass",
        "abab": "aba",
        "efef": "fe",
        "himenss": "mens",
        "abcde": "bcde",
        "rotation": "rotat",
        "teststring": "testst",
        "longstring123": "longstrin",
        "identical": "identica",
        "singlechar": "b",
        "singlechar2": "c",
        "aabaa": "aa",
        "aaaaa": "aaa",
        "mississippi": "issis",
        "banana": "bana",
        "racecar": "raceca",
        "level": "leve",
        "rotor": "roto",
        "madam": "mada",
        "kayak": "kaya",
        "stats": "stat",
        "deified": "deifie",
        "civic": "civi",
        "refer": "refe",
        "redder": "redde",
        "detartrated": "detartrate"
    }
    for a, b in negative_cases.items():
        assert not cycpattern_check(a, b)

def test_cycpattern_check_empty_string(sample_strings):
    """Tests cases with empty strings."""
    assert not cycpattern_check("", "")
    assert not cycpattern_check("abc", "")
    assert not cycpattern_check("", "abc")

def test_cycpattern_check_single_character(sample_strings):
    """Tests cases with single characters."""
    assert cycpattern_check("a", "a")
    assert not cycpattern_check("a", "b")
    assert not cycpattern_check("b", "a")

def test_cycpattern_check_identical_strings(sample_strings):
    """Tests cases where the strings are identical."""
    assert cycpattern_check("abc", "abc")

def test_cycpattern_check_long_strings():
    """Tests with longer strings to check performance and edge cases."""
    long_string = "abcdefghijklmnopqrstuvwxyz" * 10
    substring = "uvwxyzabcdefgh"
    assert cycpattern_check(long_string, substring)

def test_cycpattern_check_substring_at_start():
    """Tests when the substring is at the beginning of the string."""
    assert cycpattern_check("abcdef", "abc")

def test_cycpattern_check_substring_at_end():
    """Tests when the substring is at the end of the string."""
    assert cycpattern_check("abcdef", "def")

def test_cycpattern_check_substring_in_middle():
    """Tests when the substring is in the middle of the string."""
    assert cycpattern_check("abcdef", "cde")