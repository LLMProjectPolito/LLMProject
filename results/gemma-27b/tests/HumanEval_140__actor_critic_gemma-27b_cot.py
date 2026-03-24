
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

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_trailing_space():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_leading_multiple_spaces():
    assert fix_spaces("   Example 3") == "-Example_3"

def test_trailing_multiple_spaces():
    assert fix_spaces("Example 3   ") == "Example_3-"

def test_multiple_spaces_mixed():
    assert fix_spaces("  Example   4  ") == "_Example-4-"

def test_empty_string():
    assert fix_spaces("") == ""

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_spaces_within_word():
    assert fix_spaces("Exam ple") == "Exam_ple"

def test_long_string():
    long_string = "This is a very long string with   many   spaces."
    assert fix_spaces(long_string) == "This_is_a_very_long_string_with-many-spaces."

def test_consecutive_spaces():
    assert fix_spaces("Example  1") == "Example_1" #Corrected to align with function logic

def test_multiple_consecutive_spaces():
    assert fix_spaces("Example   1") == "Example-1"