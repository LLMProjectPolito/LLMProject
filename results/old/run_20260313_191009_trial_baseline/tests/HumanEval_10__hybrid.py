import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ("", ""),
    ("cat", "catac"),
    ("cata", "catac"),
    ("radar", "radar"),
    ("hello", "helloolleh"),
    ("a", "a"),
    ("ab", "aba"),
    ("abc", "abcba"),
    ("abba", "abba"),
    ("abcd", "abcddcba"),
])
def test_make_palindrome(input_string, expected_output):
    assert make_palindrome(input_string) == expected_output

def test_make_palindrome_long_string():
    long_string = "abcdefghijklmnopqrstuvwxyz"
    assert make_palindrome(long_string) == long_string + long_string[::-1]

def test_make_palindrome_already_palindrome():
    palindrome_string = "madam"
    assert make_palindrome(palindrome_string) == palindrome_string