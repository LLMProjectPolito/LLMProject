
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
    result = ""
    count = 0
    for char in text:
        if char == ' ':
            count += 1
        else:
            if count > 2:
                result += '-'
                count = 0
            result += char
    return result

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_single_space():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_consecutive_spaces():
    assert fix_spaces("Example 2") == "_Example_2"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("Example 3") == "_Example-3"

def test_fix_spaces_with_underscores():
    assert fix_spaces("Example 4") == "Example_4"

def test_fix_spaces_with_hyphens():
    assert fix_spaces("Example 5") == "Example-5"

def test_fix_spaces_with_numbers():
    assert fix_spaces("Example 6") == "Example_6"

def test_fix_spaces_with_special_characters():
    assert fix_spaces("Example 7") == "Example_7"

def test_fix_spaces_with_leading_and_trailing_spaces():
    assert fix_spaces("Example 8") == "Example_8"

def test_fix_spaces_with_multiple_underscores():
    assert fix_spaces("Example 9") == "Example_9"

def test_fix_spaces_with_multiple_hyphens():
    assert fix_spaces("Example 10") == "Example-10"

def test_fix_spaces_with_multiple_numbers():
    assert fix_spaces("Example 11") == "Example_11"

def test_fix_spaces_with_multiple_special_characters():
    assert fix_spaces("Example 12") == "Example_12"