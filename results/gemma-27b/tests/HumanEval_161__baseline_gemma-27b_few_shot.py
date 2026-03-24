
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

def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_all_letters():
    assert solve("ab") == "AB"

def test_solve_mixed_case_and_symbols():
    assert solve("#a@C") == "#A@c"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_letter_lowercase():
    assert solve("a") == "A"

def test_solve_single_letter_uppercase():
    assert solve("A") == "a"

def test_solve_numbers_and_letters():
    assert solve("a1b2c") == "A1B2C"

def test_solve_symbols_and_letters():
    assert solve("!a@B#c$") == "!A@b#C$"

def test_solve_long_string():
    assert solve("ThisIsALongString") == "tHISiSaLONGsTRING"

def test_solve_string_with_spaces():
    assert solve("hello world") == "HELLO WORLD"