
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

def test_file_name_valid_basic():
    """Tests standard valid file names and case sensitivity of the prefix."""
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("document.exe") == 'Yes'
    assert file_name_check("library.dll") == 'Yes'
    assert file_name_check("MyFile.txt") == 'Yes'
    assert file_name_check("FILE.txt") == 'Yes'  # Confirms prefix case-insensitivity

def test_file_name_digit_count():
    """Tests the condition: no more than three digits total in the entire name."""
    assert file_name_check("file123.txt") == 'Yes'  # Exactly 3 digits
    assert file_name_check("file1.txt") == 'Yes'    # Fewer than 3 digits
    assert file_name_check("file1234.txt") == 'No'  # 4 digits
    assert file_name_check("12345.exe") == 'No'     # More than 3 digits
    assert file_name_check("a1b2c3.exe") == 'Yes'   # Max digits spread out

def test_file_name_dot_count():
    """Tests the condition: exactly one dot."""
    assert file_name_check("exampletxt") == 'No'       # No dot
    assert file_name_check("example.txt.bak") == 'No'  # More than one dot

def test_file_name_prefix_start():
    """Tests that the prefix must not be empty and must start with a Latin letter."""
    assert file_name_check(".txt") == 'No'          # Empty prefix
    assert file_name_check("1example.dll") == 'No'  # Starts with digit
    assert file_name_check("_example.txt") == 'No'  # Starts with special character
    assert file_name_check(" a.txt") == 'No'        # Starts with space
    assert file_name_check("éxample.txt") == 'No'   # Starts with non-Latin Unicode character

def test_file_name_prefix_internal():
    """Tests that special characters/spaces are allowed INSIDE the prefix."""
    assert file_name_check("my file.txt") == 'Yes'    # Space inside
    assert file_name_check("file_name.txt") == 'Yes'  # Underscore inside
    assert file_name_check("file-1.txt") == 'Yes'     # Hyphen and digit inside
    assert file_name_check("exampleé.txt") == 'Yes'   # Unicode inside (starts with Latin 'e')

def test_file_name_extension():
    """Tests the substring after the dot against the whitelist ['txt', 'exe', 'dll']."""
    # Whitelist validation
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("example.jpg") == 'No'   # 3-letter extension NOT in whitelist
    assert file_name_check("example.pdf") == 'No'   # Invalid extension
    
    # Extension content and formatting
    assert file_name_check("example.txt1") == 'No'  # Not in whitelist (contains digit)
    assert file_name_check("example.TXT") == 'No'   # Must be lowercase per whitelist
    assert file_name_check("example.") == 'No'      # Empty extension
    assert file_name_check("example.txt ") == 'No'  # Trailing whitespace

def test_file_name_input_types():
    """Tests that non-string inputs are handled gracefully."""
    assert file_name_check(None) == 'No'
    assert file_name_check(123) == 'No'
    assert file_name_check(["example.txt"]) == 'No'

def test_file_name_edge_cases():
    """Tests various boundary conditions."""
    assert file_name_check("") == 'No'              # Empty string
    assert file_name_check(".") == 'No'             # Only a dot
    assert file_name_check("a.txt") == 'Yes'        # Minimum valid length