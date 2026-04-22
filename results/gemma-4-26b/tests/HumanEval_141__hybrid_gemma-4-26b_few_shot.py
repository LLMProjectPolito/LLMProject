
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

# Assuming the function is imported from your module
# from your_module import file_name_check

@pytest.mark.parametrize("file_name", [
    "example.txt",
    "test.exe",
    "my_file.dll",
    "A.txt",
    "Z.txt",
    "a1b2c3.exe",    # Exactly 3 digits
    "file1.txt",     # 1 digit
    "abc123.dll",    # 3 digits
    "abc.txt",       # 0 digits
])
def test_valid_filenames(file_name):
    """Tests filenames that meet all criteria (prefix, digits, dots, and extension)."""
    assert file_name_check(file_name) == "Yes"


@pytest.mark.parametrize("file_name", [
    "1abc.txt",      # Starts with a digit
    "1234.txt",      # Starts with a digit
    "_abc.txt",      # Starts with underscore
    " abc.txt",      # Starts with space
    "!abc.txt",      # Starts with special char
    ".txt",          # Empty prefix
    "",              # Completely empty
])
def test_invalid_prefix(file_name):
    """Tests that the prefix must be non-empty and start with a letter."""
    assert file_name_check(file_name) == "No"


@pytest.mark.parametrize("file_name", [
    "a1234.txt",     # 4 digits
    "abc1234.exe",   # 4 digits
    "a1b2c3d4.dll",  # 4 digits
    "99999.dll",     # 5 digits
])
def test_invalid_digit_count(file_name):
    """Tests that the prefix contains a maximum of three digits."""
    assert file_name_check(file_name) == "No"


@pytest.mark.parametrize("file_name", [
    "filename",      # Zero dots
    "file.name.txt", # Two dots
    "file..txt",     # Double dot
    "file.txt.exe",  # Two dots
])
def test_invalid_dot_count(file_name):
    """Tests that there must be exactly one dot separating prefix and extension."""
    assert file_name_check(file_name) == "No"


@pytest.mark.parametrize("file_name", [
    "file.jpg",      # Unauthorized extension
    "file.pdf",      # Unauthorized extension
    "file.txtt",     # Typo in extension
    "file.exe1",     # Extra character in extension
    "file.TXT",      # Case sensitivity (assuming strict match)
    "file.DLL",      # Case sensitivity
    "file.t",        # Incomplete extension
    "file.",         # Empty extension
    "file.exe ",     # Trailing space
])
def test_invalid_extensions(file_name):
    """Tests that the extension must be exactly 'txt', 'exe', or 'dll'."""
    assert file_name_check(file_name) == "No"


@pytest.mark.parametrize("file_name", [
    "a1234.jpg",     # Too many digits AND wrong extension
    "1a.b.txt",      # Starts with digit AND too many dots
    ".pdf",          # Empty prefix AND wrong extension
    "1234.png",      # Too many digits AND wrong extension
])
def test_edge_case_multiple_violations(file_name):
    """Tests combinations of multiple rule violations."""
    assert file_name_check(file_name) == "No"