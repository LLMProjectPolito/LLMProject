import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ("", True),
    ("a", True),
    ("ab", False),
    ("aba", True),
    ("abba", True),
    ("abcba", True),
    ("radar", True),
    ("python", False),
    ("level", True),
])
def test_is_palindrome(input_string, expected_output):
    assert is_palindrome(input_string) == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("", ""),
    ("a", "a"),
    ("ab", "aba"),
    ("cata", "catac"),
    ("cat", "catac"),
    ("abccba", "abccba"),
    ("", ""),
    ("cat", "catac"),
    ("cata", "catac"),
    ("abba", "abba"),
    ("abc", "abcba"),
])
def test_make_palindrome(input_string, expected_output):
    assert make_palindrome(input_string) == expected_output

def test_make_palindrome_long_string():
    long_string = "abcdefghijklmnopqrstuvwxyz"
    result = make_palindrome(long_string)
    assert result == long_string + long_string[::-1]

def test_make_palindrome_non_ascii():
    non_ascii_string = "öäü"
    result = make_palindrome(non_ascii_string)
    assert result == non_ascii_string + non_ascii_string[::-1]

def test_is_palindrome_non_string_input():
    with pytest.raises(TypeError):
        is_palindrome(123)

def test_make_palindrome_non_string_input():
    with pytest.raises(TypeError):
        make_palindrome(123)