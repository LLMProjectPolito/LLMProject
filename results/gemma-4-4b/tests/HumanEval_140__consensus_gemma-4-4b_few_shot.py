
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
    text = text.replace(" ", "_")
    while "   " in text:
        text = text.replace("   ", "-")
    return text

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example ") == "Example_"

def test_multiple_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_and_trailing_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_only_spaces():
    assert fix_spaces("   ") == "__"

def test_mixed_spaces_and_other_chars():
    assert fix_spaces("a b c") == "a_b_c"

def test_spaces_at_beginning_and_end_with_other_chars():
    assert fix_spaces("  a b  c   ") == "__a_b__c--"

def test_complex_string():
    assert fix_spaces("This is a  test string   with   multiple   spaces.") == "This_is_a_test_string---with---multiple---spaces."

def test_string_with_special_characters():
    assert fix_spaces("Hello!  World?") == "Hello!_World?"

def test_string_with_numbers():
    assert fix_spaces("1 2  3") == "1_2--3"

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_long_string():
    long_string = "a" * 100 + " " * 50 + "b" * 100
    assert fix_spaces(long_string) == "a" * 100 + "_" * 50 + "b" * 100