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
        if text[i] == ' ':
            if i + 2 < len(text) and text[i+1] == ' ' and text[i+2] == ' ':
                result += '-'
                i += 3
            else:
                result += '_'
                i += 1
        else:
            result += text[i]
            i += 1
    return result

class TestFixSpaces:
    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_double_spaces(self):
        assert fix_spaces("Example  1") == "Example__1"

    def test_triple_spaces(self):
        assert fix_spaces("Example   1") == "Example-1"

    def test_multiple_triple_spaces(self):
        assert fix_spaces("Example   1   2") == "Example-1-2"

    def test_leading_space(self):
        assert fix_spaces(" Example") == "_Example"

    def test_trailing_space(self):
        assert fix_spaces("Example ") == "Example_"

    def test_leading_and_trailing_spaces(self):
        assert fix_spaces(" Example ") == "_Example_"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1   2") == "Example__1-2"

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_string_with_other_characters(self):
        assert fix_spaces("Example! 1?") == "Example!_1?"

    def test_long_string(self):
        assert fix_spaces("This is a long   string with  multiple   spaces.") == "This_is_a_long-string_with__multiple-spaces."