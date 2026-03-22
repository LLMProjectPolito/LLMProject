import pytest

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"

def test_all_letters_lowercase():
    assert solve("ab") == "AB"

def test_all_letters_uppercase():
    assert solve("AB") == "ab"

def test_mixed_case_letters():
    assert solve("aB") == "Ab"

def test_mixed_letters_and_numbers():
    assert solve("a1B2") == "A1b2"

def test_special_characters_and_letters():
    assert solve("#a@C") == "#A@c"

def test_string_with_spaces():
    assert solve("a b C") == "A b c"

def test_string_with_only_special_characters():
    assert solve("!@#$%^") == "!@#$%^"

def test_long_string_with_mixed_content():
    assert solve("ThisIsA123TestString") == "tHISiSa123tESTsTRING"

def test_string_with_unicode_characters():
    assert solve("你好世界") == "你好世界"

def test_string_with_numbers_and_special_chars():
    assert solve("123!@#") == "!@#321"

def test_string_with_leading_and_trailing_spaces():
    assert solve("  aB  ") == "  Ab  "

def test_string_with_multiple_consecutive_letters():
    assert solve("abc") == "ABC"

def test_string_with_multiple_consecutive_letters_mixed_case():
    assert solve("aBcDeF") == "AbCdEf"

def test_string_with_only_one_letter():
    assert solve("a") == "A"

def test_string_with_only_one_number():
    assert solve("1") == "1"

def test_string_with_only_one_special_char():
    assert solve("!") == "!"