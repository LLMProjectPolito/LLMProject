import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
    res = ''
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            if 'a' <= char <= 'z':
                res += char.upper()
            else:
                res += char.lower()
        else:
            res += char
    return res

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == False

def test_is_palindrome_with_spaces():
    assert is_palindrome('madam') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == False

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_lowercase():
    assert solve("ab") == "AB"

def test_solve_uppercase():
    assert solve("#a@C") == "#A@c"

def test_solve_mixed_case():
    assert solve("aBc") == "AbC"

def test_solve_with_numbers():
    assert solve("123a456") == "123A456"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_special_characters():
    assert solve("!@#$%^") == "!@#$%^"

def test_solve_mixed_special_and_letters():
    assert solve("a!b@c#") == "A!B@C#"