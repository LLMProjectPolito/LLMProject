
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
    # Condition: The file's name contains exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'
    
    parts = file_name.split('.')
    prefix = parts[0]
    suffix = parts[1]
    
    # Condition: Substring before the dot should not be empty, and it starts with a letter from the latin alphabet
    if not prefix or not prefix[0].isalpha():
        return 'No'
    
    # Condition: Substring after the dot should be one of these: ['txt', 'exe', 'dll']
    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Condition: There should not be more than three digits ('0'-'9') in the file's name
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'

@pytest.mark.parametrize("name, expected", [
    # --- Valid Cases ---
    ("example.txt", "Yes"),        # Basic valid
    ("Document.exe", "Yes"),       # Uppercase start
    ("my_file123.dll", "Yes"),     # Exactly 3 digits
    ("a.txt", "Yes"),              # Minimum valid prefix
    ("file1.exe", "Yes"),          # 1 digit
    ("f1i2l3e.dll", "Yes"),        # Digits scattered in prefix
    ("test.txt", "Yes"),           # Standard extension
    ("A.dll", "Yes"),              # Single letter prefix
    ("myFile123.exe", "Yes"),      # CamelCase with digits
    
    # --- Invalid: Digit Count (> 3) ---
    ("file1234.txt", "No"),        # 4 digits in prefix
    ("f1i2l3e4.exe", "No"),        # 4 digits scattered
    ("file.txt1234", "No"),        # Digits in suffix
    ("1234file.dll", "No"),        # 4 digits at start
    ("1a2b3c4.exe", "No"),         # 4 digits scattered
    ("12345.dll", "No"),           # Only digits (also fails alpha start)
    
    # --- Invalid: Dot Constraints ---
    ("exampletxt", "No"),          # No dot
    ("example..txt", "No"),        # Two dots
    ("my.file.txt", "No"),         # Two dots
    ("...txt", "No"),              # Multiple dots
    ("example.tar.gz", "No"),      # Multiple dots
    ("..txt", "No"),               # Multiple dots
    
    # --- Invalid: Prefix Rules ---
    (".txt", "No"),                # Empty prefix
    ("1example.dll", "No"),        # Starts with digit
    ("_file.exe", "No"),           # Starts with underscore
    ("!file.txt", "No"),           # Starts with special char
    (" 1file.dll", "No"),          # Starts with space
    ("_example.txt", "No"),        # Starts with underscore
    (" example.exe", "No"),        # Starts with space
    
    # --- Invalid: Suffix Rules ---
    ("file.pdf", "No"),            # Wrong extension
    ("file.txt1", "No"),           # Extension has extra char
    ("file.EXE", "No"),            # Case sensitivity
    ("file.", "No"),               # Empty suffix
    ("file.t", "No"),              # Too short suffix
    ("file.txttxt", "No"),         # Too long suffix
    ("file.png", "No"),            # Unsupported extension
    ("file.txts", "No"),           # Slight variation
    ("file.tx", "No"),             # Too short
    ("file.TXT", "No"),            # Case sensitivity
    ("file.ex", "No"),             # Too short
])
def test_file_name_check_parametrized(name, expected):
    assert file_name_check(name) == expected

def test_edge_case_large_number_of_digits():
    """Ensure that a very long string of digits is handled correctly."""
    assert file_name_check("a" + "1" * 10 + ".txt") == "No"

def test_edge_case_non_latin_start():
    """Ensure that non-latin characters at the start are rejected."""
    assert file_name_check("你好.txt") == "No"
    assert file_name_check("éxample.txt") == "No"

def test_edge_case_empty_string():
    """Ensure empty strings are handled."""
    assert file_name_check("") == "No"

def test_edge_case_only_dot():
    """Ensure a single dot is handled."""
    assert file_name_check(".") == "No"