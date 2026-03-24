
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
    words = sentence.split()
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("a b c d") == "a b c d"
    assert words_in_sentence("abc") == "abc"
    assert words_in_sentence("12345") == "12345"
    assert words_in_sentence("1234567890") == "1234567890"
    assert words_in_sentence("") == ""
    assert words_in_sentence("a b c") == "a b c"
    assert words_in_sentence("a b c d e f") == "a b c d e f"
    assert words_in_sentence("a b c d e f g h") == "a b c d e f g h"
    assert words_in_sentence("a b c d e f g h i") == "a b c d e f g h i j"
    assert words_in_sentence("a b c d e f g h i j k") == "a b c d e f g h i j k l"
    assert words_in_sentence("a b c d e f g h i j k l m") == "a b c d e f g h i j k l m"
    assert words_in_sentence("a b c d e f g h i j k l m n") == "a b c d e f g h i j k l m n"
    assert words_in_sentence("a b c d e f g h i j k l m n o") == "a b c d e f g h i j k l m n o"
    assert words_in_sentence("a b c d e f g h i j k l m n o p") == "a b c d e f g h i j k l m n o p"
    assert words_in_sentence("a b c d e f g h i j k l m n o p q") == "a b c d e f g h i j k l m n o p q"
    print("All test cases passed!")