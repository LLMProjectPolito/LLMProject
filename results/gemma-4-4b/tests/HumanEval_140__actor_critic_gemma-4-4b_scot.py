
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
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if len(text) == 0:
        return ""

    result = ""
    count = 0
    for char in text:
        if char == ' ':
            count += 1
            if count > 2:
                result += "-" * count
                count = 0
            else:
                result += "_"
        else:
            result += char
            count = 0
    
    if count > 0:
        result += "_" * count

    return result


def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example ") == "Example_"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_leading_trailing_spaces():
    assert fix_spaces("  Test  ") == "__Test__"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "__"

def test_fix_spaces_mixed_spaces_and_non_spaces():
    assert fix_spaces("This is a test") == "This_is_a_test"

def test_fix_spaces_long_string_with_many_spaces():
    long_string = " " * 50 + "Test" + " " * 50
    expected_result = "__" * 50 + "Test" + "__" * 50
    assert fix_spaces(long_string) == expected_result