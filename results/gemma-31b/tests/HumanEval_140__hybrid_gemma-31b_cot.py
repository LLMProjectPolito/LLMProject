
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

@pytest.mark.parametrize("input_text, expected_output", [
    # --- Basic cases from docstring ---
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # --- Edge cases: Empty, no spaces, and punctuation ---
    ("", ""),
    ("Hello", "Hello"),
    ("12345", "12345"),
    ("!@#$%^&*()", "!@#$%^&*()"),
    ("Hello, World!", "Hello,_World!"),
    ("123-456", "123-456"),
    ("!!!", "!!!"),
    ("Combined123", "Combined123"),
    
    # --- Pure space strings (Testing the 1, 2, 3+ logic) ---
    (" ", "_"),             # 1 space -> _
    ("  ", "__"),           # 2 spaces -> __
    ("   ", "-"),           # 3 spaces -> -
    ("    ", "-"),          # 4 spaces -> -
    ("     ", "-"),         # 5 spaces -> -
    
    # --- Leading and trailing spaces ---
    (" Hello", "_Hello"),
    ("Hello ", "Hello_"),
    ("  Hello", "__Hello"),
    ("   Hello", "-Hello"),
    ("Hello  ", "Hello__"),
    ("Hello   ", "Hello-"),
    (" Hello ", "_Hello_"),
    ("  Hello  ", "__Hello__"),
    ("   Hello   ", "-Hello-"),
    
    # --- Mixed sequences of spaces ---
    ("a b", "a_b"),
    ("a  b", "a__b"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("a b c", "a_b_c"),
    ("a  b  c", "a__b__c"),
    ("a   b   c", "a-b-c"),
    ("a b  c   d", "a_b__c-d"),
    ("a    b  c d   e", "a-b__c_d-e"),
    ("a b  c   d    e", "a_b__c-d-e"),
    ("  a b   c  d    e ", "__a_b-c__d-e_"),
    ("  a b   c  d    e  ", "__a_b-c__d-e__"),
    
    # --- Complex strings ---
    ("The quick brown fox", "The_quick_brown_fox"),
    ("The  quick   brown    fox", "The__quick-brown-fox"),
    ("   Multiple   spaces   here   ", "-Multiple-spaces-here-"),
    ("Check  2spaces  and 3spaces   ", "Check__2spaces__and_3spaces-"),
    
    # --- Non-space whitespace (Should remain unchanged) ---
    ("Hello\tWorld", "Hello\tWorld"),
    ("Hello\nWorld", "Hello\nWorld"),
    ("Hello\rWorld", "Hello\rWorld"),
    ("Hello\vWorld", "Hello\vWorld"),
    ("Hello\fWorld", "Hello\fWorld"),
])
def test_fix_spaces(input_text, expected_output):
    """
    Comprehensive test suite for fix_spaces.
    Logic:
    1 space -> '_'
    2 spaces -> '__'
    3+ spaces -> '-'
    Other characters and whitespace types remain untouched.
    """
    assert fix_spaces(input_text) == expected_output

def test_fix_spaces_long_string_repeating():
    """Test with a significantly longer repeating string to ensure consistency."""
    input_text = "a " * 100 + "  " + "b " * 100 + "   " + "c " * 100
    # "a " * 100 -> "a_" * 100
    # "  " -> "__"
    # "b " * 100 -> "b_" * 100
    # "   " -> "-"
    # "c " * 100 -> "c_" * 100
    expected = "a_" * 100 + "__" + "b_" * 100 + "-" + "c_" * 100
    assert fix_spaces(input_text) == expected

def test_fix_spaces_long_string_varied():
    """Test with a long string containing varied space gaps for stability."""
    input_str = "Word " + " " * 10 + "Word " + " " * 2 + "Word " + " " * 1 + "Word"
    # 10 spaces -> '-', 2 spaces -> '__', 1 space -> '_'
    expected = "Word-Word__Word_Word"
    assert fix_spaces(input_str) == expected