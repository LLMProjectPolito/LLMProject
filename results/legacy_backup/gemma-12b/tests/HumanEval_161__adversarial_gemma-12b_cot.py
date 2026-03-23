import pytest

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
    has_letter = False
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            has_letter = True
            break

    if not has_letter:
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


def test_solve_all_letters_lowercase():
    assert solve("abc") == "ABC"

def test_solve_all_letters_uppercase():
    assert solve("ABC") == "abc"

def test_solve_mixed_letters():
    assert solve("aBc") == "AbC"

def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_numbers_and_symbols():
    assert solve("#$%^") == "#$%^"

def test_solve_letters_and_symbols():
    assert solve("#a@C") == "#A@c"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_letter_lowercase():
    assert solve("a") == "A"

def test_solve_single_letter_uppercase():
    assert solve("A") == "a"

def test_solve_single_number():
    assert solve("1") == "1"

def test_solve_single_symbol():
    assert solve("#") == "#"

def test_solve_long_string():
    assert solve("abcdefghijklmnopqrstuvwxyz") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def test_solve_long_string_mixed():
    assert solve("aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "AbCdEfGhIjKlMnOpQrStUvWxYz"

def test_solve_with_spaces():
    assert solve("hello world") == "HELLO WORLD"

def test_solve_with_numbers_and_spaces():
    assert solve("1 2 3") == "1 2 3"

def test_solve_with_special_characters():
    assert solve("!@#$%^&*()") == "!@#$%^&*()"

def test_solve_unicode_characters():
    assert solve("你好世界") == "你好世界"

def test_solve_invalid_input_type():
    with pytest.raises(TypeError):
        solve(123)