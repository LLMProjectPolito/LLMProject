
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


import pytest

class TestSolve:

    def test_empty_string(self):
        assert solve("") == ""

    def test_string_with_no_letters(self):
        assert solve("12345") == "54321"
        assert solve("!@#$%^") == "!@#$%^"

    def test_string_with_only_lowercase_letters(self):
        assert solve("abc") == "ABC"

    def test_string_with_only_uppercase_letters(self):
        assert solve("ABC") == "abc"

    def test_string_with_mixed_case_letters(self):
        assert solve("aBcDeF") == "AbCdEf"

    def test_string_with_letters_and_numbers(self):
        assert solve("a1b2c") == "A1B2C"
        assert solve("Ab1C2d") == "aB1c2D"

    def test_string_with_letters_and_symbols(self):
        assert solve("#a@C") == "#A@c"
        assert solve("!@#a$B") == "!@#A$b"

    def test_complex_string(self):
        assert solve("HeLlO wOrLd!") == "hElLo WoRlD!"

    def test_long_string(self):
        assert solve("ThisIsALongStringWithMixedCase123!") == "tHiSiSaLoNgStRiNgWiThMiXeDcAsE123!"
    
    def test_special_characters(self):
        assert solve("!@#$%^&*()") == "!@#$%^&*()"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_no_letters():
    assert solve("12345") == "54321"
    assert solve("!@#$%^") == "^%$#@!"

def test_solve_all_letters_lower():
    assert solve("abc") == "ABC"

def test_solve_all_letters_upper():
    assert solve("ABC") == "abc"

def test_solve_mixed_case():
    assert solve("aBc") == "AbC"
    assert solve("AbC") == "abc"
    assert solve("aB") == "Ab"
    assert solve("Ab") == "ab"
    assert solve("HeLlO") == "hElLo"

def test_solve_mixed_case_with_symbols():
    assert solve("aB12c") == "Ab12C"
    assert solve("!aB@c") == "!Ab@C"
    assert solve("aB!c@") == "Ab!c@"

def test_solve_complex_string():
    assert solve("Hello World!") == "hELLO wORLD!"
    assert solve("ThisIsATest") == "tHISisAtEST"

def test_solve_palindrome_like():
    assert solve("madAm") == "MaDaM"

def test_solve_with_spaces():
    assert solve("a b c") == "A b C"



def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None