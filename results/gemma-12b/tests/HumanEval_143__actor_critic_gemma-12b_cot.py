
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
    assert words_in_sentence("this is a long sentence") == ""

def test_single_prime_length_word():
    assert words_in_sentence("a") == "a"

def test_multiple_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_spaces_handling():
    assert words_in_sentence("  This is a test  ") == "is"
    assert words_in_sentence("This  is   a    test") == "is"
    assert words_in_sentence("   ") == ""

def test_sentence_with_only_one_word():
    assert words_in_sentence("prime") == "prime"

def test_sentence_with_prime_length_words_at_beginning_and_end():
    assert words_in_sentence("a lets go for swimming") == "a lets"

def test_sentence_with_all_prime_length_words():
    assert words_in_sentence("a is go") == "a is go"

def test_sentence_with_long_prime_length_words():
    assert words_in_sentence("This is a verylongword test") == ""

def test_sentence_with_short_prime_length_words():
    assert words_in_sentence("I am") == "I am"

def test_mixed_case():
    assert words_in_sentence("This Is A Test") == "Is A"

def test_with_special_characters():
    assert words_in_sentence("hello! world?") == ""