
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
import math

@pytest.mark.parametrize("input_sentence, expected_output", [
    ("my cat is a pet", "my cat is pet"),
    ("I am a student", "am student"),
    ("I do a bit of work", "do bit of"),
])
def test_words_in_sentence(input_sentence, expected_output):
    """
    Tests that words_in_sentence correctly filters words based on prime lengths.
    Covers edge cases: length 1 (non-prime), length 2 (prime), and various prime/non-prime lengths.
    """
    assert words_in_sentence(input_sentence) == expected_output