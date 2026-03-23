import pytest

def solve(s):
    """
    Reverses the case of letters in a string.

    Args:
        s: The input string.

    Returns:
        The reversed string.
    """
    if not s:
        return s[::-1]

    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
        elif 'A' <= char <= 'Z':
            result += char.lower()
        else:
            result += char

    return result

def test_empty_string():
    assert solve("") == ""

def test_single_character():
    assert solve("a") == "A"

def test_all_letters():
    assert solve("abc") == "ABC"

def test_mixed_case():
    assert solve("ab") == "AB"

def test_numbers():
    assert solve("123") == "321"

def test_symbols():
    assert solve("#a") == "#A"

def test_special_characters():
    assert solve("#@") == "#@"

def test_complex_string():
    assert solve("hello") == "olleh"

def test_string_with_numbers_and_symbols():
    assert solve("123!@#") == "!@#123"

def test_empty_string_with_numbers():
    assert solve("") == ""