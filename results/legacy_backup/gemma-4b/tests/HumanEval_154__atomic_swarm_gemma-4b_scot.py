import pytest
import math

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

def test_basic():
    assert cycpattern_check("hello", "ell") == True

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if b in a or any(rotation in a for rotation in [b[i:] + b[:i] for i in range(len(b))]):
        return True
    else:
        return False
import pytest

def test_empty_b():
    assert cycpattern_check("abcd", "") == True

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
    if not isinstance(a, str) or not isinstance(b, str):
        return False

    if len(b) > len(a):
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

### SCoT Steps:
### STEP 1: REASONING - The function should handle invalid input types (non-strings) and cases where the second string is longer than the first.  It should also correctly identify rotations as substrings.
### STEP 2: PLAN - Test cases: 1. Non-string input. 2. b is longer than a. 3. A rotation of b is a substring of a. 4. No rotation of b is a substring of a.
### STEP 3: CODE -
def test_invalid_input_type():
    assert cycpattern_check(123, "abc") == False
    assert cycpattern_check("abc", 123) == False
    assert cycpattern_check(None, "abc") == False
    assert cycpattern_check("abc", None) == False