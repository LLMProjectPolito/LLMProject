
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

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
    if not a or not b:
        return False

    b_len = len(b)
    a_len = len(a)

    if b_len > a_len:
        return False

    for i in range(b_len):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_cycpattern_check_basic():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "acb") == True


def test_cycpattern_check_empty():
    assert cycpattern_check("", "abc") == False
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "") == False

def test_cycpattern_check_long_strings():
    assert cycpattern_check("verylongstring", "verylong") == True
    assert cycpattern_check("anotherverylongstring", "verylong") == True
    assert cycpattern_check("averyverylongstring", "verylongstring") == True
    assert cycpattern_check("verylongstring", "short") == False

def test_cycpattern_check_same_length_no_rotation():
  assert cycpattern_check("abc", "def") == False

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_b_same_as_a():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_edge_case_b_at_start():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_edge_case_b_at_end():
    assert cycpattern_check("abc", "cba") == True

def test_cycpattern_check_edge_case_b_equals_a_with_repeats():
    assert cycpattern_check("aaaa", "aa") == True
    assert cycpattern_check("aaaa", "aaa") == True
    assert cycpattern_check("aaaa", "a") == True
    assert cycpattern_check("aaaa", "") == False

def test_cycpattern_check_complex_case():
    assert cycpattern_check("aaaaaaaaaa", "a") == True
    assert cycpattern_check("abcabcabc", "abc") == True
    assert cycpattern_check("abcabcabc", "cab") == True
    assert cycpattern_check("abcabcabc", "bca") == True
    assert cycpattern_check("abcabcabc", "cba") == True

def test_cycpattern_check_mixed_case():
    assert cycpattern_check("Hello World", "ell") == True
    assert cycpattern_check("Hello World", "ElL") == True
    assert cycpattern_check("Hello World", "WORLD") == False

def test_cycpattern_check_special_chars():
    assert cycpattern_check("a!b@c#d", "b@c") == True
    assert cycpattern_check("a!b@c#d", "a!b") == True
    assert cycpattern_check("a!b@c#d", "c#d") == True
    assert cycpattern_check("a!b@c#d", "d") == True



def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_longer_string():
    assert is_palindrome('madam') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('refer') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True

def test_palindrome_not_palindrome():
    assert is_palindrome('hello') == False
    assert is_palindrome('world') == False
    assert is_palindrome('python') == False

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == False #Consider punctuation and spaces

def test_palindrome_with_spaces():
    assert is_palindrome('race car') == False
    assert is_palindrome('A man a plan a canal Panama') == False

def test_palindrome_with_special_chars():
    assert is_palindrome('A man, a plan, a canal: Panama') == False
    assert is_palindrome('Was it a car or a cat I saw?') == False

def test_palindrome_empty_string():
    assert is_palindrome("") == True