
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

import pytest
from your_module import file_name_check  # Replace your_module

class TestFileNameCheck:
    """
    Test suite for the file_name_check function.
    """

    def test_valid_file_name(self):
        """Tests with valid file names."""
        assert file_name_check("example.txt") == "Yes"
        assert file_name_check("document.dll") == "Yes"
        assert file_name_check("my_program.exe") == "Yes"
        assert file_name_check("a.txt") == "Yes"
        assert file_name_check("A.TXT") == "Yes"
        assert file_name_check("long_file_name.txt") == "Yes"
        assert file_name_check("file12.txt") == "Yes"
        assert file_name_check("file123.txt") == "Yes"
        assert file_name_check("document.pdf") == "No"
        assert file_name_check("my_file.exe") == "Yes"
        assert file_name_check("another.dll") == "Yes"
        assert file_name_check("file1.txt") == "Yes"
        assert file_name_check("file0.txt") == "Yes"
        assert file_name_check("file00.txt") == "Yes"
        assert file_name_check("file000.txt") == "Yes"
        assert file_name_check("file0000.txt") == "No"  # More than 3 digits

    def test_invalid_file_name_no_dot(self):
        """Tests with file names missing a dot."""
        assert file_name_check("exampletxt") == "No"
        assert file_name_check("example") == "No"
        assert file_name_check("example.tar.gz") == "No"
        assert file_name_check("example.txt.bak") == "No"

    def test_invalid_file_name_empty_before_dot(self):
        """Tests with file names where the part before the dot is empty."""
        assert file_name_check(".txt") == "No"
        assert file_name_check(".exe") == "No"
        assert file_name_check(".dll") == "No"

    def test_invalid_file_name_not_letter_before_dot(self):
        """Tests with file names where the part before the dot doesn't start with a letter."""
        assert file_name_check("1example.txt") == "No"
        assert file_name_check("_example.txt") == "No"
        assert file_name_check("-example.txt") == "No"
        assert file_name_check(" example.txt") == "No"

    def test_invalid_file_name_invalid_extension(self):
        """Tests with file names with invalid extensions."""
        assert file_name_check("example.pdf") == "No"
        assert file_name_check("example.jpg") == "No"
        assert file_name_check("example.zip") == "No"
        assert file_name_check("example.abc") == "No"

    def test_invalid_file_name_too_many_digits(self):
        """Tests with file names containing too many digits."""
        assert file_name_check("1234example.txt") == "No"
        assert file_name_check("1234.txt") == "No"
        assert file_name_check("12345.txt") == "No"

    def test_edge_cases(self):
        """Tests with edge cases and boundary conditions."""
        assert file_name_check("a000.txt") == "No"
        assert file_name_check("a1234.txt") == "No"
        assert file_name_check("a.txt") == "Yes"
        assert file_name_check("A.TXT") == "Yes"
        assert file_name_check("a.exe") == "Yes"
        assert file_name_check("a.dll") == "Yes"
        assert file_name_check("0.txt") == "No"
        assert file_name_check("000.txt") == "Yes"
        assert file_name_check("0000.txt") == "No"

    def test_empty_file_name(self):
        """Tests with an empty file name."""
        assert file_name_check("") == "No"

    def test_file_name_with_leading_trailing_spaces(self):
        """Tests with file names containing leading/trailing spaces."""
        assert file_name_check("  example.txt") == "No"
        assert file_name_check("example.txt  ") == "No"
        assert file_name_check("  example.txt  ") == "No"

    def test_file_name_with_special_characters(self):
        """Tests with file names containing special characters."""
        assert file_name_check("example!.txt") == "No"
        assert file_name_check("example#.txt") == "No"
        assert file_name_check("example$.txt") == "No"
        assert file_name_check("example#.exe") == "No"

    def test_string_with_only_dot(self):
        """Tests with a string containing only a dot."""
        assert file_name_check(".") == "No"

    def test_invalid_file_name_extension_case(self):
        """Tests with file names with incorrect extension case."""
        assert file_name_check("example.TXT") == "No"
        assert file_name_check("example.EXE") == "No"
        assert file_name_check("example.DLL") == "No"