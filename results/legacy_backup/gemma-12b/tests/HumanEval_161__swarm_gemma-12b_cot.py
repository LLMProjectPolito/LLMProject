import pytest
import math

def test_solve_empty_string():
    """Test case for an empty string."""
    assert solve("") == ""

def test_string_with_only_numbers():
    assert solve("12345") == "54321"

def test_string_with_only_symbols():
    assert solve("!@#$%^") == "!@#$%^"

def test_string_with_mixed_symbols_and_numbers():
    assert solve("!1@2#3$") == "$3#2@1!"

def test_string_with_unicode_characters():
    assert solve("你好世界") == "界世好你"

def test_string_with_mixed_case_and_unicode():
    assert solve("a你好B世界c") == "A你好b世界C"

def test_string_with_leading_and_trailing_spaces():
    assert solve("  abc  ") == "  ABC  "

def test_string_with_multiple_consecutive_letters():
    assert solve("abcdefg") == "gfedcba"

def test_string_with_mixed_case_symbols_and_numbers():
    assert solve("a1B@c2#D$") == "A1b@C2#d$"

def test_string_with_special_characters():
    assert solve("!@#$%^&*()") == "!@#$%^&*()"