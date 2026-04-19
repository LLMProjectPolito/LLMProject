
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

@pytest.mark.parametrize("sentence, expected", [
    ("I love my dog", "my dog"),
    ("a bb c ddd e ffff ggggg", "bb ddd ggggg"),
    ("a test a test", ""),
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected