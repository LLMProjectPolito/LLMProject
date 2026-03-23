import pytest
from your_module import fix_spaces  # Replace your_module

class TestFixSpaces:

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_multiple_spaces(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_multiple_consecutive_spaces(self):
        assert fix_spaces("This  is   a    test") == "This-is-a-test"

    def test_mixed_spaces(self):
        assert fix_spaces("  Leading and   trailing spaces  ") == "-Leading_and--trailing_spaces-"

    def test_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_string_with_tabs(self):
        assert fix_spaces("Example\t1") == "Example_1"

    def test_string_with_newlines(self):
        assert fix_spaces("Example\n1") == "Example_1"

    def test_string_with_mixed_whitespace(self):
        assert fix_spaces("Example \t 1 \n 2") == "Example_1_2"

    def test_long_string_with_consecutive_spaces(self):
        long_string = "This is a very long string with many   consecutive   spaces."
        assert fix_spaces(long_string) == "This_is_a_very_long_string_with_many-consecutive-spaces."

    def test_string_with_special_characters(self):
        assert fix_spaces("!@#$%^&*()") == "!@#$%^&*()"

    def test_string_with_numbers(self):
        assert fix_spaces("123 456") == "123_456"