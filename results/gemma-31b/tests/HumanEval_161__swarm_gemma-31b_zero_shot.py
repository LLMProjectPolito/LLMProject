
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

def test_solve_no_letters_mixed():
    assert solve("! 12 34 @") == "@ 43 21 !"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_only_non_letters_with_spaces():
    assert solve("123 !@# ") == " #@! 321"