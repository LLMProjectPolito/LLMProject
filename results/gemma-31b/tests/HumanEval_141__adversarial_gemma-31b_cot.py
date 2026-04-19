
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
    # --- Valid Cases ---
    ("example.txt", "Yes"),
    ("example.exe", "Yes"),
    ("example.dll", "Yes"),
    ("A.txt", "Yes"),           # Minimal valid name
    ("a1.txt", "Yes"),          # One digit
    ("a12.txt", "Yes"),         # Two digits
    ("a123.txt", "Yes"),        # Three digits (boundary)
    ("File123.exe", "Yes"),     # Three digits, uppercase start
    ("MyFile_1.dll", "Yes"),    # Underscore and digit
    ("a.txt", "Yes"),           # Minimal valid
    
    # --- Invalid: Digit Count ---
    ("a1234.txt", "No"),        # Four digits (too many)
    ("a12345.exe", "No"),       # Five digits
    ("1234.dll", "No"),         # Four digits, starts with digit
    ("a1b2c3d4.txt", "No"),     # Scattered digits exceeding 3
    
    # --- Invalid: Dot Count ---
    ("exampletxt", "No"),       # Zero dots
    ("example.txt.txt", "No"),  # Two dots
    ("example..txt", "No"),     # Two dots (consecutive)
    ("...", "No"),              # Multiple dots
    
    # --- Invalid: Substring Before Dot ---
    (".txt", "No"),             # Empty before dot
    ("1example.dll", "No"),     # Starts with digit
    ("2.txt", "No"),            # Starts with digit
    ("_example.txt", "No"),     # Starts with non-latin character
    ("!example.exe", "No"),     # Starts with non-latin character
    (" example.txt", "No"),     # Starts with space
    
    # --- Invalid: Substring After Dot ---
    ("example.pdf", "No"),      # Unsupported extension
    ("example.jpg", "No"),      # Unsupported extension
    ("example.tx", "No"),       # Too short
    ("example.txts", "No"),     # Too long
    ("example.TXT", "No"),      # Case sensitivity check (should be lowercase)
    ("example.EXE", "No"),      # Case sensitivity check
    ("example.DLL", "No"),      # Case sensitivity check
    ("example.", "No"),         # Empty after dot
    
    # --- Edge Cases ---
    ("", "No"),                 # Empty string
    (" ", "No"),                # Single space
    ("a.txt ", "No"),           # Trailing space
    (" a.txt", "No"),           # Leading space
    ("a.txt\n", "No"),          # Newline character
    ("a.txt\t", "No"),          # Tab character
    ("a.txt1", "No"),           # Extension contains digit
])
def test_file_name_check(file_name, expected):
    """
    Test the file_name_check function against a variety of valid and invalid inputs
    to ensure all constraints are strictly enforced.
    """
    assert file_name_check(file_name) == expected