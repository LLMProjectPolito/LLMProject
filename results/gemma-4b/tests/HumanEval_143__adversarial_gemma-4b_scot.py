
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

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

### STEP 1: REASONING
# The function `words_in_sentence` takes a sentence as input and returns a new string containing only the words from the original sentence whose lengths are prime numbers, preserving the original order.
# We need to test various scenarios including:
# 1. Empty sentence: Should return an empty string.
# 2. Sentence with no prime-length words: Should return an empty string.
# 3. Sentence with one prime-length word: Should return that word.
# 4. Sentence with multiple prime-length words: Should return those words concatenated with spaces.
# 5. Sentence with a mix of prime and non-prime length words: Should return only the prime-length words.
# 6. Edge cases: short sentences, long sentences.

### STEP 2: PLAN
# Test functions:
# - test_empty_sentence: Tests the case where the input sentence is empty.
# - test_no_prime_words: Tests the case where no words have prime lengths.
# - test_single_prime_word: Tests the case where only one word has a prime length.
# - test_multiple_prime_words: Tests the case where multiple words have prime lengths.
# - test_mixed_prime_and_non_prime_words: Tests the case where some words have prime lengths and others don't.
# - test_edge_case_short: Tests a short sentence with prime words.
# - test_edge_case_long: Tests a long sentence with prime words.

### STEP 3: CODE
import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_words():
    assert words_in_sentence("hello world") == ""

def test_single_prime_word():
    assert words_in_sentence("test") == "test"

def test_multiple_prime_words():
    assert words_in_sentence("this is a test") == "is"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("hello world test") == "world test"

def test_edge_case_short():
    assert words_in_sentence("a b c") == "b"

def test_edge_case_long():
    assert words_in_sentence("this is a very long sentence") == "is"