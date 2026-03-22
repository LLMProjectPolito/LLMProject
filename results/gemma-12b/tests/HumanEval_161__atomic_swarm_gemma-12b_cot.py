import pytest
import math

def test_solve_basic():
    assert solve("ab") == "AB"

def test_solve_empty_string():
    """Test with an empty string."""
    assert solve("") == ""

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_string_with_no_letters():
    assert solve("1234") == "4321"

def test_solve_string_with_only_letters():
    assert solve("abc") == "CBA"

def test_solve_string_with_mixed_characters():
    assert solve("#a@C") == "#A@c"

def test_solve_string_with_special_characters():
    assert solve("!@#$%^") == "!@#$%^"

def test_solve_string_with_numbers_and_letters():
    assert solve("a1b2c") == "A1B2C"

def test_solve_string_with_uppercase_and_lowercase():
    assert solve("AbCd") == "aBcD"

def test_solve_string_with_unicode_characters():
    assert solve("你好世界") == "你好世界"

def test_solve_string_with_mixed_unicode_and_letters():
    assert solve("你好a世界") == "你好A世界"