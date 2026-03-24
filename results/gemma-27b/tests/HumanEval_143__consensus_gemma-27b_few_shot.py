
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
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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

def test_single_prime_word():
    assert words_in_sentence("is") == "is"

def test_single_non_prime_word():
    assert words_in_sentence("this") == ""

def test_multiple_words_some_prime():
    assert words_in_sentence("This is a test") == "is"

def test_multiple_words_all_prime():
    assert words_in_sentence("go for") == "go for"

def test_multiple_words_none_prime():
    assert words_in_sentence("this that those") == ""

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("This   is  a   test") == "is"

def test_long_sentence():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the over dog"

def test_sentence_with_mixed_case():
    assert words_in_sentence("This Is A Test") == "Is"

def test_sentence_with_numbers_and_symbols():
    assert words_in_sentence("123 abc !@# def") == "abc def"

def test_sentence_with_prime_and_non_prime_lengths():
    assert words_in_sentence("two three four five") == "three five"

def test_sentence_with_only_one_word_length_2():
    assert words_in_sentence("to") == ""

def test_sentence_with_only_one_word_length_3():
    assert words_in_sentence("cat") == "cat"