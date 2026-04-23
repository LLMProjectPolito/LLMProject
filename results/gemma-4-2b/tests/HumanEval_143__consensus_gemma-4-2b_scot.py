
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

import pytest
from your_module import words_in_sentence  # Replace your_module

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_word_not_prime():
    assert words_in_sentence("a") == ""

def test_single_word_prime():
    assert words_in_sentence("i") == "i"

def test_simple_case_1():
    assert words_in_sentence("This is a test") == "is"

def test_simple_case_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_multiple_prime_words():
    assert words_in_sentence("The quick brown fox jumps over the lazy dog") == "quick brown"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test sentence") == "is"

def test_sentence_with_spaces():
    assert words_in_sentence("hello world") == "world"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "world"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("hello   world") == "world"

def test_long_sentence():
    sentence = "This is a very long sentence with many words."
    assert words_in_sentence(sentence) == "is"

def test_sentence_with_capitalization():
    assert words_in_sentence("This Is A Test") == "Is"

def test_sentence_with_numbers():
    assert words_in_sentence("This is a 123 test") == "is"

def test_sentence_with_special_characters():
    assert words_in_sentence("This is a test!") == "is"

def test_sentence_with_mixed_case_and_numbers():
    sentence = "This Is A 123 Test"
    assert words_in_sentence(sentence) == "Is"

def test_sentence_with_long_words():
    sentence = "This is a very very long word"
    assert words_in_sentence(sentence) == "is"

def test_sentence_with_numbers_and_spaces():
    sentence = "This is a 123 test"
    assert words_in_sentence(sentence) == "is"

def test_sentence_with_uppercase_and_lowercase():
    sentence = "This Is A Test"
    assert words_in_sentence(sentence) == "Is"

def test_sentence_with_special_characters():
    sentence = "This is a test!"
    assert words_in_sentence(sentence) == "is"

def test_sentence_with_unicode_characters():
    sentence = "你好世界"
    assert words_in_sentence(sentence) == ""

def test_sentence_with_all_lowercase():
    sentence = "this is a test"
    assert words_in_sentence(sentence) == "is"

def test_sentence_with_all_uppercase():
    sentence = "THIS IS A TEST"
    assert words_in_sentence(sentence) == "IS"

def test_sentence_with_mixed_case_and_numbers():
    sentence = "This Is A 123 Test"
    assert words_in_sentence(sentence) == "Is"