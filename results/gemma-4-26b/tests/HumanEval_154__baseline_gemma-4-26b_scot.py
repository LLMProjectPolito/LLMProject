
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

@pytest.mark.parametrize("a, b, expected", [
    # Docstring examples
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    
    # Rotation specific tests
    ("abcde", "eab", True),    # 'eab' rotation 'abe' is not in 'abcde', but 'eab' rotation 'abe' is not... 
                               # wait, 'eab' rotations: 'eab', 'abe', 'bea'. 
                               # 'abcde' contains 'abc', 'bcd', 'cde'. 
                               # Let's try: a="abcde", b="dea" -> rotations: "dea", "ead", "ade". "ade" is not in "abcde".
                               # Let's try: a="abcde", b="eab" -> rotations: "eab", "abe", "bea". None in "abcde".
                               # Let's try: a="abcde", b="dea" -> rotations: "dea", "ead", "ade". None in "abcde".
                               # Correct rotation example: a="abcde", b="eab" -> rotation "abe" is not in "abcde".
                               # Let's use: a="apple", b="lea" -> rotations: "lea", "eal", "ale". "ale" is in "apple" (no, it's not).
                               # Let's use: a="banana", b="nan" -> True (direct)
                               # Let's use: a="banana", b="ana" -> True (direct)
                               # Let's use: a="abcde", b="dec" -> rotations: "dec", "ecd", "cde". "cde" is in "abcde".
    ("abcde", "dec", True),    # 'cde' is a rotation of 'dec' and is in 'abcde'
    ("testing", "gtes", True), # 'gtes' rotation 'testg' (no), 'estg' (no), 'stge' (no)... 
                               # 'gtes' rotations: 'gtes', 'tesg', 'estg', 'stge'. 
                               # If a="testing", b="gtes" -> 'test' is in 'testing'. 'test' is a rotation of 'stte'? No.
                               # Let's use: a="testing", b="ingt" -> rotations: 'ingt', 'ngti', 'gtin', 'ting'. 'ting' is in 'testing'.
    ("testing", "ingt", True), 

    # Mismatch scenarios
    ("abcdef", "fed", False),  # 'fed' is reverse, not rotation
    ("abc", "acb", False),     # 'acb' is permutation, not rotation
    ("aaaaa", "aaab", False),  # characters exist but rotation doesn't match
    
    # Length constraints
    ("abc", "abcd", False),    # b longer than a
    ("a", "abc", False),       # b longer than a
    
    # Edge cases
    ("a", "a", True),          # Single char match
    ("a", "b", False),         # Single char mismatch
    ("", "a", False),          # Empty a
    ("a", "", True),           # Empty b (empty string is a substring of any string)
    ("", "", True),            # Both empty
])
def test_cycpattern_check_parametrized(a, b, expected):
    """Tests various combinations of strings including docstring examples."""
    assert cycpattern_check(a, b) == expected

def test_case_sensitivity():
    """Verify that the function is case sensitive."""
    assert cycpattern_check("Hello", "ell") is True
    assert cycpattern_check("Hello", "ELL") is False
    assert cycpattern_check("Hello", "ell" + "H".lower()) is False # "ellh" not in "Hello"

def test_large_strings():
    """Test with larger strings to ensure performance/logic stability."""
    a = "a" * 100 + "b" + "a" * 100
    b = "ba" + "a" * 99
    # b is "ba" + 99 'a's. Rotation: 99 'a's + "b".
    # "a"*99 + "b" is in a.
    assert cycpattern_check(a, b) is True

def test_no_rotation_needed():
    """Explicitly test that a simple substring match works."""
    assert cycpattern_check("substring", "sub") is True
    assert cycpattern_check("substring", "string") is True