
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
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_words_in_sentence():
    # Basic examples
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == ""

    # Empty and single word cases
    assert words_in_sentence("") == ""  # Empty sentence should return an empty string
    assert words_in_sentence("a") == "a"  # Single word sentence should return the word if its length is prime

    # Multiple words with varying lengths
    assert words_in_sentence("a bb ccc dddd eeeee") == "bb ccc"
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the quick fox over the dog"

    # Representative prime and non-prime lengths
    assert words_in_sentence("one two three five seven eleven") == "one two three five seven eleven"

    # Edge case: Non-letter characters - should return empty string
    assert words_in_sentence("hello, world!") == ""
    assert words_in_sentence("123 abc") == ""

    # Long sentence with mixed prime and non-prime lengths
    long_sentence = " ".join(["a" * i for i in range(1, 21)])
    expected_output = " ".join([ "a" * i for i in [2, 3, 5, 7, 11, 13, 17, 19]])
    assert words_in_sentence(long_sentence) == expected_output

    # Test for large prime number
    large_prime_word = "a" * 101
    assert words_in_sentence(large_prime_word) == large_prime_word

    # Test with negative number (should handle gracefully)
    assert words_in_sentence("-1") == ""

    # Test with a sentence containing a negative number
    assert words_in_sentence("hello -1 world") == "hello world"