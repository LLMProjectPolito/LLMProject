import pytest

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0 or len(b) == 0:
        return False

    if len(a) == 1 and len(b) == 1:
        return a.lower() in b.lower()

    if len(a) == 1:
        return a.lower() in b.lower()

    if len(b) == 1:
        return b.lower() in a.lower()

    for i in range(1, len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

def test_cycpattern_check():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

    # Edge cases
    assert cycpattern_check("", "") == False
    assert cycpattern_check("a", "") == False
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "cba") == True
    assert cycpattern_check("abc", "bc") == True
    assert cycpattern_check("abc", "ac") == True
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == True
    assert cycpattern_check("abc", "c") == True
    assert cycpattern_check("abc", "d") == False
    assert cycpattern_check("abcd", "d") == False
    assert cycpattern_check("abcd", "abc") == False
    assert cycpattern_check("abcd", "ab") == False
    assert cycpattern_check("abcd", "a") == False
    assert cycpattern_check("abcd", "b") == False
    assert cycpattern_check("abcd", "c") == False
    assert cycpattern_check("abcd", "d") == False
    assert cycpattern_check("abcd", "e") == False
    assert cycpattern_check("abcd", "f") == False
    assert cycpattern_check("abcd", "g") == False
    assert cycpattern_check("abcd", "h") == False
    assert cycpattern_check("abcd", "i") == False
    assert cycpattern_check("abcd", "j") == False
    assert cycpattern_check("abcd", "k") == False
    assert cycpattern_check("abcd", "l") == False
    assert cycpattern_check("abcd", "m") == False
    assert cycpattern_check("abcd", "n") == False
    assert cycpattern_check("abcd", "o") == False
    assert cycpattern_check("abcd", "p") == False
    assert cycpattern_check("abcd", "q") == False
    assert cycpattern_check("abcd", "r") == False
    assert cycpattern_check("abcd", "s") == False
    assert cycpattern_check("abcd", "t") == False
    assert cycpattern_check("abcd", "u") == False
    assert cycpattern_check("abcd", "v") == False
    assert cycpattern_check("abcd", "w") == False
    assert cycpattern_check("abcd", "x") == False
    assert cycpattern_check("abcd", "y") == False
    assert cycpattern_check("abcd", "z") == False
    print("All test cases passed")