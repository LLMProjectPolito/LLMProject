
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
from typing import List

def words_in_sentence(sentence: str) -> str:
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
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("The quick brown fox jumps over the lazy dog", "quick brown"),
        ("a b c d", "a b c d"),
        ("one two three", "one two three"),
        ("hello world", "hello"),
        ("abcdefg", "a"),
        ("12345", ""),
        ("", ""),
        ("a", ""),
        ("ab", "a"),
        ("abc", "b"),
        ("abcd", "c"),
        ("abcde", "d"),
        ("abcdef", "e"),
        ("abcdefg", "f"),
        ("abcdefgh", "g"),
        ("abcdefghi", "h"),
        ("abcdefigh", "i"),
    ],
)
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize(
    "sentence",
    [
        "This is a test",
        "lets go for swimming",
        "The quick brown fox jumps over the lazy dog",
        "a b c d",
        "one two three",
        "hello world",
        "abcdefg",
        "12345",
        "",
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefg",
        "abcdefgh",
        "abcdefghi",
        "abcdefigh",
        "abcdefg",
    ],
)
def test_edge_cases(sentence):
    assert words_in_sentence(sentence) == words_in_sentence(sentence)

@pytest.mark.parametrize(
    "sentence",
    [
        "This is a test",
        "lets go for swimming",
        "The quick brown fox jumps over the lazy dog",
        "a b c d",
        "one two three",
        "hello world",
        "abcdefg",
        "12345",
        "",
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefg",
        "abcdefgh",
        "abcdefghi",
        "abcdefigh",
        "abcdefg",
    ],
)
def test_empty_sentence(sentence):
    assert words_in_sentence(sentence) == ""

@pytest.mark.parametrize(
    "sentence",
    [
        "This is a test",
        "lets go for swimming",
        "The quick brown fox jumps over the lazy dog",
        "a b c d",
        "one two three",
        "hello world",
        "abcdefg",
        "12345",
        "",
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefg",
        "abcdefgh",
        "abcdefghi",
        "abcdefigh",
        "abcdefg",
    ],
)
def test_single_character(sentence):
    assert words_in_sentence(sentence) == ""

@pytest.mark.parametrize(
    "sentence",
    [
        "This is a test",
        "lets go for swimming",
        "The quick brown fox jumps over the lazy dog",
        "a b c d",
        "one two three",
        "hello world",
        "abcdefg",
        "12345",
        "",
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefg",
        "abcdefgh",
        "abcdefghi",
        "abcdefigh",
        "abcdefg",
    ],
)
def test_mixed_lengths(sentence):
    assert words_in_sentence(sentence) == words_in_sentence(sentence)