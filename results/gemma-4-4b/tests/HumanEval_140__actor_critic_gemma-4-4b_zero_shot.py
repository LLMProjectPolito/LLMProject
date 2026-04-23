
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
        return ""  # Or raise TypeError, depending on desired behavior

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


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("Example", "Example"),
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        (" Example   3", "_Example-3"),
        ("", ""),  # Empty string
        ("   ", "---"),  # Only spaces
        ("a b c", "a_b_c"),  # Single spaces
        ("a   b", "a___b"),  # Multiple spaces between chars
        ("a  b  c", "a__b__c"),  # Multiple spaces around chars
        (" a b c ", "_a_b_c_"),  # Spaces at start and end
        ("  a   b  c   ", "___a___b___c___"),  # Lots of spaces
        ("123", "123"),  # No spaces
        ("a b c d", "a_b_c_d"), # no consecutive spaces
        ("a   b c", "a___b_c"), # spaces at the end
        ("a b   c", "a_b__c"), # spaces at the beginning and end
        ("  a  b  c  ", "___a___b___c___"),
    ],
)
def test_fix_spaces(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        (123, ""), #Non-string input
        (None, ""), #None input
        ([1,2,3], ""), #List input
        {"a":1}, #Dict input
    ],
)
def test_fix_spaces_non_string(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output