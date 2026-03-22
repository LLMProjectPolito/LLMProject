import pytest

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

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
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("hello world", ""),
        ("a bb ccc dddd", "bb ccc"),
        ("the quick brown fox jumps over the lazy dog", "the quick fox jumps over"),
        ("one two three four five", "one three five"),
        ("a", ""),
        ("aa", "aa"),
        ("aaa", "aaa"),
        ("aaaa", ""),
        ("", ""),
        ("very long sentence with many words", "very long sentence with many words"),
        ("word", "word"),
        ("words", "words"),
        ("wordss", "wordss"),
        ("wordsss", "wordsss"),
        ("wordssss", ""),
        ("  This is a test  ", "is"),
        ("This   is  a   test", "is test"),
        ("is a test are", "is are"),
        ("123 abc 45 def", "abc def"),
        ("hello! world?", "hello world"),
        ("go no so", "go no so"),
        ("lets go for swimming and running", "go for"),
    ],
)
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected