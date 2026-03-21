import pytest

def test_is_palindrome_empty_string():
    assert is_palindrome('') == True

def test_is_palindrome_single_character():
    assert is_palindrome('a') == True

def test_is_palindrome_palindrome_string():
    assert is_palindrome('madam') == True

def test_is_palindrome_non_palindrome_string():
    assert is_palindrome('hello') == False

def test_make_palindrome_empty_string():
    assert make_palindrome('') == ''

def test_make_palindrome_single_character():
    assert make_palindrome('a') == 'a'

def test_make_palindrome_palindrome_string():
    assert make_palindrome('madam') == 'madam'

def test_make_palindrome_non_palindrome_string():
    assert make_palindrome('cat') == 'catac'

def test_make_palindrome_non_palindrome_string_empty():
    assert make_palindrome('') == ''

def test_make_palindrome_non_palindrome_string_single_character():
    assert make_palindrome('a') == 'a'