import pytest

def test_empty_string():
    assert solve("") == ""

def test_only_letters_lowercase():
    assert solve("abc") == "ABC"

def test_only_letters_uppercase():
    assert solve("ABC") == "abc"

def test_mixed_case_letters():
    assert solve("aBc") == "AbC"

def test_only_numbers():
    assert solve("1234") == "4321"

def test_only_special_characters():
    assert solve("#@$") == "#@$"

def test_mixed_letters_numbers():
    assert solve("a1b2c") == "A1B2C"

def test_mixed_letters_special_characters():
    assert solve("a#b$c%") == "A#B$C%"

def test_mixed_all_characters():
    assert solve("a1#b2$c%") == "A1#B2$C%"

def test_letter_at_beginning():
    assert solve("a123") == "A123"

def test_letter_at_end():
    assert solve("123a") == "123A"

def test_letter_in_middle():
    assert solve("12a34") == "12A34"

def test_single_letter():
    assert solve("a") == "A"

def test_single_number():
    assert solve("1") == "1"

def test_single_special_character():
    assert solve("#") == "#"

def test_long_string():
    long_string = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    expected_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    assert solve(long_string) == expected_string

def test_unicode_characters():
    assert solve("你好世界") == "你好世界"

def test_unicode_and_letters():
    assert solve("你好a世界") == "你好A世界"

def test_no_letters():
    assert solve("123!@#") == "!@#321"

def test_string_with_spaces():
    assert solve("a b c") == "A b C"