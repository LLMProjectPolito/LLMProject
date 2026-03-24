
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
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_word():
    assert words_in_sentence("hello") == "hello"

def test_multiple_words():
    assert words_in_sentence("this is a test") == "is a test"

def test_example_1():
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_example_3():
    assert words_in_sentence("a b c d e") == "a b c d e"

def test_example_4():
    assert words_in_sentence("12345") == "12345"

def test_example_5():
    assert words_in_sentence("abc") == "abc"

def test_example_6():
    assert words_in_sentence("a b c d e f") == "a b c d e f"

def test_example_7():
    assert words_in_sentence("1234567890") == "1234567890"

def test_example_8():
    assert words_in_sentence("a b c d e f g h") == "a b c d e f g h"