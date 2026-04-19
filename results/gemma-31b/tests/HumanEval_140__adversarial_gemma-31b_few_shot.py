
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

def test_fix_spaces_examples():
    """Verify the examples provided in the docstring."""
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_boundary_two_spaces():
    """
    Test the boundary condition: 'more than 2 consecutive spaces'.
    Exactly 2 spaces should be replaced by two underscores, NOT a hyphen.
    """
    assert fix_spaces("Example  2") == "Example__2"
    assert fix_spaces("  ") == "__"

def test_fix_spaces_boundary_three_plus_spaces():
    """
    Test the boundary condition: 3 or more spaces should be replaced by a single hyphen.
    """
    assert fix_spaces("Example   3") == "Example-3"
    assert fix_spaces("Example    4") == "Example-4"
    assert fix_spaces("Example     5") == "Example-5"
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed_sequences():
    """Test strings containing a mix of single, double, and triple+ spaces."""
    # 1 space -> _, 2 spaces -> __, 3 spaces -> -
    assert fix_spaces("a b  c   d    e") == "a_b__c-d-e"
    assert fix_spaces("  a   b  c ") == "__a-b__c_"

def test_fix_spaces_edges():
    """Test empty strings and strings with no spaces."""
    assert fix_spaces("") == ""
    assert fix_spaces("NoSpacesHere") == "NoSpacesHere"
    assert fix_spaces("12345") == "12345"

def test_fix_spaces_positioning():
    """Test spaces at the very beginning and very end of the string."""
    assert fix_spaces(" leading") == "_leading"
    assert fix_spaces("trailing ") == "trailing_"
    assert fix_spaces("   both   ") == "-both-"
    assert fix_spaces("  both  ") == "__both__"

def test_fix_spaces_non_space_whitespace():
    """
    Ensure that only actual space characters ' ' are replaced, 
    not tabs or newlines (unless the requirement defines 'spaces' as all whitespace).
    """
    assert fix_spaces("Tab\tTest") == "Tab\tTest"
    assert fix_spaces("Newline\nTest") == "Newline\nTest"