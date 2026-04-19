
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
    # Examples from docstring
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    # All words prime length
    ("he she likes it", "he she likes it"), # 2, 3, 5, 2
    ("hi there world", "hi there world"), # 2, 5, 5
    ("He ate apple", "He ate apple"), # 2, 3, 5
    # No words prime length
    ("This test a test", ""), # 4, 4, 1, 4
    ("a b c d", ""), # 1, 1, 1, 1
    ("banana applepie", ""), # 6, 9
    ("test school swimming football basketball", ""), # 4, 6, 8, 8, 10
    ("a test banana strength algorithm everything", ""), # 1, 4, 6, 8, 9, 10
    # Mixed lengths
    ("I am a student", "am student"), # 1, 2, 1, 7
    ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps the dog"), # 3, 5, 5, 3, 5, 4, 3, 4, 3
    ("to the great mountain wilderness", "to the great"), # 2, 3, 5, 8, 10
    ("abracadabra test", "abracadabra"), # 11, 4
    # Single word cases
    ("apple", "apple"), # 5 (prime)
    ("banana", ""), # 6 (non-prime)
    ("a", ""), # 1 (non-prime)
    ("is", "is"), # 2 (prime)
    # Boundary prime sequence
    ("to the apple station description", "to the apple station description"), # 2, 3, 5, 7, 11
])
def test_words_in_sentence_parametrized(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_max_length():
    # Test sentence close to 100 characters
    # 33 occurrences of "hi" (len 2) + 32 spaces + "a" (len 1) = 33*2 + 32 + 1 = 99 chars
    sentence = "hi " * 33 + "a"
    expected = " ".join(["hi"] * 33)
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_max_length_non_prime():
    # 10 words of length 9 (non-prime) + 9 spaces = 99 chars
    sentence = "ninechars " * 9 + "ninechars"
    assert words_in_sentence(sentence) == ""

def test_words_in_sentence_empty_or_whitespace():
    # While constraints say 1 <= len, testing robustness
    assert words_in_sentence(" ") == ""