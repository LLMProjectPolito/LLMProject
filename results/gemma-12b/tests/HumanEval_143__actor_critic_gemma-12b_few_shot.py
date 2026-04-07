
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

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome.

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    # Type check to handle non-string inputs
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s == s[::-1]

def get_max(arr: list[int]) -> int | None:
    """Returns the maximum element in a list, or None if empty.

    Args:
        arr: A list of integers.

    Returns:
        The maximum integer in the list, or None if the list is empty.
    """
    if not arr:
        return None
    return max(arr)

def words_in_sentence(sentence):
    """
    Returns a string containing words from the input sentence whose lengths are prime numbers,
    preserving the original order.

    Args:
        sentence: The input sentence (string).

    Returns:
        A string containing the prime-length words from the sentence, separated by spaces.
        Returns an empty string if no words have prime lengths.
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    # Clarify behavior when no prime-length words are found
    if not prime_words:
        return ""
    return " ".join(prime_words)

### Problem:
# No changes needed to the functions themselves based on the review.

### Tests (Pytest):
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

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_primes():
    assert words_in_sentence("This is a very long sentence") == ""

def test_words_in_sentence_all_primes():
    assert words_in_sentence("go for a swim") == "go for a"

def test_words_in_sentence_multiple_primes():
    assert words_in_sentence("go for a big run") == "go for a"

def test_words_in_sentence_single_length():
    assert words_in_sentence("a I to") == "a I"

def test_words_in_sentence_leading_trailing_spaces():
    assert words_in_sentence("  This   is  a  test  ") == "is"

def test_words_in_sentence_case_sensitivity():
    assert words_in_sentence("This Is A Test") == ""