
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

def is_prime(n: int) -> bool:
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "a b c d e f g h i j k l m n o p q r s t u v w x y z"),
        ("one two three", "one"),
        ("short long medium", "short"),
        ("very very very long", "very"),
        ("", ""),
        (" ", ""),
        ("a", "a"),
        ("ab", "ab"),
        ("abc", "abc"),
        ("abcdef", "abc"),
        ("abcdefg", "abc"),
        ("abcdefgh", "abc"),
        ("abcdefghi", "abc"),
        ("abcdefghij", "abc"),
        ("abcdefghijk", "abc"),
        ("abcdefghijk", "abc"),
        ("abcdefghijkl", "abc"),
        ("abcdefghijklm", "abc"),
        ("abcdefghijklmn", "abc"),
        ("abcdefghijklmno", "abc"),
        ("abcdefghijklmnop", "abc"),
        ("abcdefghijklmnopq", "abc"),
        ("abcdefghijklmnopqr", "abc"),
        ("abcdefghijklmnopqrs", "abc"),
        ("abcdefghijklmnopqrstu", "abc"),
        ("abcdefghijklmnopqrstu", "abc"),
        ("abcdefghijklmnopqrstuvw", "abc"),
        ("abcdefghijklmnopqrstuvwxyz", "abc"),
        ("abcdefghijklmnopqrstuvwxy", "abc"),
        ("abcdefghijklmnopqrstuvwxyz", "abc"),
    ],
)
def test_words_in_sentence(sentence: str, expected: str):
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize(
    "sentence",
    [
        "This is a test",
        "lets go for swimming",
        "The quick brown fox jumps over the lazy dog",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "one two three",
        "short long medium",
        "very very very long",
        "",
        " ",
        "a",
        "ab",
        "abc",
        "abcdef",
        "abcdefg",
        "abcdefgh",
        "abcdefghi",
        "abcdefghij",
        "abcdefghijk",
        "abcdefghijkl",
        "abcdefghijklm",
        "abcdefghijklmn",
        "abcdefghijklmno",
        "abcdefghijklmnop",
        "abcdefghijklmnopq",
        "abcdefghijklmnopqr",
        "abcdefghijklmnopqrs",
        "abcdefghijklmnopqrstu",
        "abcdefghijklmnopqrstu",
        "abcdefghijklmnopqrstuvw",
        "abcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqrstuvwxy",
        "abcdefghijklmnopqrstuvwxyz",
    ],
)
def test_edge_cases(sentence):
    assert words_in_sentence(sentence) == "" if sentence == "" else words_in_sentence(sentence) == "" if sentence == " " else words_in_sentence(sentence) == "" if sentence == "a" else words_in_sentence(sentence) == "" if sentence == "ab" else words_in_sentence(sentence) == "" if sentence == "abc" else words_in_sentence(sentence) == "" if sentence == "abcdef" else words_in_sentence(sentence) == "" if sentence == "abcdefg" else words_in_sentence(sentence) == "" if sentence == "abcdefgh" else words_in_sentence(sentence) == "" if sentence == "abcdefghi" else words_in_sentence(sentence) == "" if sentence == "abcdefghij" else words_in_sentence(sentence) == "" if sentence == "abcdefghijk" else words_in_sentence(sentence) == "" if sentence == "abcdefghijkl" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklm" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmn" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmno" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnop" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopq" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopqr" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopqrs" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopqrstu" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopqrstu" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopqrstuvw" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopqrstuvwxyz" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopqrstuvwxy" else words_in_sentence(sentence) == "" if sentence == "abcdefghijklmnopqrstuvwxyz"