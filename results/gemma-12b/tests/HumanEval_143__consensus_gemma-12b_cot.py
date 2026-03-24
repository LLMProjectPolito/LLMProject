
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
    sentence = "This is a very long sentence with some words of prime lengths and some not"
    expected = "is a very long with some and"
    assert words_in_sentence(sentence) == expected

def test_sentence_with_only_one_word():
    assert words_in_sentence("prime") == "prime"

def test_sentence_with_same_length_words():
    assert words_in_sentence("go do re mi") == "go do re"

def test_sentence_with_numbers_as_words():
    assert words_in_sentence("1 2 3 4 5") == "2 3"

def test_sentence_with_special_characters():
    assert words_in_sentence("!@#$ %^&*()") == ""

def test_sentence_with_unicode_characters():
    assert words_in_sentence("你好 世界") == ""

def test_prime_length_at_end():
    assert words_in_sentence("This is a test a") == "is a"