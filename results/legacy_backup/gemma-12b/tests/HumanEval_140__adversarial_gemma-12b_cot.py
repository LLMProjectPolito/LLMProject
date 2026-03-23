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
    i = 0
    while i < len(text):
        if text[i] == " ":
            count = 0
            while i < len(text) and text[i] == " ":
                count += 1
                i += 1
            if count > 2:
                result += "-"
            else:
                result += "_"
        else:
            result += text[i]
            i += 1
    return result

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_single_spaces():
    assert fix_spaces("Example 1 2 3") == "Example_1_2_3"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_trailing_space():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_two_consecutive_spaces():
    assert fix_spaces("Example  1") == "Example__1"

def test_three_consecutive_spaces():
    assert fix_spaces("Example   1") == "Example-1"

def test_more_than_three_consecutive_spaces():
    assert fix_spaces("Example    1") == "Example-1"

def test_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example__1-2"

def test_empty_string():
    assert fix_spaces("") == ""

def test_special_characters():
    assert fix_spaces("Example!@#$%^&*()") == "Example!@#$%^&*()"
    assert fix_spaces(" Example 1!") == "_Example_1!"

def test_numbers():
    assert fix_spaces("1 2 3") == "1_2_3"
    assert fix_spaces("1  2 3") == "1-2_3"

def test_consecutive_spaces_at_start():
    assert fix_spaces("   Example") == "-Example"

def test_consecutive_spaces_at_end():
    assert fix_spaces("Example   ") == "Example-"

def test_long_string_with_consecutive_spaces():
    assert fix_spaces("Example   1 2   3   4") == "Example-1_2-3_4"

def test_type_handling():
    with pytest.raises(TypeError):
        fix_spaces(123)