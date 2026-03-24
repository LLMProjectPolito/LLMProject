
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

from typing import Optional

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome (case-insensitive)."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    s = s.lower()
    return s == s[::-1].lower()

def get_max(arr: list[int]) -> Optional[int]:
    """Returns the maximum element in a list, or None if empty."""
    if not arr:
        return None
    return max(arr)

def words_in_sentence(sentence: str) -> str:
    """
    Returns a string containing words from the input sentence whose lengths are prime numbers,
    preserving the original order.

    If no words have prime lengths, an empty string is returned.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"
    """
    def is_prime(n: int) -> bool:
        """Checks if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):  # Optimization: check up to n // 2
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    # If no words have prime lengths, return an empty string.
    if not prime_words:
        return ""
    return " ".join(prime_words)


### Tests (Pytest):
import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_non_string():
    with pytest.raises(TypeError):
        is_palindrome(123)

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_words():
    assert words_in_sentence("This is a long sentence") == ""

def test_words_in_sentence_all_prime_words():
    assert words_in_sentence("go for a swim") == "go for a"

def test_words_in_sentence_mixed():
    assert words_in_sentence("This is a very long test") == "is a"

def test_words_in_sentence_whitespace():
    assert words_in_sentence("   ") == ""