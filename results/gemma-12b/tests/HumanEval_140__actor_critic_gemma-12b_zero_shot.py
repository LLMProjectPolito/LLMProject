
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

@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("Example 1", "Example-1"),
        (" Example 2", "-Example-2"),
        (" Example   3", "-Example-3"),
        ("   Example", "-Example"),
        ("Example   ", "Example-"),
        ("  Hello  World  ", "-Hello-World-"),
    ],
)
def test_space_variations(input_string, expected_result):
    assert fix_spaces(input_string) == expected_result

def test_multiple_consecutive_spaces():
    assert fix_spaces("This  is   a    test") == "This-is-a-test"

def test_only_spaces():
    assert fix_spaces("   ") == "---"

def test_spaces_at_beginning_and_end():
    assert fix_spaces("  Test  ") == "-Test-"

def test_long_string_with_multiple_spaces():
    long_string = "This is a very long string with many spaces.   It has  multiple   consecutive   spaces."
    expected_result = "This-is-a-very-long-string-with-many-spaces.-It-has-multiple-consecutive-spaces."
    assert fix_spaces(long_string) == expected_result

# The following tests are removed as they are redundant or inconsistent
# def test_string_with_tabs():
#     assert fix_spaces("Example\t1") == "Example_1"
#
# def test_string_with_newlines():
#     assert fix_spaces("Example\n1") == "Example_1"
#
# def test_string_with_mixed_whitespace():
#     assert fix_spaces("Example\t 1 \n 2") == "Example_1_2"
#
# def test_string_with_only_tabs():
#     assert fix_spaces("\t\t") == "-"
#
# def test_string_with_only_newlines():
#     assert fix_spaces("\n\n") == "-"
#
# def test_string_with_tabs_and_spaces():
#     assert fix_spaces("Example \t 1") == "Example_1"

def test_unicode_whitespace():
    assert fix_spaces("Example\u20001") == "Example-1" # Example with unicode space