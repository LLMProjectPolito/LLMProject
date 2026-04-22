
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
    def is_prime(n):
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
        ("hello world", "world"),
        ("one two three", "two"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "b d f h j l n p r t v x"),
        ("short", "short"),
        ("verylongword", "verylongword"),
        ("a very very long word", "very very"),
        ("", ""),
        (" ", ""),
        ("  multiple   spaces  ", ""),
        ("abcdefghijk", "bdfh"),
    ],
)
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("hello world", "world"),
        ("one two three", "two"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "b d f h j l n p r t v x"),
        ("short", "short"),
        ("verylongword", "verylongword"),
        ("a very very long word", "very very"),
        ("", ""),
        (" ", ""),
        ("  multiple   spaces  ", ""),
        ("abcdefghijk", "bdfh"),
    ]
)
def test_empty_string(sentence, expected):
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("hello world", "world"),
        ("one two three", "two"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "b d f h j l n p r t v x"),
        ("short", "short"),
        ("verylongword", "verylongword"),
        ("a very very long word", "very very"),
        ("", ""),
        (" ", ""),
        ("  multiple   spaces  ", ""),
        ("abcdefghijk", "bdfh"),
    ]
)
def test_multiple_spaces(sentence, expected):
    assert words_in_sentence(sentence) == expected