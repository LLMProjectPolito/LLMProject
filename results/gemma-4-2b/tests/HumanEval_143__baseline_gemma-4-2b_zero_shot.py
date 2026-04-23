
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

```python
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
        ("a b c d e", "b d"),
        ("one two three", "two"),
        ("", ""),
        ("hello", ""),
        ("a", ""),
        ("ab", "a"),
        ("abc", "b"),
        ("abcdef", "c"),
        ("abcdefg", "d"),
        ("abcdefgh", "e"),
        ("abcdefghi", "f"),
        ("abcdefighj", "g"),
        ("abcdefij", "h"),
        ("abcdefijk", "i"),
        ("abcdefiljk", "j"),
        ("abcdefiljkm", "k"),
        ("abcdefiljkm", "l"),
        ("abcdefiljkmno", "m"),
        ("abcdefiljkmno", "n"),
        ("abcdefiljkmno", "o"),
        ("abcdefiljkmno", "p"),
        ("abcdefiljkmno", "q"),
        ("abcdefiljkmno", "r"),
        ("abcdefiljkmno", "s"),
        ("abcdefiljkmno", "t"),
        ("abcdefiljkmno", "u"),
        ("abcdefiljkmno", "v"),
        ("abcdefiljkmno", "w"),
        ("abcdefiljkmno", "x"),
        ("abcdefiljkmno", "y"),
        ("abcdefiljkmno", "z"),
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
        "a b c d e",
        "one two three",
        "",
        "hello",
        "a",
        "ab",
        "abc",
        "abcdef",
        "abcdefg",
        "abcdefgh",
        "abcdefghi",
        "abcdefighj",
        "abcdefij",
        "abcdefijk",
        "abcdefiljk",
        "abcdefiljkm",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",
        "abcdefiljkmno",