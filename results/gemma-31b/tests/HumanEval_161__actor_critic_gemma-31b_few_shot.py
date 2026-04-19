
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

def test_solve_basic_case_swap():
    """Tests standard case swapping when letters are present."""
    assert solve("ab") == "AB"
    assert solve("ABC") == "abc"
    assert solve("aBcD") == "AbCd"

def test_solve_mixed_characters():
    """Tests strings containing both letters and non-letter characters."""
    assert solve("#a@C") == "#A@c"
    assert solve("Hello World 123!") == "hELLO wORLD 123!"
    assert solve("1a2b3C") == "1A2B3c"

def test_solve_no_letters_reverse():
    """Tests that strings with no letters are reversed."""
    assert solve("1234") == "4321"
    assert solve("!@#$%") == "%$#@!"
    assert solve("12 34") == "43 21"

def test_solve_empty_string():
    """Tests the behavior with an empty string."""
    assert solve("") == ""

def test_solve_whitespace_only():
    """Tests strings containing only whitespace (should be treated as no letters and reversed)."""
    assert solve("   ") == "   "
    assert solve(" \t\n") == "\n\t "

def test_solve_unicode_cased():
    """Tests that Unicode letters with case are swapped correctly."""
    assert solve("éΩß") == "Éωẞ" 
    assert solve("é123!") == "É123!"

def test_solve_unicode_non_cased():
    """
    Tests characters that are alphabetical (isalpha() == True) but lack case.
    These should be treated as letters (preventing reversal) but remain unchanged.
    """
    # Chinese characters are isalpha() but have no case
    assert solve("你好") == "你好" 
    assert solve("a你好") == "A你好"

def test_solve_unicode_non_letters():
    """Tests that non-letter Unicode symbols (like Emojis) trigger reversal if no letters are present."""
    # No letters present: should reverse
    assert solve("😀😊") == "😊😀"
    # Letters present: should swap case and keep emoji in place
    assert solve("a😀") == "A😀"

def test_solve_invalid_types():
    """Tests that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        solve(None)
    with pytest.raises(TypeError):
        solve(123)
    with pytest.raises(TypeError):
        solve(["a", "b"])