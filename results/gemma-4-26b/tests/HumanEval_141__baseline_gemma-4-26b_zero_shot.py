
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
    ("a.exe", "Yes"),
    ("A.dll", "Yes"),
    ("file123.txt", "Yes"),
    ("test1.exe", "Yes"),
    ("test12.dll", "Yes"),
    ("test123.txt", "Yes"),
    ("abc.txt", "Yes"),
    ("Abc.exe", "Yes"),
    
    # Invalid: More than three digits
    ("a1234.txt", "No"),
    ("1234.txt", "No"),
    ("a1b2c3d4.txt", "No"),
    ("a1234e.exe", "No"),
    
    # Invalid: Dot count
    ("exampletxt", "No"),      # No dot
    ("a.txt.exe", "No"),       # Two dots
    ("a..txt", "No"),          # Two dots
    ("a.b.c.txt", "No"),       # Multiple dots
    
    # Invalid: Prefix rules (empty or doesn't start with letter)
    (".txt", "No"),            # Empty prefix
    ("1example.dll", "No"),    # Starts with digit
    ("_example.txt", "No"),    # Starts with underscore
    (" example.txt", "No"),    # Starts with space
    ("!example.exe", "No"),    # Starts with special char
    
    # Invalid: Extension rules
    ("example.png", "No"),     # Invalid extension
    ("example.txt1", "No"),    # Extension contains extra chars
    ("example.exe ", "No"),    # Extension has trailing space
    ("example.dll.txt", "No"), # Extension is not just the suffix (also fails dot rule)
    ("example.T", "No"),       # Extension too short
    ("example.txt.exe", "No"), # Extension is part of a larger string
    
    # Edge cases
    ("a.txt", "Yes"),
    ("a123.dll", "Yes"),
    ("a1234.dll", "No"),
    ("A.txt", "Yes"),
    ("a.exe", "Yes"),
    ("a.dll", "Yes"),
])
def test_file_name_check(file_name, expected):
    """
    Tests the file_name_check function with various valid and invalid inputs
    covering all specified constraints.
    """
    assert file_name_check(file_name) == expected

def test_file_name_check_types():
    """
    Optional: Test behavior with non-string inputs if the function 
    is expected to handle them (though the prompt implies string input).
    """
    with pytest.raises(TypeError):
        file_name_check(None)
    with pytest.raises(TypeError):
        file_name_check(123)