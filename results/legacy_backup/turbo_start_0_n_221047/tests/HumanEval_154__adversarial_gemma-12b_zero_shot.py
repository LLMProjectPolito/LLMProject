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
        "abc": "cab",
        "a": "a",
        "aa": "aa",
        "aaa": "aaa",
        "aaaa": "aaaa",
        "abcabc": "bca",
        "longstring": "string",
        "longstring": "gstringl",
        "longstring": "longstri",
        "longstring": "ngstring",
        "longstring": "stringl",
        "longstring": "longstrin",
        "longstring": "g",
        "longstring": "l",
        "longstring": "o",
        "longstring": "n",
        "longstring": "g",
        "longstring": "s",
        "longstring": "t",
        "longstring": "r",
        "longstring": "i",
        "longstring": "n",
        "longstring": ""
    }

def test_cycpattern_check_positive_cases(sample_strings):
    """Tests positive cases where the second word or its rotation is a substring."""
    for a, b in sample_strings.items():
        if a == "abcd" and b == "abd":
            continue
        if a == "whassup" and b == "psus":
            continue
        if a == "efef" and b == "eeff":
            continue
        assert cycpattern_check(a, b) == True

def test_cycpattern_check_negative_cases(sample_strings):
    """Tests negative cases where the second word or its rotation is not a substring."""
    for a, b in sample_strings.items():
        if a == "abcd" and b == "abd":
            assert cycpattern_check(a, b) == False
        if a == "whassup" and b == "psus":
            assert cycpattern_check(a, b) == False
        if a == "efef" and b == "eeff":
            assert cycpattern_check(a, b) == False

def test_cycpattern_check_empty_string(sample_strings):
    """Tests cases with empty strings."""
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False
    assert cycpattern_check("", "") == False

def test_cycpattern_check_single_character(sample_strings):
    """Tests cases with single characters."""
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("b", "a") == False

def test_cycpattern_check_same_string(sample_strings):
    """Tests cases where both strings are the same."""
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("aaaa", "aaaa") == True

def test_cycpattern_check_rotation(sample_strings):
    """Tests cases involving rotations."""
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abcd", "bcda") == True
    assert cycpattern_check("abcd", "cdab") == True
    assert cycpattern_check("abcd", "dabc") == True
    assert cycpattern_check("abcd", "abcd") == True

def test_cycpattern_check_long_string_rotation(sample_strings):
    """Tests rotations with longer strings."""
    a = "longstring"
    b = "gstringl"
    assert cycpattern_check(a, b) == True

    b = "longstri"
    assert cycpattern_check(a, b) == True

    b = "ngstring"
    assert cycpattern_check(a, b) == True

    b = "stringl"
    assert cycpattern_check(a, b) == True

    b = "longstrin"
    assert cycpattern_check(a, b) == True