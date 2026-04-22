
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
    s = s.lower()
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
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

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


def test_is_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == False #case sensitive
    assert is_palindrome('Racecar') == False #case sensitive
    assert is_palindrome('madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False

def test_get_max():
    assert get_max([1, 2, 3]) == 3
    assert get_max([]) == None
    assert get_max([-1, -2, -3]) == -1
    assert get_max([5]) == 5
    assert get_max([1, 5, 2, 8, 3]) == 8
    assert get_max([-5, -1, -10]) == -1
    assert get_max([0,0,0]) == 0

def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["abc", "def", "ghi"]) == "abc"
    assert find_max(["aba", "abc", "abb"]) == "abc"
    assert find_max(["a", "aa", "aaa"]) == "aaa"
    assert find_max(["", "a", "aa"]) == "a"
    assert find_max(["abc", "bca", "cab"]) == "abc"
    assert find_max(["abc", "cba", "bac"]) == "abc"
    assert find_max(["abc", "def", "ghi", "abc"]) == "ghi"
    assert find_max(["abc", "def", "ghi", "abc", "def"]) == "ghi"
    assert find_max(["abc", "def", "ghi", "abc", "def", "ghi"]) == "abc"
    assert find_max(["a", "b", "c"]) == "a"
    assert find_max(["c", "b", "a"]) == "a"
    assert find_max(["ab", "ba"]) == "ab"
    assert find_max(["abc", "abd", "abe"]) == "abc"
    assert find_max(["abc", "ab", "a"]) == "abc"
    assert find_max(["abc", "abc", "abc"]) == "abc"
    assert find_max(["abc", "def", "ghi", "jkl", "mno"]) == "mno"
    assert find_max(["abc", "def", "ghi", "jkl", "mno", "abc"]) == "mno"
    assert find_max(["abc", "def", "ghi", "jkl", "mno", "abc", "def"]) == "mno"
    assert find_max(["abc", "def", "ghi", "jkl", "mno", "abc", "def", "ghi"]) == "mno"
    assert find_max(["abc", "def", "ghi", "jkl", "mno", "abc", "def", "ghi", "jkl"]) == "mno"