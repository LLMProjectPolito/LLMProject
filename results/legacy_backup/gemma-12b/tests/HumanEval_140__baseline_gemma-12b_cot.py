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
            j = i
            while j < len(text) and text[j] == " ":
                count += 1
                j += 1
            if count > 2:
                result += "-"
                i = j
            else:
                result += "_"
                i = j
        else:
            result += text[i]
            i += 1
    return result

class TestFixSpaces:
    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_multiple_consecutive_spaces(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_multiple_spaces_and_text(self):
        assert fix_spaces("This is a  test") == "This_is_a-test"

    def test_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_leading_and_trailing_spaces(self):
        assert fix_spaces("  Example  ") == "-Example-"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1   2") == "Example-1__2"

    def test_long_string_with_consecutive_spaces(self):
        assert fix_spaces("This is a very long string with   many   consecutive spaces.") == "This_is_a_very_long_string_with-many-consecutive_spaces."

    def test_string_with_tabs_and_spaces(self):
        assert fix_spaces("Example\t1") == "Example_1"

    def test_string_with_newline_and_spaces(self):
        assert fix_spaces("Example\n1") == "Example_1"

    def test_string_with_special_characters_and_spaces(self):
        assert fix_spaces("!@#$%^&*() Example 1") == "_!@#$%^&*()_1"