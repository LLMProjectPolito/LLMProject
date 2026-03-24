
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
    s = s.lower()
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

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("This  is   a    test") == "is"

    def test_sentence_with_single_prime_word(self):
        assert words_in_sentence("a") == "a"

    def test_sentence_with_all_prime_words(self):
        assert words_in_sentence("go for a run") == "go for a"

    def test_sentence_with_long_words(self):
        assert words_in_sentence("This is a very long sentence") == "is"

    def test_sentence_with_numbers_in_words(self):
        assert words_in_sentence("This is 2 a test") == "is"

    @pytest.mark.parametrize(
        "sentence, expected",
        [
            ("abc def ghi", "def"),
            ("a b c d e f g", "a b c d e f g"),
            ("hello world", ""),
            ("This is a test sentence", "is a"),
            ("The quick brown fox jumps over the lazy dog", "The fox the"),
        ],
    )
    def test_parametrized_cases(self, sentence, expected):
        assert words_in_sentence(sentence) == expected


class TestPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

    def test_palindrome_case_insensitive(self):
        assert is_palindrome("Racecar") == True
        assert is_palindrome("Madam") == True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("A man, a plan, a canal: Panama") == False # Spaces are not handled

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None

    def test_max_negative(self):
        assert get_max([-1, -2, -3]) == -1

    def test_max_mixed(self):
        assert get_max([-1, 2, -3, 4]) == 4