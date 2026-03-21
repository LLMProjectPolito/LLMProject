import pytest
import math


# Focus: Boundary Values
def test_make_palindrome_empty_string():
    assert make_palindrome('') == ''

def test_make_palindrome_single_character():
    assert make_palindrome('a') == 'a'

def test_make_palindrome_single_character_with_reversed_prefix():
    assert make_palindrome('a') == 'a'

# Focus: Error Scenarios
def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_non_palindrome_string():
    assert is_palindrome("hello") == False

# Focus: Edge Case Strings
def test_make_palindrome_empty_string():
    assert make_palindrome('') == ''

def test_make_palindrome_single_char():
    assert make_palindrome('a') == 'a'

def test_make_palindrome_already_palindrome():
    assert make_palindrome('catac') == 'catac'