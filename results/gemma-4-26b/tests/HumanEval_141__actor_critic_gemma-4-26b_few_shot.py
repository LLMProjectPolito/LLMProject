
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

def test_file_name_check_valid():
    """Tests valid file names that meet all criteria."""
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("test.exe") == 'Yes'
    assert file_name_check("my_file.dll") == 'Yes'
    assert file_name_check("A.txt") == 'Yes'  # Starts with uppercase letter
    assert file_name_check("a1b2c3.exe") == 'Yes'  # Exactly 3 digits
    assert file_name_check("abc.txt") == 'Yes'  # 0 digits

def test_file_name_check_invalid_digits():
    """Tests files with too many digits."""
    assert file_name_check("a1b2c3d.txt") == 'No'  # 4 digits
    assert file_name_check("1234.exe") == 'No'     # 4 digits
    assert file_name_check("abc1234.dll") == 'No'  # 4 digits

def test_file_name_check_invalid_dots():
    """Tests files with incorrect dot placement or count."""
    assert file_name_check("exampletxt") == 'No'      # No dot
    assert file_name_check("example.txt.exe") == 'No' # More than one dot
    assert file_name_check("example.") == 'No'        # No extension after dot
    assert file_name_check(".txt") == 'No'            # Empty substring before dot

def test_file_name_check_invalid_prefix():
    """Tests files where the prefix doesn't start with a letter or is empty."""
    assert file_name_check("1example.txt") == 'No'    # Starts with a digit
    assert file_name_check("_example.txt") == 'No'    # Starts with special char
    assert file_name_check(" example.txt") == 'No'    # Starts with a space
    assert file_name_check(".exe") == 'No'            # Empty prefix

def test_file_name_check_invalid_extension():
    """Tests files with unsupported extensions."""
    assert file_name_check("example.png") == 'No'     # Unsupported extension
    assert file_name_check("example.pdf") == 'No'     # Unsupported extension
    assert file_name_check("example.TXT") == 'No'     # Case sensitivity check (if strict)
    assert file_name_check("example.txt1") == 'No'    # Extension contains digits

@pytest.mark.parametrize("filename, expected", [
    ("valid.txt", "Yes"),
    ("v1a2b3.exe", "Yes"),
    ("v1a2b3c.exe", "No"),
    ("1abc.txt", "No"),
    ("abc.png", "No"),
    ("a.dll", "Yes"),
    ("..txt", "No"),
    ("abc.txt.exe", "No"),
])
def test_file_name_check_parameterized(filename, expected):
    """A parameterized version to cover multiple scenarios efficiently."""
    assert file_name_check(filename) == expected