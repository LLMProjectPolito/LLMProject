
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
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
            if space_count <= 2:
                result += "_"
            else:
                result += "-"
        else:
            result += char
            space_count = 0
    return result

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_no_leading_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "--"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("This  has   many   spaces") == "This---has---many---spaces"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("A  B   C") == "A__B--C"

def test_fix_spaces_long_string():
    assert fix_spaces("This is a very long string with many spaces.") == "This_is_a_very_long_string_with_many_spaces."

def test_fix_spaces_with_special_characters():
    assert fix_spaces("Hello!  World!") == "Hello!__World!"

def test_fix_spaces_with_numbers():
    assert fix_spaces("1 2 3 4") == "1_2_3_4"

def test_fix_spaces_with_mixed_content():
    assert fix_spaces("A1 B2 C3") == "A1_B2_C3"