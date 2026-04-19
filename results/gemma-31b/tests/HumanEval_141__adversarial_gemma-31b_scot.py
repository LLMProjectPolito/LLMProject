
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

# The function is provided in the environment, we are testing it.
# from solution import file_name_check 

@pytest.mark.parametrize("file_name, expected", [
    # --- Positive Cases ---
    ("example.txt", "Yes"),
    ("MyFile.exe", "Yes"),
    ("system_lib.dll", "Yes"),
    ("a123.txt", "Yes"),        # 3 digits, starts with letter
    ("test12.exe", "Yes"),      # 2 digits
    ("file1.dll", "Yes"),       # 1 digit
    ("document.txt", "Yes"),    # 0 digits
    ("A.txt", "Yes"),           # Minimal valid prefix
    
    # --- Digit Constraint (Max 3) ---
    ("file1234.txt", "No"),     # 4 digits
    ("1234file.txt", "No"),     # 4 digits (also fails start char, but digit count is a primary rule)
    ("a1b2c3d4.exe", "No"),     # 4 digits scattered
    
    # --- Dot Constraint (Exactly one) ---
    ("exampletxt", "No"),       # 0 dots
    ("example.txt.bak", "No"),  # 2 dots
    ("example..txt", "No"),     # 2 dots
    (".txt", "No"),             # 1 dot, but prefix is empty
    
    # --- Prefix Constraints ---
    (".txt", "No"),             # Empty prefix
    ("1example.dll", "No"),     # Starts with digit
    ("_example.txt", "No"),     # Starts with underscore
    (" example.exe", "No"),     # Starts with space
    ("!file.dll", "No"),        # Starts with special char
    
    # --- Extension Constraints ---
    ("file.pdf", "No"),         # Invalid extension
    ("file.png", "No"),         # Invalid extension
    ("file.txt1", "No"),        # Extension too long
    ("file.tx", "No"),          # Extension too short
    ("file.TXT", "No"),         # Case sensitivity (should be lowercase)
    ("file.EXE", "No"),         # Case sensitivity
    ("file.DLL", "No"),         # Case sensitivity
    
    # --- Edge Cases ---
    ("", "No"),                 # Empty string
    (".", "No"),                # Only a dot
    ("a.", "No"),               # Prefix exists, extension empty
    (" .txt", "No"),            # Prefix is a space
    ("a" * 100 + ".txt", "Yes"),# Long valid prefix
])
def test_file_name_check(file_name, expected):
    """
    Test the file_name_check function against a variety of valid and invalid inputs.
    """
    assert file_name_check(file_name) == expected

def test_digit_boundary():
    """
    Specifically target the boundary of the digit count rule.
    """
    # 3 digits should be Yes
    assert file_name_check("abc123.txt") == "Yes"
    # 4 digits should be No
    assert file_name_check("abc1234.txt") == "No"

def test_prefix_start_boundary():
    """
    Specifically target the Latin alphabet start rule.
    """
    # Upper case start
    assert file_name_check("Z.txt") == "Yes"
    # Lower case start
    assert file_name_check("z.txt") == "Yes"
    # Non-latin start (e.g., Greek or Cyrillic)
    assert file_name_check("π.txt") == "No"