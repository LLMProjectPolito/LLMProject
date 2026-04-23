
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

# The function is assumed to be defined in the same environment or imported.
# If testing in a real scenario, use: from your_module import file_name_check

@pytest.mark.parametrize("file_name, expected", [
    # --- POSITIVE CASES (Should return 'Yes') ---
    ("example.txt", "Yes"),
    ("a.exe", "Yes"),
    ("abc.dll", "Yes"),
    ("A12.txt", "Yes"),           # Starts with uppercase, has 2 digits
    ("z1b2c3.exe", "Yes"),        # Exactly 3 digits
    ("LongFileName123.dll", "Yes"), # Max digits allowed
    ("a.txt", "Yes"),             # Minimum valid length

    # --- NEGATIVE CASES: DIGITS ---
    ("a1234.txt", "No"),          # 4 digits (too many)
    ("1234abc.exe", "No"),        # 4 digits (too many)
    ("a1b2c3d4.dll", "No"),       # 4 digits (too many)
    ("a1b2c34.txt", "No"),        # 4 digits (too many)

    # --- NEGATIVE CASES: DOTS ---
    ("filename", "No"),           # No dot
    ("file.name.txt", "No"),      # Multiple dots
    (".txt", "No"),               # Empty substring before dot
    ("file.", "No"),              # Empty substring after dot
    ("file.txt.exe", "No"),       # Multiple dots
    ("file..txt", "No"),          # Double dot

    # --- NEGATIVE CASES: START CHARACTER ---
    ("1abc.txt", "No"),           # Starts with a digit
    ("_abc.txt", "No"),           # Starts with an underscore
    (" abc.txt", "No"),           # Starts with a space
    ("-abc.txt", "No"),           # Starts with a hyphen
    (".txt", "No"),               # Starts with a dot (empty before dot)
    ("!abc.txt", "No"),           # Starts with special character

    # --- NEGATIVE CASES: EXTENSION ---
    ("file.pdf", "No"),           # Invalid extension
    ("file.doc", "No"),           # Invalid extension
    ("file.txt1", "No"),          # Extension contains extra characters
    ("file.TXT", "No"),           # Case sensitivity check (assuming strict match)
    ("file.exe ", "No"),          # Trailing space in extension
    ("file.dll.txt", "No"),       # Multiple dots (extension is .txt, but dot count is wrong)
    ("file.t", "No"),             # Incomplete extension
    ("file.ex", "No"),            # Incomplete extension
])
def test_file_name_check(file_name, expected):
    """
    Tests the file_name_check function against various valid and invalid 
    scenarios to ensure all business logic constraints are met.
    """
    assert file_name_check(file_name) == expected

def test_file_name_check_non_string_input():
    """
    Blue Team edge case: Check how the function handles non-string inputs.
    Note: Depending on implementation, this might raise a TypeError.
    """
    with pytest.raises(TypeError):
        file_name_check(None)
    with pytest.raises(TypeError):
        file_name_check(123)