
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

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""

@pytest.mark.parametrize("word, expected", [
    ("go", "go"),
    ("this", "")
])
def test_single_word(word, expected):
    assert words_in_sentence(word) == expected

def test_multiple_words_with_prime_lengths():
    assert words_in_sentence("This is a test") == "is"

def test_multiple_words_with_mixed_lengths():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_all_words_non_prime_lengths():
    assert words_in_sentence("this is a very long sentence") == ""

def test_all_words_prime_lengths():
    assert words_in_sentence("go for two five") == "go for two five"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  go for  ") == "go for"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("go   for  two") == "go for two"

def test_sentence_with_one_letter_prime_word():
    assert words_in_sentence("a go") == "go"

def test_sentence_with_one_letter_non_prime_word():
    assert words_in_sentence("i go") == "go"

def test_sentence_with_long_prime_length_word():
    assert words_in_sentence("This is a verylongword") == "verylongword"

def test_sentence_with_long_non_prime_length_word():
    assert words_in_sentence("This is a verylongwordnotprime") == ""

def test_sentence_with_numbers_in_words():
    assert words_in_sentence("This is 2 test") == ""

def test_sentence_with_special_characters():
    assert words_in_sentence("This is a test!") == ""

def test_sentence_with_prime_and_non_prime_words_at_start_and_end():
    assert words_in_sentence("go this is a test") == "go"

def test_sentence_with_prime_and_non_prime_words_in_middle():
    assert words_in_sentence("this go is a test") == "go"

def test_sentence_with_only_punctuation():
    assert words_in_sentence("!@#$%^&*()") == ""

def test_sentence_with_very_long_prime_word():
    long_prime_word = "a" * 101  # Length 101 is prime
    assert words_in_sentence(long_prime_word) == long_prime_word

def test_sentence_with_unicode_characters():
    assert words_in_sentence("你好世界") == "" # Assuming Unicode characters are not considered prime

def test_empty_string_after_stripping():
    assert words_in_sentence("a i o") == ""

def test_sentence_with_one_word_non_prime():
    assert words_in_sentence("this") == ""

def test_sentence_with_one_word_prime():
    assert words_in_sentence("go") == "go"