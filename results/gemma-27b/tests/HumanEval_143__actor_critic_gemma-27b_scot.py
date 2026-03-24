
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

def test_empty_sentence_returns_empty_string():
    assert words_in_sentence("") == ""

def test_sentence_with_only_spaces_returns_empty_string():
    assert words_in_sentence("   ") == ""

def test_sentence_with_invalid_characters_raises_error():
    with pytest.raises(ValueError):
        words_in_sentence("hello 123 world!")

def test_prime_number_two():
    assert words_in_sentence("two") == "two"

def test_prime_number_eleven():
    assert words_in_sentence("programming") == "programming"

def test_no_prime_length_words():
    assert words_in_sentence("four five six seven") == ""

def test_all_prime_length_words():
    assert words_in_sentence("two three five seven") == "two three five seven"

def test_mixed_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_sentence_with_various_spaces():
    assert words_in_sentence("  two  three   five ") == "two three five"

def test_sentence_with_long_prime_word():
    assert words_in_sentence("programming is fun and challenging") == "programming"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("two four five seven eight") == "two five seven"

def test_long_sentence():
    long_sentence = "a " * 95 + "two three five"
    assert len(words_in_sentence(long_sentence)) > 0