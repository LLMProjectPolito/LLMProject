import pytest
from your_module import fix_spaces  # Replace your_module
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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

    # Palindrome Tests
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

    def test_palindrome_mixed_case(self):
        assert is_palindrome("Racecar") == True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") == False #spaces are not removed

    # Get Max Tests
    def test_get_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_get_max_empty(self):
        assert get_max([]) == None

    def test_get_max_negative(self):
        assert get_max([-1, -2, -3]) == -1

    def test_get_max_mixed(self):
        assert get_max([-1, 2, -3, 4]) == 4