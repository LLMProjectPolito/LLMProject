
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
    import re
    return re.sub(r" {3,}", "-", text).replace(" ", "_")

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_and_trailing_spaces():
    assert fix_spaces(" Example ") == "_Example_"

def test_multiple_spaces():
    assert fix_spaces("Example 1 2 3") == "Example_1_2_3"

def test_more_than_two_consecutive_spaces():
    assert fix_spaces("Example   1") == "Example-1"

def test_empty_string():
    assert fix_spaces("") == ""

def test_mixed_single_and_multiple_spaces():
    assert fix_spaces("Example  1   2  3") == "Example__1-2__3"

def test_complex_string():
    assert fix_spaces("  This is a   test  with  many   spaces.  ") == "_This_is_a-test__with__many-spaces._"

def test_consecutive_spaces_at_beginning():
    assert fix_spaces("  abc") == "__abc"

def test_consecutive_spaces_at_end():
    assert fix_spaces("abc  ") == "abc__"

def test_multiple_space_groups():
    assert fix_spaces("abc   def") == "abc-def"

def test_tabs():
    assert fix_spaces("Example\t1") == "Example\t1"