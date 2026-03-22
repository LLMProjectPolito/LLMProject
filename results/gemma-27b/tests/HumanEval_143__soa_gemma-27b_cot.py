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

def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == ""
    assert words_in_sentence("a bb ccc dddd") == "a bb ccc"
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the quick fox over the dog"
    assert words_in_sentence("one two three four five six seven eight nine ten") == "one two three five seven"
    assert words_in_sentence("") == ""
    assert words_in_sentence("a") == "a"
    assert words_in_sentence("aa") == ""
    assert words_in_sentence("abc") == "abc"
    assert words_in_sentence("abcd") == ""
    assert words_in_sentence("abcde") == "abcde"
    assert words_in_sentence("abcdef") == ""
    assert words_in_sentence("abcdefg") == "abcdefg"
    assert words_in_sentence("abcdefgh") == ""
    assert words_in_sentence("abcdefghi") == "abcdefghi"
    assert words_in_sentence("abcdefghij") == ""
    assert words_in_sentence("abcdefghijk") == "abcdefghijk"
    assert words_in_sentence("abcdefghijkl") == ""
    assert words_in_sentence("abcdefghijklm") == "abcdefghijklm"
    assert words_in_sentence("abcdefghijklmn") == ""
    assert words_in_sentence("abcdefghijklmno") == "abcdefghijklmno"
    assert words_in_sentence("abcdefghijklmnop") == ""
    assert words_in_sentence("abcdefghijklmnopq") == "abcdefghijklmnopq"
    assert words_in_sentence("abcdefghijklmnopqr") == ""
    assert words_in_sentence("abcdefghijklmnopqrs") == "abcdefghijklmnopqrs"
    assert words_in_sentence("abcdefghijklmnopqrst") == ""
    assert words_in_sentence("abcdefghijklmnopqrstu") == "abcdefghijklmnopqrstu"
    assert words_in_sentence("abcdefghijklmnopqrstuv") == ""
    assert words_in_sentence("abcdefghijklmnopqrstuvw") == "abcdefghijklmnopqrstuvw"
    assert words_in_sentence("abcdefghijklmnopqrstuvwx") == ""
    assert words_in_sentence("abcdefghijklmnopqrstuvwxy") == "abcdefghijklmnopqrstuvwxy"
    assert words_in_sentence("abcdefghijklmnopqrstuvwxyz") == ""
    assert words_in_sentence("word1 word2 word3") == "word1 word2 word3"
    assert words_in_sentence("word11 word22 word33") == "word11 word22 word33"