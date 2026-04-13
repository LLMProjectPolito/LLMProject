
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
    count = 0
    for char in text:
        if char == " ":
            count += 1
            if count <= 2:
                result += "_"
            else:
                result += "-"
        else:
            result += char
            count = 0
    return result

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "--"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("Hello  World") == "Hello__World"

def test_fix_spaces_long_consecutive_spaces():
    assert fix_spaces("This   has    many   spaces") == "This---has----many---spaces"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces("Some text   ") == "Some_text--"

def test_fix_spaces_multiple_consecutive_and_trailing():
    assert fix_spaces("  Multiple   spaces   at   the   end  ") == "_Multiple---spaces---at---the---end"

def test_fix_spaces_all_spaces():
    assert fix_spaces("   ") == "---"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  a  b  c") == "_a_b_c"

def test_fix_spaces_long_consecutive_spaces():
    assert fix_spaces("This has   many   spaces") == "This has ---many---spaces"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces("Hello   ") == "Hello---"

def test_fix_spaces_spaces_at_start_and_end():
    assert fix_spaces("  Test  ") == "_Test--"