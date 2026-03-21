import pytest

def test_count_distinct_characters_empty_string():
    assert count_distinct_characters("") == 0

def test_count_distinct_characters_single_character():
    assert count_distinct_characters("a") == 1

def test_count_distinct_characters_multiple_characters():
    assert count_distinct_characters("abc") == 3

def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters("aA") == 1

def test_count_distinct_characters_repeated_characters():
    assert count_distinct_characters("aaa") == 1

def test_count_distinct_characters_mixed_case():
    assert count_distinct_characters("xyzXYZ") == 3

def test_count_distinct_characters_real_word():
    assert count_distinct_characters("Jerry") == 4

def test_count_distinct_characters_numbers():
    assert count_distinct_characters("123") == 3

def test_count_distinct_characters_special_characters():
    assert count_distinct_characters("!@#") == 3

def test_count_distinct_characters_long_string():
    long_string = "abcdefghijklmnopqrstuvwxyz"
    assert count_distinct_characters(long_string) == 26

def test_count_distinct_characters_string_with_spaces():
    assert count_distinct_characters("hello world") == 9

def test_count_distinct_characters_string_with_punctuation():
    assert count_distinct_characters("hello, world!") == 10