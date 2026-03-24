
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
    return re.sub(r" +", "-", text.replace(" ", "_"))


### Tests (Pytest):
def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_consecutive():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "---"

def test_fix_spaces_more_than_two_spaces():
    assert fix_spaces("  Example   ") == "-Example-"

def test_fix_spaces_leading_trailing_spaces():
    assert fix_spaces("   Example   ") == "---Example---"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("Example  1  2") == "Example-1-2"