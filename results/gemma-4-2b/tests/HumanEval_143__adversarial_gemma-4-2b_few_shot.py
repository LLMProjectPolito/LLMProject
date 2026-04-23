
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


# --- Tests for is_palindrome ---
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True
    assert is_palindrome('b') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == True
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('  race car  ') == True

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([10, 5, 20, 1]) == 20
    assert get_max([1, 1, 1]) == 1

def test_max_empty():
    assert get_max([]) is None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-10, -5, -20]) == -5

def test_max_mixed():
    assert get_max([-1, 0, 1]) == 1
    assert get_max([0, -1, 1]) == 1

def test_max_single_element():
    assert get_max([5]) == 5

# --- Tests for words_in_sentence ---
def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_length():
    assert words_in_sentence("abc def ghi") == ""

def test_words_in_sentence_mixed():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == ""

def test_words_in_sentence_multiple_prime_length():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z") == ""

def test_words_in_sentence_with_spaces():
    assert words_in_sentence("  This is a test  ") == "is"
    assert words_in_sentence("lets go for swimming ") == "go for"