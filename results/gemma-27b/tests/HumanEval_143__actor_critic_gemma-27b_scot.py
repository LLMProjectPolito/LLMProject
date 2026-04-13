
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
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("four five six seven") == ""

def test_mixed_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_single_word_prime():
    assert words_in_sentence("two") == "two"

def test_single_word_non_prime():
    assert words_in_sentence("four") == ""

def test_sentence_with_spaces_returns_prime_words():
    assert words_in_sentence("  two three five  ") == "two three five"
    assert words_in_sentence("two  three   five") == "two three five"

def test_sentence_with_long_words_returns_prime_words():
    assert words_in_sentence("programming is fun") == "programming fun"

def test_sentence_with_non_letter_characters_raises_error():
    with pytest.raises(ValueError):
        words_in_sentence("123 abc")
    with pytest.raises(ValueError):
        words_in_sentence("a b c!")

def test_long_sentence_returns_prime_words():
    long_sentence = "a " * 90 + "two three five"
    assert words_in_sentence(long_sentence) == "two three five"

def test_is_prime_with_large_prime():
    assert is_prime(997) == True

def test_sentence_with_one_prime_word():
    assert words_in_sentence("hello two world") == "two"

def test_sentence_with_all_prime_words():
    assert words_in_sentence("two three five seven") == "two three five seven"