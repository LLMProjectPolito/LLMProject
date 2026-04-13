
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

def test_fix_spaces_provided_examples():
    """Tests the examples explicitly provided in the docstring."""
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_no_spaces():
    """Tests strings that contain no spaces at all."""
    assert fix_spaces("") == ""
    assert fix_spaces("HelloWorld") == "HelloWorld"
    assert fix_spaces("12345") == "12345"

def test_fix_spaces_single_space():
    """Tests that single spaces are always replaced by underscores."""
    assert fix_spaces("a b") == "a_b"
    assert fix_spaces(" a") == "_a"
    assert fix_spaces("a ") == "a_"
    assert fix_spaces(" ") == "_"

def test_fix_spaces_double_space():
    """
    Tests the boundary condition of exactly 2 spaces.
    According to the rules: 'more than 2' triggers '-', 
    so 2 spaces should be treated as individual spaces -> '__'.
    """
    assert fix_spaces("a  b") == "a__b"
    assert fix_spaces("  ") == "__"

def test_fix_spaces_triple_plus_space():
    """Tests that 3 or more consecutive spaces are replaced by a single hyphen."""
    assert fix_spaces("a   b") == "a-b"        # Exactly 3
    assert fix_spaces("a    b") == "a-b"       # 4 spaces
    assert fix_spaces("a          b") == "a-b" # Many spaces
    assert fix_spaces("   ") == "-"            # Only 3 spaces

def test_fix_spaces_mixed_sequences():
    """Tests complex strings with mixed counts of consecutive spaces."""
    # 1 space (_), 2 spaces (__), 3 spaces (-)
    assert fix_spaces("a b  c   d") == "a_b__c-d"
    # 4 spaces (-), 1 space (_), 2 spaces (__)
    assert fix_spaces("a    b c  d") == "a-b_c__d"
    # Leading and trailing mixed
    assert fix_spaces("   hello  world  ") == "-hello__world__"

def test_fix_spaces_non_space_whitespace():
    """
    Ensures that only actual space characters ' ' are replaced, 
    not tabs or newlines (unless the requirement implies all whitespace).
    """
    assert fix_spaces("a\tb") == "a\tb"
    assert fix_spaces("a\nb") == "a\nb"