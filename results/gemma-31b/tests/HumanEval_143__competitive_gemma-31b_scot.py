
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
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("a b c d", ""),
    ("hello world", "hello world"),
    ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps the dog"),
    ("I am a student", "am"),
    ("Prime numbers are cool", "Prime numbers are"),
    ("a", ""),
    ("is", "is"),
    ("the", "the"),
    ("this", ""),
    ("apple", "apple"),
    ("banana", ""),
    ("", ""),
    ("abcdefghijk", "abcdefghijk"), # length 11 is prime
    ("abcdefghij", ""), # length 10 is not prime
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_sentence_with_single_word_prime():
    assert words_in_sentence("cat") == "cat"

def test_sentence_with_single_word_non_prime():
    assert words_in_sentence("book") == ""

def test_sentence_with_all_non_prime_lengths():
    assert words_in_sentence("a test book") == ""

def test_sentence_with_all_prime_lengths():
    assert words_in_sentence("go for it") == "go for it"

def test_max_constraint_length():
    # 100 characters, words of length 2 (prime)
    sentence = "is " * 33 + "is" # 33*3 + 2 = 101 (too long), 32*3 + 2 = 98
    sentence = "is " * 32 + "is" 
    expected = " ".join(["is"] * 33)
    assert words_in_sentence(sentence) == expected