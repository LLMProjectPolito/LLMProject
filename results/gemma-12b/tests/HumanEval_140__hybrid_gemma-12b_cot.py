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
    new_text = text.replace(" ", "_")
    while "__" in new_text:
        new_text = new_text.replace("__", "-")
    while "___" in new_text:
        new_text = new_text.replace("___", "-")
    return new_text

class TestFixSpaces:
    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_trailing_space(self):
        assert fix_spaces("Example 3 ") == "Example_3_"

    def test_multiple_spaces(self):
        assert fix_spaces("Example   4") == "Example-4"

    def test_consecutive_spaces(self):
        assert fix_spaces("Example    5") == "Example-5"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1   2") == "Example__1-2"

    def test_multiple_consecutive_spaces(self):
        assert fix_spaces("Example     6") == "Example-6"

    def test_string_with_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_string_with_more_than_three_consecutive_spaces(self):
        assert fix_spaces("Example    7") == "Example-7"

    def test_string_with_leading_and_trailing_spaces(self):
        assert fix_spaces("  Example 8  ") == "-Example_8-"

    def test_string_with_special_characters(self):
        assert fix_spaces("Example!@#$%^&*()") == "Example!@#$%^&_()*"

    def test_string_with_numbers_and_spaces(self):
        assert fix_spaces("1 2 3 4 5") == "1_2_3_4_5"

    def test_string_with_tabs_and_spaces(self):
        assert fix_spaces("Example\t1") == "Example_1"

    def test_long_string_with_consecutive_spaces(self):
        long_string = "This is a very long string with   multiple   consecutive   spaces."
        assert fix_spaces(long_string) == "This_is_a_very_long_string_with-multiple-consecutive-spaces."

    def test_consecutive_spaces_at_beginning(self):
        assert fix_spaces("   Example 4") == "-Example_4"

    def test_consecutive_spaces_at_end(self):
        assert fix_spaces("Example 5   ") == "Example_5-"

    def test_consecutive_spaces_in_middle(self):
        assert fix_spaces("Example   6  7") == "Example-6_7"

    def test_mixed_spaces2(self):
        assert fix_spaces("Example  8  9  10") == "Example-8_9-10"

    def test_only_spaces2(self):
        assert fix_spaces("   ") == "-"

    def test_multiple_consecutive_spaces2(self):
        assert fix_spaces("Example     11") == "Example-------11"

    def test_string_with_tabs2(self):
        assert fix_spaces("Example\t12") == "Example_12"

    def test_string_with_newlines(self):
        assert fix_spaces("Example\n13") == "Example_13"

    def test_string_with_mixed_whitespace(self):
        assert fix_spaces("Example \t 14\n15") == "Example_14-15"

    def test_long_string_with_consecutive_spaces2(self):
        long_string = "This is a very long string with   multiple    consecutive   spaces."
        expected = "This_is_a_very_long_string_with-multiple-------consecutive-spaces."
        assert fix_spaces(long_string) == expected

    def test_string_with_special_characters2(self):
        assert fix_spaces("Example!@#$%^&*()") == "Example!@#$%^&*()"

    def test_string_with_numbers2(self):
        assert fix_spaces("123 456 789") == "123_456_789"