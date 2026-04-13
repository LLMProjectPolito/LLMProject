
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
    # --- Basic Cases ---
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    ("NoSpacesHere", "NoSpacesHere"),
    ("12345", "12345"),
    ("!@#$%^&*()", "!@#$%^&*()"),
    
    # --- Edge Case: Empty and Minimal Strings ---
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    
    # --- Logic: 1 Space (replaced by '_') ---
    ("a b", "a_b"),
    (" a", "_a"),
    ("a ", "a_"),
    (" a ", "_a_"),
    
    # --- Logic: 2 Spaces (replaced by '__') ---
    ("a  b", "a__b"),
    ("  a", "__a"),
    ("a  ", "a__"),
    ("  a  ", "__a__"),
    
    # --- Logic: 3+ Spaces (replaced by single '-') ---
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("   a", "-a"),
    ("a   ", "a-"),
    ("   Hello   ", "-Hello-"),
    
    # --- Mixed Space Lengths in Single String ---
    ("a b  c   d    e", "a_b__c-d-e"),
    ("   a b  c   ", "-a_b__c-"),
    ("  a b   c  d    e  ", "__a_b-c__d-e__"),
    ("   Hello   World   ", "-Hello-World-"),
    ("One  Two   Three    Four", "One__Two-Three-Four"),
    ("Multiple   spaces and  some_underscores", "Multiple-spaces_and__some_underscores"),
    
    # --- Special Characters, Numbers, and Non-Space Whitespace ---
    ("123 456", "123_456"),
    ("!@#   $%^", "!@#-$%^"),
    ("   1 2  3   4    5", "-1_2__3-4-5"),
    ("Hello\tWorld", "Hello\tWorld"),
    ("Hello\nWorld", "Hello\nWorld"),
    ("Hello\rWorld", "Hello\rWorld"),
    ("Hello \t World", "Hello_\t_World"),
    
    # --- Stress Tests / Long Sequences ---
    ("a" + " " * 10 + "b", "a-b"),
    (" " * 10, "-"),
    (" " * 2, "__"),
    (" " * 1, "_"),
    ("a" + " " * 3 + "b" + " " * 2 + "c" + " " * 1 + "d", "a-b__c_d"),
])
def test_fix_spaces(input_text, expected):
    """
    Comprehensive test for fix_spaces logic:
    1 space -> '_'
    2 spaces -> '__'
    3+ spaces -> '-'
    Other characters/whitespace -> unchanged
    """
    assert fix_spaces(input_text) == expected

def test_fix_spaces_non_string_input():
    """Ensure the function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces(123)

def test_fix_spaces_idempotency():
    """Test that running the function on its own output does not change the result."""
    text = "  Example   of   mixed   spaces  "
    first_pass = fix_spaces(text)
    second_pass = fix_spaces(first_pass)
    assert first_pass == second_pass

def test_fix_spaces_type_stability():
    """Ensure the function always returns a string regardless of input content."""
    assert isinstance(fix_spaces("test"), str)
    assert isinstance(fix_spaces("   "), str)
    assert isinstance(fix_spaces(""), str)