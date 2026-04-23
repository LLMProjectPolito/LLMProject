
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

    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()

@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("hello world", "hello"),
        ("a b c d e", "a b e"),
        ("abcdefgh", "abc"),
        ("short", "short"),
        ("verylongword", "verylongword"),
        ("one two three four five", "one two three five"),
        ("a", "a"),
        ("", ""),
        ("abcde", "abcde"),
        ("abcdefghijk", "abc"),
        ("aaaaaaaaaa", ""),
        ("12345", ""), # Test with non-letter characters
        ("  leading and trailing spaces  ", "leading and trailing spaces"),
        (" ", ""), # Test case for spaces only
    ],
)
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_is_prime_small_numbers():
    assert not is_prime(1)
    assert is_prime(2)
    assert not is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert is_prime(9)
    assert not is_prime(10)

def test_words_in_sentence_empty_string():
    assert words_in_sentence("") == ""

def test_words_in_sentence_single_word():
    assert words_in_sentence("hello") == "hello"

def test_words_in_sentence_multiple_prime_length_words():
    assert words_in_sentence("abcde") == "abcde"

def test_words_in_sentence_no_prime_length_words():
    assert words_in_sentence("abcdefgh") == "abc"