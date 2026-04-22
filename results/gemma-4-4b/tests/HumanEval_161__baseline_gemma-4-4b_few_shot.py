
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
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
        elif 'A' <= char <= 'Z':
            result += char.lower()
        else:
            result += char
    return result

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_no_letters():
    assert solve("12345") == "54321"

def test_solve_all_letters_lower():
    assert solve("abc") == "ABC"

def test_solve_all_letters_upper():
    assert solve("ABC") == "abc"

def test_solve_mixed_case():
    assert solve("aBc") == "AbC"

def test_solve_mixed_case_with_numbers_and_symbols():
    assert solve("aB1c@D") == "Ab1C@d"

def test_solve_complex_string():
    assert solve("HeLlO wOrLd!") == "HeLlO WoRlD!"

def test_solve_another_complex_string():
    assert solve("ThIsIsAtEsT") == "tHiSiSaTeSt"