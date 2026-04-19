
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

# The function is assumed to be imported or defined in the environment.
# from solution import file_name_check

@pytest.mark.parametrize("file_name, expected", [
    ("example.txt", "Yes"),
    ("document1.exe", "Yes"),
    ("system_file22.dll", "Yes"),
    ("A.txt", "Yes"),
    ("my123file.exe", "Yes"), # Exactly 3 digits
    ("ValidName.dll", "Yes"),
])
def test_valid_filenames(file_name, expected):
    """Test cases that meet all validity criteria."""
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize("file_name", [
    "file1234.txt",    # 4 digits
    "12345.exe",       # 5 digits
    "a1b2c3d4.dll",    # 4 digits scattered
])
def test_too_many_digits(file_name):
    """Test that more than three digits result in 'No'."""
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    "filenametxt",     # 0 dots
    "file.name.txt",   # 2 dots
    "file..txt",       # 2 dots
    "...",             # 3 dots
    "",                # 0 dots (Empty string)
    " ",               # 0 dots (Whitespace string)
])
def test_dot_count(file_name):
    """Test that exactly one dot is required."""
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    ".txt",            # Empty prefix
    "1file.txt",       # Starts with digit
    "1.txt",           # Minimal prefix (digit)
    "_file.txt",       # Starts with underscore
    "!file.exe",       # Starts with symbol
    " file.dll",       # Starts with space
    ".",               # Empty prefix and empty extension
])
def test_prefix_constraints(file_name):
    """Test that prefix is non-empty and starts with a Latin letter (a-z, A-Z)."""
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    "file.pdf",        # Invalid extension
    "file.png",        # Invalid extension
    "file.txt1",       # Extension contains digit
    "file.123",        # Extension is only digits
    "file.TXT",        # Case sensitivity check
    "file.Exe",        # Case sensitivity check
    "file.DLL",        # Case sensitivity check
    "file.",           # Empty extension
])
def test_extension_constraints(file_name):
    """Test that the extension is exactly 'txt', 'exe', or 'dll' (lowercase)."""
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name, expected", [
    ("a😊.txt", "Yes"),      # Starts with Latin, contains Emoji (Allowed)
    ("Кириллица.txt", "No"), # Starts with non-Latin (Cyrillic)
    ("😊file.txt", "No"),     # Starts with non-Latin (Emoji)
    ("a漢字.exe", "Yes"),     # Starts with Latin, contains Kanji (Allowed)
    ("éxample.txt", "No"),   # Starts with accented Latin (Not in a-z, A-Z)
])
def test_non_latin_characters(file_name, expected):
    """
    Test that only the first character of the prefix is restricted to ASCII Latin letters.
    """
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize("file_name", [
    "example.txt ",    # Trailing space
    " example.txt",    # Leading space
    "example .txt",    # Space before dot
    "example. txt",    # Space after dot
])
def test_whitespace_handling(file_name):
    """Test that leading, trailing, or internal whitespace results in 'No'."""
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("invalid_input", [
    None,              # NoneType
    123,               # Integer
    ["example.txt"],   # List
    {"name": "file.txt"} # Dictionary
])
def test_invalid_input_types(invalid_input):
    """Test that non-string inputs are handled without crashing."""
    try:
        result = file_name_check(invalid_input)
        assert result == "No"
    except (AttributeError, TypeError):
        # If the implementation doesn't handle types, it might raise these.
        # In a strict environment, we'd prefer the function to return "No".
        pytest.fail(f"Function crashed with {type(invalid_input)} input")