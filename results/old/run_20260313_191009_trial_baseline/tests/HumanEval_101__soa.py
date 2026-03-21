import pytest

def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return s.replace(",", " ").split()

def test_words_string_empty_string():
    assert words_string("") == []

def test_words_string_single_word():
    assert words_string("Hello") == ["Hello"]

def test_words_string_multiple_words_comma_separated():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

def test_words_string_multiple_words_space_separated():
    assert words_string("One two three four five six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_multiple_words_mixed_separators():
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_multiple_words_with_punctuation():
    assert words_string("Hello, world! How are you?") == ["Hello", "world", "How", "are", "you"]

def test_words_string_multiple_words_with_leading_trailing_spaces():
    assert words_string("   Hello, world!  ") == ["Hello", "world"]

def test_words_string_multiple_words_with_leading_trailing_commas():
    assert words_string(", Hello, world!, ") == ["Hello", "world"]

def test_words_string_multiple_words_with_leading_trailing_spaces_and_commas():
    assert words_string(" , Hello, world!,  ") == ["Hello", "world"]