
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
import math

@pytest.mark.parametrize("input_str, expected", [
    (" 123! @# ", " #@ !321 "),
    (" 123 ! ", " ! 321 "),
    (" 123 !@# ", " #@! 321 "),
])
def test_solve_no_letters_reversal(input_str, expected):
    """
    Tests that strings containing spaces, numbers, and symbols, 
    but no alphabetic letters, are correctly reversed.
    """
    assert solve(input_str) == expected