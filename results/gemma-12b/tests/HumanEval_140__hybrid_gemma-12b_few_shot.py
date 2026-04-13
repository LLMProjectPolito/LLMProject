
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
from your_module import fix_spaces  # Replace your_module
from your_module import is_palindrome, get_max  # Assuming these are in your_module

class TestFixSpaces:
    """
    A comprehensive test suite for the fix_spaces function.
    """

    def test_no_spaces(self):
        """Test case: String with no spaces."""
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        """Test case: String with a single space."""
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        """Test case: String with a leading space."""
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_multiple_consecutive_spaces(self):
        """Test case: String with multiple consecutive spaces."""
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_multiple_spaces_mixed(self):
        """Test case: String with a mix of single and multiple spaces."""
        assert fix_spaces("Example  1   2") == "Example__1-2"

    def test_all_spaces(self):
        """Test case: String consisting only of spaces."""
        assert fix_spaces("   ") == "-"

    def test_empty_string(self):
        """Test case: Empty string."""
        assert fix_spaces("") == ""

    def test_string_with_tabs(self):
        """Test case: String with tabs (should be treated as spaces)."""
        assert fix_spaces("Example\t1") == "Example_1"

    def test_string_with_newlines(self):
        """Test case: String with newlines (should be treated as spaces)."""
        assert fix_spaces("Example\n1") == "Example_1"

    def test_string_with_mixed_whitespace(self):
        """Test case: String with a mix of spaces, tabs, and newlines."""
        assert fix_spaces("Example \t 1\n2") == "Example_1_2"

    def test_long_string_with_consecutive_spaces(self):
        """Test case: A longer string with multiple consecutive spaces."""
        long_string = "This is a  very   long string with     many spaces."
        expected_result = "This_is_a-very___long_string_with-----many_spaces."
        assert fix_spaces(long_string) == expected_result

    def test_string_with_special_characters(self):
        """Test case: String with special characters and spaces."""
        assert fix_spaces("!@# Example $ %^") == "!@#_Example_$_%^"

    @pytest.mark.parametrize(
        "input_string, expected_output",
        [
            ("abc def", "abc_def"),
            ("abc   def", "abc-def"),
            ("abc     def", "abc-def"),
            ("abc  def  ghi", "abc__def_ghi"),
            ("abc  def  ghi jkl", "abc__def_ghi_jkl"),
        ],
    )
    def test_parametrized_cases(self, input_string, expected_output):
        """Test cases using pytest.mark.parametrize for various inputs."""
        assert fix_spaces(input_string) == expected_output


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False  # Case sensitive

def test_is_palindrome_with_spaces():
    assert is_palindrome("A man, a plan, a canal: Panama") == False # Spaces are not ignored

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_duplicates():
    assert get_max([5, 5, 5]) == 5