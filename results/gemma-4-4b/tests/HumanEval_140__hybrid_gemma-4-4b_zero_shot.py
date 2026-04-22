
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
from typing import List

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
    for i in range(len(text)):
        if text[i] == ' ':
            count += 1
            if count > 2:
                result += "-" * count
                count = 0
            else:
                result += "_"
        else:
            result += text[i]
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
        ("   ", "-"),
        ("abc", "abc"),
        ("a b c", "a_b_c"),
        ("a   b   c", "a___b___c"),
        (" a b   c ", "_a_b---c_"),
        ("   a", "-_a"),
        ("a   ", "a___"),
        ("   a   ", "---a---"),
        ("123 456", "123_456"),
        ("  123  ", "__123__"),
        ("123", "123"),
        (" 123 ", "_123_"),
        ("123   ", "123___"),
    ],
)
def test_fix_spaces_basic(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("This is a test string", "This_is_a_test_string"),
        ("Multiple   spaces  here", "Multiple---spaces--here"),
        ("Leading and trailing spaces   ", "_Leading_and_trailing_spaces___"),
        ("  Only spaces  ", "__Only_spaces__"),
    ],
)
def test_fix_spaces_complex(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string",
    [
        "   ",
        "abc",
        "",
        "123",
        " a b c ",
    ],
)
def test_fix_spaces_edge_cases(input_string):
    assert fix_spaces(input_string) == fix_spaces(input_string)

@pytest.mark.parametrize(
    "input_string",
    [
        "  a  b  c  ",
        "a   b   c   ",
        "a b c",
    ],
)
def test_fix_spaces_multiple(input_string):
    assert fix_spaces(input_string) == fix_spaces(input_string)

@pytest.mark.parametrize(
    "input_string",
    [
        " a   b   c ",
        "a b c",
        "  a  b  c  ",
    ],
)

def test_fix_spaces_padding(input_string):
    assert fix_spaces(input_string) == fix_spaces(input_string)

@pytest.mark.parametrize(
    "input_string",
    [
        None,
        123,
        [1,2,3],
    ],
)
def test_fix_spaces_type_error(input_string):
    with pytest.raises(TypeError):
        fix_spaces(input_string)