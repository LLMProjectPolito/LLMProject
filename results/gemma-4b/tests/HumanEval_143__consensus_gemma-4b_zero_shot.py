
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
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)


def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_word_prime():
    assert words_in_sentence("test") == "test"

def test_single_word_non_prime():
    assert words_in_sentence("hello") == ""

def test_multiple_words_some_prime():
    assert words_in_sentence("This is a test") == "is"

def test_multiple_words_all_prime():
    assert words_in_sentence("prime prime prime") == "prime prime prime"

def test_multiple_words_no_prime():
    assert words_in_sentence("hello world") == ""

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("This   is  a    test") == "is"

def test_sentence_with_numbers():
    assert words_in_sentence("This is 123 test") == "is"

def test_sentence_with_special_characters():
    assert words_in_sentence("This is a!@# test") == "is"

def test_sentence_with_long_words():
    assert words_in_sentence("This is a verylongword test") == "is"

def test_sentence_with_short_words():
    assert words_in_sentence("a b c d e") == "b"

def test_sentence_with_mixed_prime_and_non_prime():
    assert words_in_sentence("one two three four five") == "two three five"

def test_sentence_with_prime_length_words_at_start_and_end():
    assert words_in_sentence("prime test prime") == "prime test prime"

def test_sentence_with_only_non_prime_words():
    assert words_in_sentence("hello world") == ""

def test_sentence_with_one_prime_word():
    assert words_in_sentence("test") == "test"

def test_sentence_with_two_prime_words():
    assert words_in_sentence("one two") == "one two"

def test_sentence_with_three_prime_words():
    assert words_in_sentence("one two three") == "two three"