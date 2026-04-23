
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    max_unique_chars = -1
    result = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word
    return result

import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('racecar') == True
    assert is_palindrome('madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome('refer') == True
    assert is_palindrome('redder') == True
    assert is_palindrome('reviver') == True
    assert is_palindrome('civic') == True
    assert is_palindrome('wow') == True
    assert is_palindrome('a man a plan a canal panama') == False
    assert is_palindrome('A man a plan a canal Panama') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([10, 20, 30, 40]) == 40
    assert get_max([1, 5, 2, 8, 3]) == 8
    assert get_max([100, 200, 300]) == 300
    assert get_max([1, 1, 1, 1]) == 1

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-10, -20, -30]) == -10
    assert get_max([-1, 5, -2, 8, -3]) == 8
    assert get_max([-100, -200, -300]) == -100
    assert get_max([-1, -1, -1, -1]) == -1

def test_find_max_empty():
    assert find_max([]) == ""

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["abc", "def", "ghi"]) == "abc"
    assert find_max(["abc", "def", "ghi", "abc"]) == "abc"
    assert find_max(["abc", "def", "ghi", "abc", "def"]) == "abc"
    assert find_max(["abc", "def", "ghi", "abc", "def", "ghi"]) == "abc"

def test_find_max_duplicates():
    assert find_max(["aaaaaaa", "aaaaaaa", "aaaaaaa"]) == "aaaaaaa"
    assert find_max(["aaaaaaa", "bb", "cc", "aaaaaaa"]) == "aaaaaaa"
    assert find_max(["abc", "def", "ghi", "abc", "def", "ghi"]) == "abc"

def test_find_max_mixed():
    assert find_max(["abc", "def", "ghi", "abc", "def", "ghi", "abc"]) == "abc"
    assert find_max(["abc", "def", "ghi", "abc", "def", "ghi", "abc", "def"]) == "abc"
    assert find_max(["abc", "def", "ghi", "abc", "def", "ghi", "abc", "def", "ghi"]) == "abc"
    assert find_max(["abc", "def", "ghi", "abc", "def", "ghi", "abc", "def", "ghi", "abc"]) == "abc"
    assert find_max(["abc", "def", "ghi", "abc", "def", "ghi", "abc", "def", "ghi", "abc", "def"]) == "abc"