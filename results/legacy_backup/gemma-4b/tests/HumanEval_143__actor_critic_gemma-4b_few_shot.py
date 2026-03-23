import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

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


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Madam') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('A121A') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed_positive_negative():
    assert get_max([-1, 2, -3, 4]) == 4

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_prime_words():
    assert words_in_sentence("This is a test") == ""

def test_words_in_sentence_all_prime_words():
    assert words_in_sentence("abc def ghi") == "def"

def test_words_in_sentence_empty_sentence():
    assert words_in_sentence("") == ""

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("abc") == "abc"

def test_words_in_sentence_single_word_non_prime():
    assert words_in_sentence("abcd") == ""

def test_words_in_sentence_multiple_prime_words():
    assert words_in_sentence("This is a test sentence") == "is a"

def test_is_prime_small_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False

def test_is_prime_larger_numbers():
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(19) == True
    assert is_prime(23) == True
    assert is_prime(29) == True
    assert is_prime(31) == True
    assert is_prime(37) == True
    assert is_prime(41) == True
    assert is_prime(43) == True
    assert is_prime(47) == True
    assert is_prime(53) == True
    assert is_prime(59) == True
    assert is_prime(61) == True
    assert is_prime(67) == True
    assert is_prime(71) == True
    assert is_prime(73) == True
    assert is_prime(79) == True
    assert is_prime(83) == True
    assert is_prime(89) == True
    assert is_prime(97) == True