
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

import pytest

@pytest.mark.parametrize("input_text, expected", [
    # Provided examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and whitespace only
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    
    # Space count variations
    ("a b", "a_b"),           # 1 space -> _
    ("a  b", "a__b"),         # 2 spaces -> __
    ("a   b", "a-b"),         # 3 spaces -> -
    ("a    b", "a-b"),        # 4 spaces -> -
    
    # Mixed sequences
    ("a b  c   d    e", "a_b__c-d-e"),
    ("  Example   of  spacing  ", "__Example-of__spacing__"),
    ("One Two   Three Four    Five", "One_Two-Three_Four-Five"),
    ("   Three   Spaces   Here   ", "-Three-Spaces-Here-"),
    ("  a   b  c ", "__a-b__c_"),
    ("   a  b   c  d    e   ", "-a__b-c__d-e-"),
    ("   a  b c   ", "-a__b_c-"),
    (" a  b   c    d     e", "_a__b-c-d-e"),
    
    # Leading and trailing spaces
    (" hello", "_hello"),
    ("hello ", "hello_"),
    ("  hello", "__hello"),
    ("   hello", "-hello"),
    ("hello  ", "hello__"),
    ("hello   ", "hello-"),
    
    # Strings with no spaces or other whitespace
    ("HelloWorld", "HelloWorld"),
    ("12345", "12345"),
    ("Example\t1", "Example\t1"),
    ("Example\n1", "Example\n1"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected