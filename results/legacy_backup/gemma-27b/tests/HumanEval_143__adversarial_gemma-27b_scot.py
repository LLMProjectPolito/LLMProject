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
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("", ""),
        ("hello world", ""),
        ("is", "is"),
        ("lets go for swimming", "go for"),
        ("a bb ccc dddd", "bb ccc"),
        ("a", ""),
        ("aa", ""),
        ("abc", "abc"),
        ("  hello  world  ", ""),
        ("hello   world", "hello world"),
        ("a" * 99 + "b", ""),
        ("abc def ghi", "abc def ghi"),
        ("abc def ghi jklm", "abc def ghi jklm"),
        ("abc def ghi jklmn", "abc def ghi jklmn"),
        ("abc def ghi jklmno", "abc def ghi jklmno"),
        ("abc def ghi jklmnop", "abc def ghi jklmnop"),
        ("abc def ghi jklmnopq", "abc def ghi jklmnopq"),
        ("abc def ghi jklmnopqr", "abc def ghi jklmnopqr"),
        ("abc def ghi jklmnopqrs", "abc def ghi jklmnopqrs"),
        ("abc def ghi jklmnopqrstu", "abc def ghi jklmnopqrstu"),
        ("abc def ghi jklmnopqrstuv", "abc def ghi jklmnopqrstuv"),
        ("abc def ghi jklmnopqrstuvw", "abc def ghi jklmnopqrstuvw"),
        ("abc def ghi jklmnopqrstuvwx", "abc def ghi jklmnopqrstuvwx"),
        ("abc def ghi jklmnopqrstuvwxy", "abc def ghi jklmnopqrstuvwxy"),
        ("abc def ghi jklmnopqrstuvwxyz", "abc def ghi jklmnopqrstuvwxyz"),
    ],
)
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected