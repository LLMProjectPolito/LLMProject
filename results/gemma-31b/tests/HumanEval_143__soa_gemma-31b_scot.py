
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
    ("apple banana cherry", "apple"),
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps the dog"),
    ("I am a student", "am student"),
    ("a", ""),
    ("hi", "hi"),
    ("prime numbers are cool", "prime numbers are"),
    ("one two three four five six seven eight nine ten", "two three five seven"),
    ("A very long sentence to test the prime length logic of the words", "very long sentence test prime length logic the words"),
])
def test_words_in_sentence(sentence, expected):
    """
    Test the words_in_sentence function with various inputs to ensure it correctly
    filters words whose lengths are prime numbers.
    """
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_single_char_not_prime():
    """Test that words of length 1 are not considered prime."""
    assert words_in_sentence("i a o") == ""

def test_words_in_sentence_length_two_is_prime():
    """Test that words of length 2 are considered prime."""
    assert words_in_sentence("to be or no") == "to be or no"

def test_words_in_sentence_length_three_is_prime():
    """Test that words of length 3 are considered prime."""
    assert words_in_sentence("the cat sat") == "the cat sat"

def test_words_in_sentence_length_four_not_prime():
    """Test that words of length 4 are not considered prime."""
    assert words_in_sentence("this that") == ""

def test_words_in_sentence_max_constraint():
    """Test with a sentence close to the maximum length constraint (100)."""
    sentence = "the quick brown fox jumps over the lazy dog and then it runs away into the deep dark forest of doom"
    # Lengths:
    # the(3)P, quick(5)P, brown(5)P, fox(3)P, jumps(5)P, over(4)X, the(3)P, lazy(4)X, dog(3)P, 
    # and(3)P, then(4)X, it(2)P, runs(4)X, away(4)X, into(4)X, the(3)P, deep(4)X, dark(4)X, 
    # forest(6)X, of(2)P, doom(4)X
    expected = "the quick brown fox jumps the dog and it the of"
    assert words_in_sentence(sentence) == expected