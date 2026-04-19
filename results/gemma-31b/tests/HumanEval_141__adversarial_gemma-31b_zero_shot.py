
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
    # Implementation provided by the user for testing purposes
    if file_name.count('.') != 1:
        return 'No'
    
    prefix, suffix = file_name.split('.')
    
    if not prefix or not prefix[0].isalpha():
        return 'No'
    
    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'
    
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'

@pytest.mark.parametrize("name, expected", [
    # --- Valid Cases ---
    ("example.txt", "Yes"),
    ("Example.exe", "Yes"),
    ("my_file.dll", "Yes"),
    ("a.txt", "Yes"),
    ("file1.txt", "Yes"),
    ("file12.txt", "Yes"),
    ("file123.txt", "Yes"),
    ("f1i2l3e.exe", "Yes"), # Digits spread out
    ("A1B2C3.dll", "Yes"),  # Exactly 3 digits
    
    # --- Digit Count Violations ---
    ("file1234.txt", "No"),   # 4 digits
    ("1234file.txt", "No"),   # 4 digits (also fails prefix, but digit count is a bug vector)
    ("a1b2c3d4.exe", "No"),   # 4 digits
    ("12345.dll", "No"),      # 5 digits
    
    # --- Dot Count Violations ---
    ("filename", "No"),       # 0 dots
    ("file.name.txt", "No"),  # 2 dots
    ("file..txt", "No"),      # 2 dots
    ("file.txt.", "No"),      # 2 dots
    
    # --- Prefix Violations ---
    (".txt", "No"),           # Empty prefix
    ("1example.dll", "No"),   # Starts with digit
    ("_example.txt", "No"),   # Starts with underscore
    (" example.exe", "No"),   # Starts with space
    ("!file.txt", "No"),      # Starts with special char
    
    # --- Suffix Violations ---
    ("file.pdf", "No"),       # Invalid extension
    ("file.png", "No"),       # Invalid extension
    ("file.txt1", "No"),      # Extension too long
    ("file.tx", "No"),        # Extension too short
    ("file.TXT", "No"),       # Case sensitivity check (should be lowercase)
    ("file.EXE", "No"),       # Case sensitivity check
    ("file.", "No"),          # Empty suffix
])
def test_file_name_check(name, expected):
    assert file_name_check(name) == expected

def test_edge_case_empty_string():
    assert file_name_check("") == "No"

def test_edge_case_only_dot():
    assert file_name_check(".") == "No"

def test_edge_case_long_string():
    # Valid prefix, valid suffix, exactly 3 digits, very long
    long_name = "a" * 1000 + "123" + ".txt"
    assert file_name_check(long_name) == "Yes"