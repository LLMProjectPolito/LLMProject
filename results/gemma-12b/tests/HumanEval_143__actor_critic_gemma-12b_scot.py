
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

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("This is a long sentence") == ""

def test_all_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_mixed_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_single_word_prime_length():
    assert words_in_sentence("test") == "test"

def test_single_word_non_prime_length():
    assert words_in_sentence("testing") == ""

def test_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is a"

def test_multiple_spaces_between_words():
    assert words_in_sentence("This   is  a   test") == "is a"

def test_long_sentence():
    assert words_in_sentence("This is a very long sentence with many words of varying lengths") == "is a very long sentence"

def test_spaces_only():
    assert words_in_sentence("   ") == ""

def test_large_prime_length_word():
    assert words_in_sentence("abcdefghijklmnop") == "abcdefghijklmnop"

def test_large_non_prime_length_word():
    assert words_in_sentence("abcdefghijklmno") == ""

def test_prime_word_at_beginning():
    assert words_in_sentence("test This is a test") == "test"

def test_multiple_prime_words_in_a_row():
    assert words_in_sentence("go for a test") == "go for test"

def test_invalid_input_with_numbers():
    assert words_in_sentence("This is a 1 test") == "is a"