
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

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("abc123") == "abc123"

def test_fix_spaces_single_spaces():
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Hello World ") == "_Hello_World_"

def test_fix_spaces_two_consecutive_spaces():
    # Rule: "more than 2" means 3 or more. 2 spaces should become underscores.
    assert fix_spaces("a  b") == "a__b"
    assert fix_spaces("  start") == "__start"
    assert fix_spaces("end  ") == "end__"

def test_fix_spaces_more_than_two_consecutive_spaces():
    # Rule: 3 or more consecutive spaces become a single hyphen.
    assert fix_spaces("Example   3") == "Example-3"
    assert fix_spaces("a    b") == "a-b"
    assert fix_spaces("   triple") == "-triple"
    assert fix_spaces("quadruple    ") == "quadruple-"

def test_fix_spaces_mixed_consecutive_counts():
    # Mix of 1, 2, and 3+ spaces
    assert fix_spaces("a b  c   d") == "a_b__c-d"
    assert fix_spaces("  a b   c ") == "__a_b-c_"

def test_fix_spaces_empty_and_whitespace_only():
    assert fix_spaces("") == ""
    assert fix_spaces(" ") == "_"
    assert fix_spaces("  ") == "__"
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"

@pytest.mark.parametrize("input_str, expected", [
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    ("Multiple   spaces  and single space", "Multiple-spaces__and_single_space"),
])
def test_fix_spaces_parametrized(input_str, expected):
    assert fix_spaces(input_str) == expected