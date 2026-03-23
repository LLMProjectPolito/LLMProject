import pytest

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"

def test_all_lowercase():
    assert solve("ab") == "AB"

def test_mixed_case():
    assert solve("#a@C") == "#A@c"

def test_with_numbers_and_symbols():
    assert solve("a1b2c") == "A1B2C"

def test_only_uppercase():
    assert solve("AB") == "ab"

def test_special_characters():
    assert solve("!@#$%^") == "!@#$%^"

def test_mixed_string():
    assert solve("HeLlO wOrLd 123") == "hElLo WoRlD 123"

def test_string_with_spaces():
    assert solve("  a b  ") == "  A B  "

def test_long_string():
    assert solve("ThisIsALongStringWithNumbers123AndSymbols!@#") == "tHISiSaLONGsTRINGwITHnUMBERS123aNDsYMBOLS!@#"

def test_string_with_unicode():
    assert solve("你好世界") == "你好世界"

def test_string_with_mixed_unicode_and_ascii():
    assert solve("Hello你好World") == "hELLO你好wORLD"