
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
from your_module import fix_spaces  # Replace your_module

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_trailing_space():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_consecutive_spaces():
    assert fix_spaces("This  is   a    test") == "This-is-a-test"

def test_mixed_whitespace():
    assert fix_spaces("  Hello  World  ") == "-Hello-World-"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_leading_and_trailing_spaces():
    assert fix_spaces("  Test  ") == "-Test-"

def test_leading_multiple_spaces():
    assert fix_spaces("   Test") == "-Test"

def test_trailing_multiple_spaces():
    assert fix_spaces("Test   ") == "Test-"

def test_consecutive_spaces_in_middle():
    assert fix_spaces("Test   More Test") == "Test-More-Test"

def test_long_string_with_multiple_spaces():
    long_string = "This is a very long string with many spaces.   It has some consecutive spaces too.  And some more."
    expected_result = "This_is_a_very_long_string_with_many_spaces.-It_has_some_consecutive_spaces_too.-And_some_more."
    assert fix_spaces(long_string) == expected_result

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_mixed_whitespace():
    assert fix_spaces("Example\t 1 \n 2") == "Example_1-2"

def test_string_with_only_tabs():
    assert fix_spaces("\t\t") == "-"

def test_string_with_only_newlines():
    assert fix_spaces("\n\n") == "-"

def test_unicode_space():
    assert fix_spaces("Example\u00A01") == "Example_1" # Non-breaking space

def test_empty_string_with_whitespace():
    assert fix_spaces("   \t\n  ") == "-"