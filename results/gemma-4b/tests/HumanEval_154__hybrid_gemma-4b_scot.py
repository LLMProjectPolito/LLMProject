
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
    if b in a or b in a[1:] or b in a[:-1]:
        return True
    else:
        return False

### SCoT Steps:

### STEP 1: REASONING
# The function `cycpattern_check` checks if a given string `b` (or any of its rotations) is a substring of another string `a`.
# The function should handle cases where `b` is an exact match, a rotation of `b` is an exact match, or `b` is a substring of `a` but not a rotation.
# The function should also handle edge cases like empty strings or when `b` is longer than `a`.
# The function should return `True` if `b` or any of its rotations is a substring of `a`, and `False` otherwise.

### STEP 2: PLAN
# Test cases:
# 1. Exact match: "abcd", "abd" - Expected: False
# 2. Rotation match: "hello", "ell" - Expected: True
# 3. No match: "whassup", "psus" - Expected: False
# 4. Rotation match: "abab", "baa" - Expected: True
# 5. No match: "efef", "eeff" - Expected: False
# 6. Rotation match: "himenss", "simen" - Expected: True
# 7. Empty string b - Expected: False
# 8. Empty string a - Expected: False
# 9. b longer than a - Expected: False
# 10. b is a substring of a but not a rotation - "abcd", "bcda" - Expected: False

### STEP 3: CODE
### pytest suite
def test_exact_match():
    assert cycpattern_check("abcd", "abd") == False

def test_rotation_match():
    assert cycpattern_check("hello", "ell") == True

def test_no_match():
    assert cycpattern_check("whassup", "psus") == False

def test_rotation_match2():
    assert cycpattern_check("abab", "baa") == True

def test_no_match2():
    assert cycpattern_check("efef", "eeff") == False

def test_rotation_match3():
    assert cycpattern_check("himenss", "simen") == True

def test_empty_string_b():
    assert cycpattern_check("abcd", "") == False

def test_empty_string_a():
    assert cycpattern_check("", "abd") == False

def test_b_longer_than_a():
    assert cycpattern_check("abcd", "abcde") == False

def test_substring_not_rotation():
    assert cycpattern_check("abcd", "bcda") == False