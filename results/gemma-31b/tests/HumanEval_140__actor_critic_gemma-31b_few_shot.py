
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
    """Tests strings that contain no spaces at all."""
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("") == ""
    assert fix_spaces("Python123") == "Python123"

def test_fix_spaces_single_spaces():
    """Tests strings with single spaces (should be replaced by underscores)."""
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces("Example 2 ") == "Example_2_"
    assert fix_spaces("a b c") == "a_b_c"
    assert fix_spaces(" ") == "_"

def test_fix_spaces_two_spaces():
    """
    Tests strings with exactly 2 consecutive spaces.
    According to the rule 'more than 2', 2 spaces should still be underscores.
    """
    assert fix_spaces("Example  2") == "Example__2"
    assert fix_spaces("  Example") == "__Example"
    assert fix_spaces("  ") == "__"

def test_fix_spaces_more_than_two_spaces():
    """Tests strings with 3 or more consecutive spaces (should be replaced by a single hyphen)."""
    assert fix_spaces("Example   3") == "Example-3"
    assert fix_spaces("Example    4") == "Example-4"
    assert fix_spaces("Example     5") == "Example-5"
    assert fix_spaces("   ") == "-"
    assert fix_spaces(" " * 10) == "-"

def test_fix_spaces_mixed():
    """Tests strings containing a mix of single, double, and triple+ spaces."""
    # 1 space -> _, 2 spaces -> __, 3+ spaces -> -
    assert fix_spaces(" a  b   c    d ") == "_a__b-c-d_"
    assert fix_spaces("Hello   World  Test") == "Hello-World__Test"

def test_fix_spaces_other_whitespace():
    """
    Tests other whitespace characters (tabs, newlines, carriage returns).
    Verifies that mixed whitespace follows the same length rules as standard spaces.
    """
    # Length 1: should be _
    assert fix_spaces("Tab\tTest") == "Tab_Test"
    assert fix_spaces("Newline\nTest") == "Newline_Test"
    assert fix_spaces("Return\rTest") == "Return_Test"
    
    # Length 2: should be __
    assert fix_spaces("Mixed\t Test") == "Mixed__Test"
    assert fix_spaces("Mixed \nTest") == "Mixed__Test"
    assert fix_spaces("Mixed\r\tTest") == "Mixed__Test"
    
    # Length 3+: should be -
    assert fix_spaces("Mixed\t \nTest") == "Mixed-Test"
    assert fix_spaces("Mixed\r\n Test") == "Mixed-Test"

def test_fix_spaces_unicode_whitespace():
    """Tests non-breaking spaces and other Unicode whitespace characters."""
    # \u00A0 is a non-breaking space
    assert fix_spaces("Unicode\u00A0Space") == "Unicode_Space"
    assert fix_spaces("Unicode\u00A0\u00A0Space") == "Unicode__Space"
    assert fix_spaces("Unicode\u00A0\u00A0\u00A0Space") == "Unicode-Space"
    
    # \u2003 is an em space
    assert fix_spaces("Em\u2003Space") == "Em_Space"
    assert fix_spaces("Em\u2003\u2003\u2003Space") == "Em-Space"

def test_fix_spaces_invalid_types():
    """Tests that the function handles invalid input types gracefully by raising a TypeError."""
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces(123)
    with pytest.raises(TypeError):
        fix_spaces(["Example", "String"])