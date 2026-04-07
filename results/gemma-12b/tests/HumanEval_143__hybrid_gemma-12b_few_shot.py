
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
from typing import List

def is_prime(n: int) -> bool:
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence: str) -> str:
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
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


class TestWordsInSentence:
    def test_basic_case(self):
        assert words_in_sentence("This is a test") == "is"

    def test_multiple_prime_words(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_no_prime_words(self):
        assert words_in_sentence("This is not a palindrome") == ""

    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_single_prime_word(self):
        assert words_in_sentence("a") == "a"

    def test_single_non_prime_word(self):
        assert words_in_sentence("abc") == ""

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("This  is   a    test") == "is"

    def test_sentence_with_long_prime_word(self):
        assert words_in_sentence("This is a verylongprime word") == "verylongprime"

    def test_sentence_with_mixed_prime_and_non_prime(self):
        assert words_in_sentence("a bb ccc d") == "a"

    def test_sentence_with_numbers_as_words(self):
        assert words_in_sentence("1 2 3 5 7") == "5 7"

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("hello! world?") == ""

    def test_sentence_with_single_prime_word(self):
        assert words_in_sentence("a b c d e f g") == "a"

    def test_sentence_with_all_prime_words(self):
        assert words_in_sentence("a bb ccc dddd eeeee") == "a"

    def test_sentence_with_long_prime_words(self):
        assert words_in_sentence("This is a very long prime word") == "is a"

    def test_sentence_with_numbers_in_words(self):
        assert words_in_sentence("word1 word2 word3") == ""

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("word! word@ word#") == ""

    def test_sentence_with_mixed_case(self):
        assert words_in_sentence("This Is A Test") == "Is A"

    @pytest.mark.parametrize(
        "sentence, expected",
        [
            ("abc def ghi", "def"),
            ("a b c d e", "a b c d e"),
            ("hello world", ""),
            ("This is a very long prime word", "is a"),
            ("a", "a"),
            ("aa", ""),
            ("aaa", "aaa"),
            ("aaaa", ""),
            ("aaaaa", "aaaaa"),
            ("aaaaaa", ""),
            ("aaaaaaa", "aaaaaaa"),
        ],
    )
    def test_parametrize(self, sentence, expected):
        assert words_in_sentence(sentence) == expected


class TestPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True


class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None