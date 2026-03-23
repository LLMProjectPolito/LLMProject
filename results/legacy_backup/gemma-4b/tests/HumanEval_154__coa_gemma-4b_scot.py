import pytest
import math


# Focus: Boundary Values
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
    if b in a or any(rotation in a for rotation in rotate(b)):
        return True
    else:
        return False

def rotate(s):
    return s[1:] + s[0]

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `cycpattern_check` checks if a string `b` (or any of its rotations) is a substring of string `a`.
### Boundary values to test include empty strings, single-character strings, and strings where `b` is a prefix or suffix of `a`.
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_empty_strings
### - test_single_character_strings
### - test_prefix_suffix
### STEP 3: CODE - Write the high-quality pytest suite.
###
### test_empty_strings
### Test case: a = "abc", b = ""
### Test case: a = "", b = "abc"
### Test case: a = "", b = ""
###
### test_single_character_strings
### Test case: a = "abc", b = "a"
### Test case: a = "abc", b = "b"
### Test case: a = "abc", b = "c"
###
### test_prefix_suffix
### Test case: a = "abc", b = "ab"
### Test case: a = "abc", b = "bc"
### Test case: a = "abc", b = "abc"
### Test case: a = "abc", b = "cba"
###
###
def test_empty_strings():
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False
    assert cycpattern_check("", "") == True

def test_single_character_strings():
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == True
    assert cycpattern_check("abc", "c") == True

def test_prefix_suffix():
    assert cycpattern_check("abc", "ab") == True
    assert cycpattern_check("abc", "bc") == True
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "cba") == False

# Focus: Type Scenarios
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
    if b in a or any(rotation in a for rotation in [b[i:] + b[:i] for i in range(len(b))]):
        return True
    else:
        return False

@pytest.mark.type_scenario("substring")
def test_cycpattern_check_substring_present():
    assert cycpattern_check("hello", "ell") == True

@pytest.mark.type_scenario("substring_not_present")
def test_cycpattern_check_substring_absent():
    assert cycpattern_check("abcd", "abd") == False

@pytest.mark.type_scenario("rotation_present")
def test_cycpattern_check_rotation_present():
    assert cycpattern_check("abab", "baa") == True

# Focus: Logic Branches
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

def test_cycpattern_check_positive_rotation():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_negative_rotation():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_substring_within():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_substring_at_start():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_substring_middle():
    assert cycpattern_check("himenss", "simen") == True