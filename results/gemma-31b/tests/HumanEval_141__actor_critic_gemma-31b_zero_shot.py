
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
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Check for digit count
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    name_part, extension_part = file_name.split('.')
    
    # Check substring before dot
    # .isalpha() is Unicode-aware; we must explicitly check for Latin alphabet 'a'-'z', 'A'-'Z'
    if not name_part:
        return 'No'
    
    first_char = name_part[0]
    if not (('a' <= first_char <= 'z') or ('A' <= first_char <= 'Z')):
        return 'No'
    
    # Check substring after the dot
    if extension_part not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

@pytest.mark.parametrize("filename, expected", [
    # Valid cases
    ("example.txt", "Yes"),
    ("Example.exe", "Yes"),
    ("file123.dll", "Yes"),
    ("a.txt", "Yes"),
    ("f1i2l3e.txt", "Yes"),
    ("MyFile01.exe", "Yes"),
    
    # Invalid: Too many digits
    ("file1234.txt", "No"),
    ("f1i2l3e4.exe", "No"),
    ("1234.dll", "No"),
    
    # Invalid: Dot constraints
    ("example", "No"),            # No dot
    ("example.name.txt", "No"),   # More than one dot
    ("example..txt", "No"),       # More than one dot
    
    # Invalid: Before the dot
    (".txt", "No"),               # Empty before dot
    ("1example.dll", "No"),       # Starts with digit
    ("_example.txt", "No"),       # Starts with special char
    (" example.exe", "No"),       # Starts with space
    
    # Invalid: Non-Latin characters at the start (Edge Cases)
    ("éxample.txt", "No"),        # Latin-1 Supplement
    ("πile.txt", "No"),           # Greek
    ("你好.txt", "No"),            # CJK
    ("αpha.exe", "No"),           # Greek
    
    # Invalid: After the dot
    ("example.pdf", "No"),        # Wrong extension
    ("example.jpg", "No"),        # Wrong extension
    ("example.", "No"),           # Empty extension
    ("example.TXT", "No"),        # Case sensitivity check
    ("example.exee", "No"),       # Slightly wrong extension
])
def test_file_name_check(filename, expected):
    assert file_name_check(filename) == expected