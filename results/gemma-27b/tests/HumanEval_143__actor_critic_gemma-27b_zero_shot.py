
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

    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_prime_length_word():
    assert words_in_sentence("a") == "a"

def test_example_1():
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_all_prime_length_words():
    assert words_in_sentence("a bb ccc dddd eeeee") == "a bb ccc"

def test_all_non_prime_length_words():
    assert words_in_sentence("aa bbb cccc ddddd") == ""

def test_mixed_prime_and_non_prime_lengths():
    assert words_in_sentence("a aa bbb ccc dddd") == "a ccc"

def test_long_sentence():
    sentence = "a bb ccc dddd eeeee ffffff ggggggg hhhhhhhh iiiiiiiii"
    assert words_in_sentence(sentence) == "a bb ccc eeeee"

def test_invalid_input_numbers():
    with pytest.raises(ValueError):
        words_in_sentence("1 23 456")

def test_invalid_input_special_chars():
    with pytest.raises(ValueError):
        words_in_sentence("!@# $")

def test_large_prime_length():
    assert words_in_sentence("a" + "b" * 97) == "a"

def test_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_length_constraint():
    long_sentence = "a " * 100
    assert words_in_sentence(long_sentence) == "a " * 100