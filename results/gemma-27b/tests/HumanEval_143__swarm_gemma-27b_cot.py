
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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_sentence_with_no_prime_length_words():
    assert words_in_sentence("aaaa bbbb cccc") == ""

def test_sentence_with_all_prime_length_words():
    assert words_in_sentence("is a go") == "is a go"

def test_mixed_sentence():
    assert words_in_sentence("This is a test") == "is"

def test_long_sentence():
    assert words_in_sentence("lets go for swimming and running") == "go for"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "hello world"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("hello   world") == "hello world"

def test_sentence_with_single_character_words():
    assert words_in_sentence("a b c d e") == "a b c d e"

def test_sentence_with_prime_and_non_prime_length_words():
    assert words_in_sentence("one two three four five") == "one three five"

def test_edge_case_sentence_with_long_word():
    assert words_in_sentence("abcdefghijk") == ""

def test_sentence_with_single_prime_length_word():
    assert words_in_sentence("two") == "two"

def test_sentence_with_single_non_prime_length_word():
    assert words_in_sentence("one") == ""

def test_sentence_with_repeated_prime_length_words():
    assert words_in_sentence("is is is") == "is is is"

def test_sentence_with_special_characters():
    with pytest.raises(TypeError):
        words_in_sentence("hello! world?")