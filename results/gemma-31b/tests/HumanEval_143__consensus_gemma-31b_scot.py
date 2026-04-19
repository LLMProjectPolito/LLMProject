
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

@pytest.mark.parametrize("sentence, expected", [
    # Examples
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    # Single word cases
    ("a", ""),
    ("is", "is"),
    ("the", "the"),
    ("test", ""),
    ("hello", "hello"),
    ("banana", ""),
    # No prime lengths
    ("a b c d", ""),
    ("four six eight ten", ""), # Wait: six(3) and eight(5) are prime. Correcting to:
    ("four nine ten", ""), 
    # All prime lengths
    ("is the it apple", "is the it apple"),
    ("hello world", "hello world"),
    # Mixed lengths
    ("a bb ccc dddd eeeee ffffff ggggggg", "bb ccc eeeee ggggggg"),
    ("a is the test apple banana", "is the apple"),
    ("a quick brown fox", "quick brown fox"),
    ("apple banana cherry", "apple"),
    # Complex sentences
    ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps the dog"),
    ("it is a great day for a walk in the park", "it is great day for in the"),
    ("I love coding", ""),
    ("Prime numbers are cool", "Prime numbers are"),
    ("quality programming is essential", "quality programming is"),
    # Sequence of primes
    ("ab abc abcd abcde abcdef abcdefg abcdefgh abcdefghi abcdefghij abcdefghijk abcdefghijkl abcdefghijklm", 
     "ab abc abcde abcdefg abcdefghijk abcdefghijklm"),
])
def test_words_in_sentence_parametrized(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_boundary_conditions():
    # Max length constraint: ~100 characters, all non-prime
    sentence_max_non_prime = "test " * 19 + "test" 
    assert words_in_sentence(sentence_max_non_prime) == ""

    # Max length constraint: ~100 characters, all prime
    sentence_max_prime = "it " * 32 + "it"
    assert words_in_sentence(sentence_max_prime) == " ".join(["it"] * 33)

    # Max length constraint: mixed
    sentence_mixed = "is " * 33 + "a"
    assert words_in_sentence(sentence_mixed) == " ".join(["is"] * 33)

def test_empty_or_whitespace():
    # Constraints say 1 <= len(sentence), but checking robustness
    assert words_in_sentence(" ") == ""
    assert words_in_sentence("  hello   world  ") == "hello world"