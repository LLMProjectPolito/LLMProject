
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
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for word in sentence.split():
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("the quick brown fox jumps over the lazy dog", "quick brown"),
        ("one two three four five", "one three five"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "b d f h j l n p r t v x"),
        ("hello world", "hello"),
        ("python is fun", "python fun"),
        ("a", "a"),
        ("", ""),
        ("123", ""),
        ("abcde", "abcde"),
    ],
)
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected


def test_empty_sentence():
    assert words_in_sentence("") == ""


def test_single_word():
    assert words_in_sentence("hello") == "hello"


def test_multiple_words_prime_lengths():
    assert words_in_sentence("abcde") == "abcde"


def test_multiple_words_no_prime_lengths():
    assert words_in_sentence("abcdefgh") == ""


def test_mixed_lengths():
    assert words_in_sentence("hello world") == "hello"


def test_long_sentence():
    sentence = "This is a very long sentence with many words"
    expected = "very long"
    assert words_in_sentence(sentence) == expected