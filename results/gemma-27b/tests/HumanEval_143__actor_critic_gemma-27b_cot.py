
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
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return " ".join(prime_words)

# Tests for is_prime function
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(29) == True
    assert is_prime(97) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(0) == False
    assert is_prime(15) == False

# Tests for words_in_sentence function
# Basic Cases
def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == ""

# Edge Cases
def test_words_in_sentence_edge():
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""
    assert words_in_sentence("a") == "a"
    assert words_in_sentence("aa") == ""
    assert words_in_sentence("aaa") == "aaa"

# Longer Prime Lengths
def test_longer_primes():
    assert words_in_sentence("a very long sentence with words of length seven eleven thirteen") == "seven eleven thirteen"

# Mixed Lengths
def test_words_in_sentence_mixed():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the quick fox over the dog"
    assert words_in_sentence("one two three four five six seven eight nine ten") == "one two three five seven"

# Consolidation of redundant tests
def test_words_in_sentence_consolidated():
    assert words_in_sentence("a bb ccc dddd") == "a bb ccc"
    assert words_in_sentence("very long sentence with many words") == "very long"

# Input Validation
def test_words_in_sentence_invalid_input():
    assert words_in_sentence("hello, world!") == ""
    assert words_in_sentence("hello 123 world") == ""

# Leading/Trailing Spaces
def test_words_in_sentence_leading_trailing_spaces():
    assert words_in_sentence("  hello world  ") == ""

# Empty String/Whitespace Combined
def test_words_in_sentence_empty_whitespace():
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""

# Multiple Spaces Between Words
def test_words_in_sentence_multiple_spaces():
    assert words_in_sentence("hello   world") == ""