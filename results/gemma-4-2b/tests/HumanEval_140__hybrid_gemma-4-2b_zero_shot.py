
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
            if count > 2:
                result += "-"
                count = 0
            else:
                result += "_"
        else:
            result += char
    return result


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Example", "Example"),
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        (" Example   3", "_Example-3"),
        ("  Hello  World  ", "_Hello-World_"),
        ("This is a test", "This_is_a_test"),
        ("  ", "_"),
        ("", ""),
        ("   ", "_"),
        ("   a   b   c", "_a_-b_-c"),
        ("   a   b   c   d", "_a_-b_-c_-d"),
        ("a b c", "a_b_c"),
        ("   a   b   c   d   e   f   ", "_a_-b_-c_-d_-e_-f_"),
        ("   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   ", "_a_-b_-c_-d_-e_-f_-g_-h_-i_-j_-k_-l_-m_-n_-o_-p_"),
        ("123 456 789", "123_456_789"),
        (" ", " "),
        ("  a   ", "_a_"),
    ],
)
def test_fix_spaces(input_text, expected_output):
    assert fix_spaces(input_text) == expected_output

@pytest.mark.insensitive
def test_fix_spaces_insensitive():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

@pytest.mark.parametrize(
    "input_text",
    [
        "  a   b   c   d   e   f   ",
        "   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   ",
        "123 456 789",
        " ",
        "",
        "   a   b   c   d   e   f   ",
    ],
)
def test_fix_spaces_edge_cases(input_text):
    assert fix_spaces(input_text) == input_text if input_text == "" else fix_spaces(input_text)
    assert fix_spaces(" ") == " "
    assert fix_spaces("") == ""
    assert fix_spaces("  a   b   c   d   e   f   ") == "_a_b_c_d_e_f_"
    assert fix_spaces("123 456 789") == "123_456_789"

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example ") == "_Example"

def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_consecutive_spaces():
    assert fix_spaces("  Example  ") == "_Example--"

def test_mixed_spaces_and_other_chars():
    assert fix_spaces("Example 123  test") == "Example_123-test"

def test_leading_and_trailing_spaces():
    assert fix_spaces("   Example   ") == "_Example--"

def test_only_spaces():
    assert fix_spaces("   ") == "---"

def test_spaces_at_beginning_and_end():
    assert fix_spaces("  ") == "__"

def test_complex_string():
    assert fix_spaces("This is a string with  multiple   spaces.") == "This_is_a_string_with--multiple--spaces."

def test_spaces_mixed_with_punctuation():
    assert fix_spaces("Hello,   world!") == "Hello,_world!"

def test_spaces_with_numbers():
    assert fix_spaces("Number 1 2 3") == "Number_1_2_3"

def test_spaces_with_special_characters():
    assert fix_spaces("Example!  @#$") == "Example!_@#$"

def test_long_string():
    long_string = "This is a very long string with many spaces.   "
    assert fix_spaces(long_string) == "This_is_a_very_long_string_with--many--spaces."

def test_string_with_only_spaces_and_punctuation():
    assert fix_spaces("   !@#$%^&*()_+=-`~[]\{}|;':\",./<>?") == "__!@#$%^&*()_+=-`~[]\{}|;':\",./<>?"