
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

def test_no_prime_length_words():
    assert words_in_sentence("this is not a prime") == ""

def test_single_prime_length_word():
    assert words_in_sentence("a") == "a"

def test_multiple_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_all_words_prime_length():
    assert words_in_sentence("I am here") == "I am"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("This  is   a    test") == "is"

def test_long_sentence():
    sentence = "This is a very long sentence with some words of prime and non-prime lengths"
    expected = "is a very long sentence with some words of prime"
    assert words_in_sentence(sentence) == expected

def test_sentence_with_only_one_word():
    assert words_in_sentence("prime") == "prime"

def test_sentence_with_same_length_words():
    assert words_in_sentence("one two three four five") == "one two three five"

def test_sentence_with_special_characters_not_allowed():
    with pytest.raises(TypeError):
        words_in_sentence("This is a test!")

def test_sentence_with_numbers_not_allowed():
    with pytest.raises(TypeError):
        words_in_sentence("This is 1 test")