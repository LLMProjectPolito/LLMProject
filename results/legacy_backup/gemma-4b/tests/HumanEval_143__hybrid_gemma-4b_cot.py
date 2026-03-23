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
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

names = ["words_in_sentence"]

@pytest.mark.parametrize(names, [
    ("This is a test"),
    ("lets go for swimming"),
    ("a b c d e"),
    ("hello world"),
    ("one two three"),
    ("prime prime prime"),
    ("notprime notprime"),
    (""),
    ("a"),
    ("ab"),
    ("abc")
])
def test_words_in_sentence(sentence):
    assert words_in_sentence(sentence) == " ".join([word for word in sentence.split() if is_prime(len(word))])

@pytest.mark.parametrize("sentence", [
    "123",
    "abc123def",
    "a123b",
    "123a",
])
def test_invalid_input(sentence):
    with pytest.raises(TypeError):
        words_in_sentence(sentence)