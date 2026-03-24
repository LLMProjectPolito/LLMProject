
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

def test_two_consecutive_spaces():
    assert fix_spaces("Example  1") == "Example__1"

def test_three_or_more_consecutive_spaces():
    assert fix_spaces("Example   1") == "Example-1"

def test_mixed_spaces():
    assert fix_spaces("Example  1   2  3") == "Example__1-2__3"

def test_empty_string():
    assert fix_spaces("") == ""

@pytest.mark.parametrize("input_string, expected_output", [
    ("   ", "-"),
    (" " * 10, "-"),
    (" " * 5, "-"),
    ("  ", "__"), # Added test case for exactly two spaces
])
def test_multiple_spaces(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output

def test_realistic_spaces():
    assert fix_spaces("  abc 123   def  ") == "_abc_123-def__"

def test_consecutive_spaces_replaced_first():
    assert fix_spaces("   abc") == "-abc"

def test_complex_string():
    assert fix_spaces("This is a test") == "This_is_a_test"
    assert fix_spaces("string with multiple spaces.") == "string_with_multiple_spaces."
    assert fix_spaces("  string with   multiple   spaces.  ") == "_string_with-multiple-spaces._"

def test_edge_case_tabs():
    assert fix_spaces("abc\tdef") == "abc\tdef" # Tabs are not handled

def test_order_of_operations_nuance():
    assert fix_spaces("   1 2") == "-1_2" # Tests the order of replacement