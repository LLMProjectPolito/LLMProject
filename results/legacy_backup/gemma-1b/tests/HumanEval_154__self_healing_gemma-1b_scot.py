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