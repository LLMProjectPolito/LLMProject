import pytest

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not b:
        return False
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False


class TestCycpatterCheck:

    def test_basic_true(self):
        assert cycpattern_check("hello", "ell") == True

    def test_basic_false(self):
        assert cycpattern_check("abcd", "abd") == False

    def test_rotation_true(self):
        assert cycpattern_check("abab", "baa") == True

    def test_no_rotation_true(self):
        assert cycpattern_check("himenss", "simen") == True

    def test_false_rotation(self):
        assert cycpattern_check("efef", "eeff") == False

    def test_empty_b(self):
        assert cycpattern_check("hello", "") == False

    def test_empty_a(self):
        assert cycpattern_check("", "hello") == False

    def test_both_empty(self):
        assert cycpattern_check("", "") == False

    def test_same_string(self):
        assert cycpattern_check("abc", "abc") == True

    def test_substring_match(self):
        assert cycpattern_check("abcdefg", "cde") == True

    def test_longer_b_than_a(self):
        assert cycpattern_check("abc", "abcdef") == False

    def test_case_sensitive(self):
        assert cycpattern_check("Hello", "ell") == False

    def test_special_characters(self):
        assert cycpattern_check("!@#$%^", "$%@!") == True

    def test_numbers(self):
        assert cycpattern_check("12345", "345") == True

    def test_mixed_characters(self):
        assert cycpattern_check("a1b2c3", "b2a") == True


@pytest.mark.parametrize("a, b, expected", [
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    ("abcde", "cde", True),
    ("abcde", "edc", False),
    ("abcde", "abc", True),
    ("abcde", "e", True),
    ("abcde", "", False),
    ("a", "a", True),
    ("a", "b", False),
    ("aaaaa", "aa", True),
    ("aaaaa", "aaa", True),
    ("aaaaa", "aaaaa", True),
    ("aaaaa", "aaaaaa", False),
    ("ababab", "bab", True),
    ("ababab", "aba", True),
    ("ababab", "babab", True),
    ("ababab", "ababab", True),
    ("ababab", "abababa", False),
    ("12345", "345", True),
    ("12345", "543", False),
    ("12345", "123", True),
    ("12345", "1", True),
    ("12345", "", False),
])
def test_cycpattern_check_parametrized(a, b, expected):
    assert cycpattern_check(a, b) == expected


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None