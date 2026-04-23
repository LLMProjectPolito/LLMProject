
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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



@pytest.mark.parametrize("input_string, expected", [
    ("radar", "radar"),
    ("hello", "hello"),
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("madam", "madam"),
    ("racecar", "racecar"),
    ("A man, a plan, a canal: Panama", "amanaplanacanalpanama"),
    ("Was it a car or a cat I saw?", "wasitacaroracatisaw"),
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("one two three", "one"),
    ("I am a", "I am a"),
    ("abcde", "abcde"),
    ("abcdef", "abcdef"),
    ("a", "a"),
    ("b", "b"),
    ("c", "c"),
])
def test_is_palindrome_parametrize(input_string, expected):
    assert is_palindrome(input_string) == expected



@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3], 3),
    ([], None),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 100], 100),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 101], 101),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1011], 1011),
])
def test_get_max_parametrize(input_list, expected):
    assert get_max(input_list) == expected

@pytest.mark.parametrize("input_string, expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("one two three", "one"),
    ("I am a", "I am a"),
    ("abcde", "abcde"),
    ("abcdef", "abcdef"),
    ("a", "a"),
    ("b", "b"),
    ("c", "c"),
    ("hello world", "world"),
    ("a b c", "c"),
    ("hello", "hello"),
    ("123", "123"),
    ("abcde", "abcde"),
    ("abc", "abc")
])
def test_words_in_sentence_parametrize(input_string, expected):
    assert words_in_sentence(input_string) == expected

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_length():
    assert words_in_sentence("abc def ghi") == ""

def test_words_in_sentence_single_word_prime_length():
    assert words_in_sentence("abc") == "abc"

def test_words_in_sentence_single_word_not_prime_length():
    assert words_in_sentence("abcd") == ""

def test_words_in_sentence_mixed_prime_non_prime():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_more_complex():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_longer_sentence():
    assert words_in_sentence("The quick brown fox jumps over the lazy dog") == "quick brown"

def test_words_in_sentence_with_spaces():
    assert words_in_sentence("  This  is   a    test  ") == "is"

def test_words_in_sentence_with_special_chars():
    assert words_in_sentence("a!b@c#d$e%f^g&h*i(j)k+l=m;n'o'') == ""