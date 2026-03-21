import pytest

def test_words_string_comma_separated():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

def test_words_string_space_separated():
    assert words_string("One two three four five six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_mixed_separators():
    assert words_string("One, two three, four five, six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_single_word():
    assert words_string("Hello") == ["Hello"]

def test_words_string_empty_string():
    assert words_string("") == []

def test_words_string_multiple_spaces():
    assert words_string("One  two   three") == ["One", "two", "three"]

def test_words_string_leading_trailing_spaces():
    assert words_string("   One two three   ") == ["One", "two", "three"]

def test_words_string_leading_trailing_commas():
    assert words_string(", One, two, three,") == ["One", "two", "three"]

def test_words_string_consecutive_commas():
    assert words_string("One,, two, three") == ["One", "", "two", "three"]