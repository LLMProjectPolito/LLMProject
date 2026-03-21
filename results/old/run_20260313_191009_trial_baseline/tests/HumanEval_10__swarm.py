import pytest
import math

def test_make_palindrome():
    assert make_palindrome('a') == 'a'
    assert make_palindrome("") == ""