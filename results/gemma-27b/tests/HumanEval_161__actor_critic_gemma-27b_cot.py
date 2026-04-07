
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """

import pytest

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"

def test_mixed_case_letters():
    assert solve("aB") == "Ab"

def test_mixed_letters_and_numbers():
    assert solve("a1B2") == "A1b2"

def test_special_characters():
    assert solve("#a@C") == "#A@c"

def test_string_with_spaces():
    assert solve("a b C") == "A b c"  # Spaces should remain unchanged

def test_long_string():
    assert solve("ThisIsALongString") == "tHISiSaLONGsTRING"

def test_string_with_unicode_characters():
    assert solve("你好世界") == "你好世界"

def test_string_with_letters_numbers_and_special_chars():
    assert solve("a1b2!c3@") == "A1b2!C3@"

def test_edge_case_single_letter_lowercase():
    assert solve("a") == "A"

def test_edge_case_single_letter_uppercase():
    assert solve("A") == "a"

def test_unicode_and_letters():
    assert solve("a你好b") == "A你好B"

def test_invalid_input_none():
    with pytest.raises(TypeError) as excinfo:
        solve(None)
    assert str(excinfo.value) == "Input must be a string"

def test_invalid_input_integer():
    with pytest.raises(TypeError) as excinfo:
        solve(123)
    assert str(excinfo.value) == "Input must be a string"

def test_invalid_input_list():
    with pytest.raises(TypeError) as excinfo:
        solve([1, 2, 3])
    assert str(excinfo.value) == "Input must be a string"

def test_complex_unicode():
    assert solve("áb") == "ÁB"

def test_unicode_combining_characters():
    assert solve("café") == "CAFÉ"