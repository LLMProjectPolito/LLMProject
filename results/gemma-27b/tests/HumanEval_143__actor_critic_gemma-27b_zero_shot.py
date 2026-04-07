
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
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_example_1():
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_all_prime_words():
    assert words_in_sentence("is are was") == "is are was"

def test_all_non_prime_words():
    assert words_in_sentence("a an the") == ""

def test_mixed_prime_and_non_prime():
    assert words_in_sentence("hello is a world") == "is"

def test_long_sentence():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "over dog"

def test_invalid_input_whitespace():
    assert words_in_sentence("  is   a    test  ") == ""

def test_invalid_input_non_letters():
    assert words_in_sentence("hello123 world!") == ""

def test_prime_non_prime_mix():
    assert words_in_sentence("one two three four five six seven") == "three five seven"

def test_boundary_lengths():
    assert words_in_sentence("a ab abc abcd abcde") == "ab abc abcde"

def test_long_word():
    long_word = "a" * 53  # A prime number
    assert words_in_sentence(long_word) == long_word

def test_word_length_two():
    assert words_in_sentence("is") == "is"

def test_sentence_too_long():
    long_sentence = "a " * 101
    assert words_in_sentence(long_sentence) == ""