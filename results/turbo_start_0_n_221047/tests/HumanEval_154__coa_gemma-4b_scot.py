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
### Test case: Both strings are empty.
### Test case: One string is empty, the other is not.
###
### test_single_character_strings
### Test case: Both strings have a single character.
### Test case: One string has a single character, the other does not.
###
### test_prefix_suffix
### Test case: b is a prefix of a.
### Test case: b is a suffix of a.
### Test case: b is a rotation of a.
###

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
    if b in a or any(rotation in a for rotation in rotate(b)):
        return True
    else:
        return False

def rotate(s):
    return s[1:] + s[0]

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# The test functions should focus solely on the 'Type Scenarios' dimension of the problem.
# We need to cover various combinations of input strings 'a' and 'b' to ensure the function behaves correctly.
# The scenarios should include cases where 'b' is a substring of 'a', a rotation of 'b' is a substring of 'a',
# and cases where 'b' is not a substring or rotation of 'a'.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_strings
# test_b_is_substring
# test_b_is_rotation
# test_b_is_not_substring
# test_b_is_rotation_but_not_substring

# STEP 3: CODE - Write the high-quality pytest suite.
###
@pytest.mark.parametrize("a, b, expected", [
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    ("", "", True),
    ("abc", "", True),
    ("", "abc", False),
    ("abc", "abcd", False),
    ("abc", "bcda", False),
])
def test_empty_strings(a, b, expected):
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    ("hello world", "ell", True),
    ("hello world", "wor", False),
    ("hello world", "ldwo", False),
    ("hello world", "world", False),
    ("hello world", "hello", True),
])
def test_b_is_substring(a, b, expected):
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    ("hello world", "ell", True),
    ("hello world", "wor", False),
    ("hello world", "ldwo", False),
    ("hello world", "world", False),
    ("hello world", "hello", True),
])
def test_b_is_rotation(a, b, expected):
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    ("hello world", "ell", True),
    ("hello world", "wor", False),
    ("hello world", "ldwo", False),
    ("hello world", "world", False),
    ("hello world", "hello", True),
])
def test_b_is_not_substring(a, b, expected):
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    ("hello world", "ell", True),
    ("hello world", "wor", False),
    ("hello world", "ldwo", False),
    ("hello world", "world", False),
    ("hello world", "hello", True),
])
def test_b_is_rotation_but_not_substring(a, b, expected):
    assert cycpattern_check(a, b) == expected

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
    if b in a or any(rotation in a for rotation in rotate(b)):
        return True
    else:
        return False

def rotate(s):
    return s[1:] + s[0]

### STEP 1: REASONING
# The function `cycpattern_check` checks if a substring of `b` (or any rotation of `b`) exists within `a`.
# We need to test various scenarios to ensure this logic is correct, focusing specifically on the branching logic of the `if` statement.
# Test cases should cover scenarios where `b` is a substring of `a`, where rotations of `b` are substrings of `a`, and where neither is.

# STEP 2: PLAN
# Test functions:
# 1. test_b_is_substring
# 2. test_rotation_is_substring
# 3. test_neither_is_substring

### STEP 3: CODE
def test_b_is_substring():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_rotation_is_substring():
    assert cycpattern_check("abcd", "bad") == True
    assert cycpattern_check("hello", "lohe") == True
    assert cycpattern_check("whassup", "supwh") == True
    assert cycpattern_check("abab", "aba") == True
    assert cycpattern_check("efef", "ffee") == True

def test_neither_is_substring():
    assert cycpattern_check("abcd", "abc") == False
    assert cycpattern_check("hello", "hell") == False
    assert cycpattern_check("whassup", "wass") == False
    assert cycpattern_check("abab", "abb") == False
    assert cycpattern_check("efef", "eff") == False
    assert cycpattern_check("himenss", "hime") == False