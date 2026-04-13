
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
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test suite
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_word_prime_length():
    assert words_in_sentence("abc") == "abc"

def test_single_word_non_prime_length():
    assert words_in_sentence("abcd") == ""

def test_multiple_words_some_prime():
    assert words_in_sentence("This is a test") == "is"

def test_multiple_words_all_prime():
    assert words_in_sentence("abc def ghi") == "abc def"

def test_multiple_words_no_prime():
    assert words_in_sentence("abcd efgh ijkl") == ""

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("This   is  a    test") == "is"

def test_sentence_with_only_prime_length_words():
    assert words_in_sentence("abc def ghi") == "abc def"

def test_sentence_with_only_non_prime_length_words():
    assert words_in_sentence("abcd efgh ijkl") == ""

def test_sentence_with_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test abc def") == "is a"

def test_long_sentence():
    assert words_in_sentence("This is a very long sentence with many words") == "is a"

def test_sentence_with_numbers_as_words():
    assert words_in_sentence("123 abc 456 def") == "abc"

def test_sentence_with_special_characters():
    assert words_in_sentence("This is a test!") == ""

def test_prime_number_1():
    assert words_in_sentence("a") == "a"

def test_prime_number_2():
    assert words_in_sentence("ab") == ""

def test_prime_number_3():
    assert words_in_sentence("abc") == "abc"

def test_prime_number_5():
    assert words_in_sentence("hello") == ""

def test_prime_number_7():
    assert words_in_sentence("world") == ""

def test_all_non_prime():
    assert words_in_sentence("abcdefghijklm") == ""

def test_is_prime_0():
    assert is_prime(0) == False

def test_is_prime_1():
    assert is_prime(1) == False

def test_is_prime_2():
    assert is_prime(2) == True