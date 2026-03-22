import pytest

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
    if "   " in text:
        return text.replace("   ", "-")
    else:
        return text.replace(" ", "_")

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_fix_spaces_trailing_space():
    assert fix_spaces("Example 3 ") == "Example_3_"

def test_fix_spaces_multiple_space_sequences():
    assert fix_spaces("Example  1   2") == "Example_1-2"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  Example   Test  ") == "_Example-Test_"

def test_fix_spaces_long_string_with_multiple_spaces():
    long_string = "This is a long string with   multiple   spaces."
    expected_string = "This_is_a_long_string_with-multiple-spaces."
    assert fix_spaces(long_string) == expected_string

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""