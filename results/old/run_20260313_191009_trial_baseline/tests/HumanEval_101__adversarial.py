import pytest

def test_words_string_commas():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

def test_words_string_spaces():
    assert words_string("One two three four five six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_mixed_separators():
    assert words_string("Hi, my name is John, and I am happy") == ["Hi", "my", "name", "is", "John", "and", "I", "am", "happy"]

def test_words_string_empty_string():
    assert words_string("") == []

def test_words_string_single_word():
    assert words_string("Hello") == ["Hello"]

def test_words_string_multiple_spaces():
    assert words_string("One   two   three") == ["One", "two", "three"]

def test_words_string_leading_trailing_spaces():
    assert words_string("   One two three   ") == ["One", "two", "three"]

def test_words_string_leading_trailing_commas():
    assert words_string(",One,two,three,") == ["One", "two", "three"]

def test_words_string_consecutive_commas():
    assert words_string("One,,two,,three") == ["One", "", "two", "", "three"]

def test_words_string_punctuation():
    assert words_string("Hello, world!") == ["Hello", "world!"]

def test_words_string_numbers():
    assert words_string("One 1 two 2 three 3") == ["One", "1", "two", "2", "three", "3"]

def test_words_string_special_characters():
    assert words_string("One @ two # three $") == ["One", "@", "two", "#", "three", "$"]