
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

@pytest.mark.parametrize("file_name, expected", [
    # Valid cases
    ("example.txt", "Yes"),
    ("Example.exe", "Yes"),
    ("myFile.dll", "Yes"),
    ("a.txt", "Yes"),
    ("A.exe", "Yes"),
    ("file1.txt", "Yes"),
    ("file12.txt", "Yes"),
    ("file123.txt", "Yes"),
    ("a1b2c3.dll", "Yes"),
    ("test_name.exe", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("a1b2c3d4.exe", "No"),
    ("1234a.dll", "No"), # Also fails start letter check
    
    # Invalid: Dot conditions (Exactly one dot)
    ("filename", "No"),        # No dot
    ("file.name.txt", "No"),   # Too many dots
    ("file..txt", "No"),       # Too many dots
    
    # Invalid: Substring before dot
    (".txt", "No"),            # Empty before dot
    ("1example.dll", "No"),    # Starts with digit
    ("_example.txt", "No"),    # Starts with underscore
    (" example.exe", "No"),    # Starts with space
    ("!file.txt", "No"),       # Starts with special char
    
    # Invalid: Substring after dot (Extension)
    ("file.pdf", "No"),        # Not in allowed list
    ("file.jpg", "No"),        # Not in allowed list
    ("file.txt1", "No"),       # Not in allowed list
    ("file.", "No"),           # Empty extension
    ("file.TXT", "No"),        # Case sensitivity check (usually strict)
    ("file.EXE", "No"),        # Case sensitivity check
    ("file.DLL", "No"),        # Case sensitivity check
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

def test_file_name_check_edge_cases():
    # Test with very long names but valid
    assert file_name_check("a" * 100 + ".txt") == "Yes"
    # Test with exactly 3 digits scattered
    assert file_name_check("a1b2c3.exe") == "Yes"
    # Test with 0 digits
    assert file_name_check("abc.dll") == "Yes"