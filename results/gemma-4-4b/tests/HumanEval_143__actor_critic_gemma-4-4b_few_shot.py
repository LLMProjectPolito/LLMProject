
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
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()

import pytest

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == "hello"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_length():
    assert words_in_sentence("a bb ccc dddd") == ""

def test_words_in_sentence_all_prime_length():
    assert words_in_sentence("abc def ghi") == "abc def ghi"

def test_words_in_sentence_mixed():
    assert words_in_sentence("one two three four five") == "two four"

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("apple") == "apple"

def test_words_in_sentence_single_word_not_prime():
    assert words_in_sentence("banana") == ""

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("This is a very long sentence with many words") == "very long"

def test_words_in_sentence_with_spaces():
    assert words_in_sentence("  leading and trailing spaces  ") == "leading and"

def test_words_in_sentence_multiple_prime_length():
    assert words_in_sentence("abc def ghi jkl mno") == "abc def ghi mno"

def test_words_in_sentence_with_numbers():
    assert words_in_sentence("abc 123 def 456 ghi") == "abc def ghi"