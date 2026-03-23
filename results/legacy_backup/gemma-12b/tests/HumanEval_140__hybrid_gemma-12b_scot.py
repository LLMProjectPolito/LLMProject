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
    result = ""
    i = 0
    while i < len(text):
        if text[i] == ' ':
            if i + 1 < len(text) and text[i+1] == ' ' and i + 2 < len(text) and text[i+2] == ' ':
                result += "-"
                i += 3
            else:
                result += "_"
                i += 1
        else:
            result += text[i]
            i += 1
    return result

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces("Example 1 2") == "Example_1_2"

def test_consecutive_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_leading_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_trailing_spaces():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_leading_and_trailing_spaces():
    assert fix_spaces("  Example 2  ") == "__Example_2__"

def test_mixed_spaces():
    assert fix_spaces("Example 1  2   3") == "Example_1-2-3"

def test_empty_string():
    assert fix_spaces("") == ""

def test_string_with_only_spaces():
    assert fix_spaces("   ") == "-"

def test_special_characters():
    assert fix_spaces("Example!@#$%^&*()") == "Example!@#$%^&*()"

def test_consecutive_three_spaces_at_start():
    assert fix_spaces("   Example") == "-Example"

def test_consecutive_three_spaces_at_end():
    assert fix_spaces("Example   ") == "Example-"

def test_consecutive_three_spaces_in_middle():
    assert fix_spaces("Example   123") == "Example-123"

def test_mix_single_and_consecutive():
    assert fix_spaces("Example 1  2   3") == "Example_1-2-3"