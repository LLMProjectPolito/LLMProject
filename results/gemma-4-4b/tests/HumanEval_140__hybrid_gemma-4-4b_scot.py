
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
        return text
    
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

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("Example", "Example"),
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        (" Example   3", "_Example-3"),
        ("", ""),
        ("   ", "---"),
        ("a b c", "a_b_c"),
        ("a   b", "a---b"),
        ("a    b c", "a----b_c"),
        ("  a  b  c  ", "__a__b__c__"),
        (" a  b c  ", "_a__b_c_"),
        ("123", "123"),
        ("  123  ", "__123__"),
    ],
)
def test_fix_spaces(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        (123, TypeError),
    ],
)
def test_fix_spaces_type_error(input_string, expected_type):
    with pytest.raises(TypeError):
        fix_spaces(input_string)