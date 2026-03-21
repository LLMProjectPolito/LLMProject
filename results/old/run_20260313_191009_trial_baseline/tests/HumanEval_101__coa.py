import pytest
import math


# Focus: Boundary Values
def test_words_string_empty_string():
    assert words_string("") == []

def test_words_string_single_word():
    assert words_string("Hello") == ["Hello"]

def test_words_string_multiple_words_with_spaces():
    assert words_string("Hello World this is a test") == ["Hello", "World", "this", "is", "a", "test"]

def test_words_string_multiple_words_with_commas():
    assert words_string("Hello, World, this, is, a, test") == ["Hello", "World", "this", "is", "a", "test"]

# Focus: Input Variations
def test_words_string_empty_string():
    assert words_string("") == []

def test_words_string_single_word():
    assert words_string("Hello") == ["Hello"]

def test_words_string_multiple_words_comma_separated():
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_multiple_words_space_separated():
    assert words_string("One two three four five six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_leading_trailing_spaces():
    assert words_string("   One, two, three, four, five, six  ") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_leading_trailing_commas():
    assert words_string(", One, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]

# Focus: Edge Cases
def test_empty_string():
    assert words_string("") == []

def test_single_word():
    assert words_string("Hello") == ["Hello"]

def test_single_word_with_comma():
    assert words_string("Hello,") == ["Hello,"]