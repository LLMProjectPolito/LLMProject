
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
    """
    # Condition: Exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    parts = file_name.split('.')
    prefix = parts[0]
    extension = parts[1]
    
    # Condition: Not more than three digits
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    # Condition: Prefix not empty and starts with a latin letter
    if not prefix or not prefix[0].isalpha():
        return 'No'
    
    # Condition: Extension must be one of ['txt', 'exe', 'dll']
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

@pytest.mark.parametrize("file_name, expected", [
    # --- Valid Cases ---
    ("example.txt", "Yes"),
    ("a.exe", "Yes"),
    ("A.dll", "Yes"),
    ("file123.txt", "Yes"),      # Exactly 3 digits
    ("abc1.exe", "Yes"),         # 1 digit
    ("z.dll", "Yes"),            # Single letter prefix
    ("TestFile.txt", "Yes"),     # Uppercase prefix
    ("a1b2c3.exe", "Yes"),       # 3 digits scattered
    
    # --- Invalid: Digit Count ---
    ("a1234.txt", "No"),         # 4 digits
    ("1234.txt", "No"),          # 4 digits (starts with digit)
    ("a1b2c3d4.exe", "No"),      # 4 digits
    ("abc1234.dll", "No"),       # 4 digits
    
    # --- Invalid: Dot Conditions ---
    ("exampletxt", "No"),        # No dot
    ("a.txt.exe", "No"),         # Two dots
    ("a..txt", "No"),            # Two dots (empty middle)
    (".txt", "No"),              # Empty prefix
    ("a.", "No"),                # Empty extension
    
    # --- Invalid: Prefix Conditions ---
    ("1example.dll", "No"),      # Starts with digit
    ("_example.txt", "No"),      # Starts with special character
    (" example.txt", "No"),      # Starts with space
    ("!abc.exe", "No"),          # Starts with symbol
    ("1.txt", "No"),             # Prefix is just a digit
    
    # --- Invalid: Extension Conditions ---
    ("a.png", "No"),             # Not in allowed list
    ("a.txt1", "No"),            # Extension contains extra characters
    ("a.exe ", "No"),            # Extension contains trailing space
    ("a.TXT", "No"),             # Case sensitivity (assuming strict match)
    ("a.dll.txt", "No"),         # (Handled by dot count, but tests extension logic)
    ("a.t", "No"),               # Extension too short
    
    # --- Edge Cases ---
    ("", "No"),                  # Empty string
    (".", "No"),                 # Just a dot
    ("a123.txt", "Yes"),         # Boundary: exactly 3 digits
    ("a1234.txt", "No"),         # Boundary: 4 digits
    ("A.exe", "Yes"),            # Boundary: Uppercase start
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected