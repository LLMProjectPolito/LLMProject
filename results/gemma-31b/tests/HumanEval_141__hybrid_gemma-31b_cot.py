
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
    ("document.exe", "Yes"),
    ("system.dll", "Yes"),
    ("MyFile.exe", "Yes"),
    ("MyFile.dll", "Yes"),
    ("a.txt", "Yes"),
    ("Z.exe", "Yes"),
    ("UppercaseStart.txt", "Yes"),
    ("lowercasestart.exe", "Yes"),
    ("test.txt", "Yes"),           # 0 digits
    ("file1.exe", "Yes"),          # 1 digit
    ("test12.exe", "Yes"),         # 2 digits
    ("file12.dll", "Yes"),         # 2 digits
    ("a123.txt", "Yes"),           # 3 digits (boundary)
    ("file123.txt", "Yes"),        # 3 digits
    ("a1b2c3.exe", "Yes"),         # 3 digits spread out
    ("A1B2C3.exe", "Yes"),         # 3 digits spread out, uppercase
    ("abc123def.dll", "Yes"),      # 3 digits inside prefix
    ("LongerFileNameWithDigits123.dll", "Yes"),

    # --- Invalid: Digit Count (More than 3) ---
    ("a1234.txt", "No"),            # 4 digits
    ("file1234.txt", "No"),        # 4 digits
    ("a12b34c5.exe", "No"),        # 5 digits
    ("f1i2l3e4.dll", "No"),        # 4 digits
    ("1234.dll", "No"),            # 4 digits and starts with digit
    ("1234file.exe", "No"),        # 4 digits and starts with digit
    ("12345.txt", "No"),           # 5 digits

    # --- Invalid: Dot Conditions (Must be exactly one dot) ---
    ("exampletxt", "No"),           # No dot
    ("example.txt.txt", "No"),      # Too many dots
    ("example..txt", "No"),         # Too many dots
    ("example.t.txt", "No"),        # Too many dots
    ("...", "No"),                  # Too many dots
    (".", "No"),                    # Just a dot

    # --- Invalid: Prefix Conditions (Must start with Latin letter, cannot be empty) ---
    (".txt", "No"),                 # Empty prefix
    ("1example.dll", "No"),         # Starts with digit
    ("0.dll", "No"),                # Starts with digit
    ("_example.txt", "No"),         # Starts with underscore
    ("_.txt", "No"),                # Starts with underscore
    (" example.exe", "No"),         # Starts with space
    (" a.exe", "No"),               # Starts with space
    (" .txt", "No"),                # Prefix is a space
    ("!file.dll", "No"),            # Starts with special char
    ("!file.txt", "No"),            # Starts with special char
    ("éxample.txt", "No"),          # Starts with non-latin letter

    # --- Invalid: Suffix Conditions (Must be 'txt', 'exe', or 'dll' - Case Sensitive) ---
    ("file.pdf", "No"),             # Unsupported extension
    ("file.png", "No"),             # Unsupported extension
    ("file.tx", "No"),              # Extension too short
    ("file.txts", "No"),            # Extension too long
    ("file.TXT", "No"),             # Case sensitivity
    ("file.EXE", "No"),             # Case sensitivity
    ("file.Dll", "No"),             # Case sensitivity
    ("file.DLL", "No"),             # Case sensitivity
    ("example.", "No"),             # Empty extension
    ("a.txt1", "No"),               # Digit in extension
    ("a.exe ", "No"),               # Trailing space in extension

    # --- Edge Cases ---
    ("", "No"),                     # Empty string
])
def test_file_name_check(file_name, expected):
    """
    Comprehensive test suite for file_name_check.
    Validates:
    1. Prefix starts with a Latin letter.
    2. Prefix contains 0-3 digits.
    3. Exactly one dot separating prefix and extension.
    4. Extension is exactly 'txt', 'exe', or 'dll'.
    """
    assert file_name_check(file_name) == expected

def test_complex_mixed_invalid():
    """Tests strings that fail multiple criteria simultaneously."""
    # No starting letter, too many digits, wrong extension
    assert file_name_check("12345.png") == "No"
    # No starting letter, too many dots
    assert file_name_check("1.2.3.txt") == "No"
    # Empty prefix, wrong extension
    assert file_name_check(".jpg") == "No"