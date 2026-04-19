
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
    ("test.exe", "Yes"),
    ("library.dll", "Yes"),
    ("A.txt", "Yes"),
    ("Example.exe", "Yes"),
    ("z.dll", "Yes"),
    ("LongFileNameWithNoDigits.txt", "Yes"),
    ("file1.txt", "Yes"),
    ("file12.exe", "Yes"),
    ("file123.txt", "Yes"),
    ("MyFile123.exe", "Yes"),
    ("MyDocument23.dll", "Yes"),
    ("a1b2c3.exe", "Yes"),
    ("A1B2C3.txt", "Yes"),
    ("my_file_1.txt", "Yes"),
    ("a.txt", "Yes"),
    ("a123.dll", "Yes"),

    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("12345.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    ("abc1234def.dll", "No"),
    ("123.456.txt", "No"),

    # Invalid: Dot conditions (must be exactly one)
    ("exampletxt", "No"),
    ("filename", "No"),
    ("example.txt.txt", "No"),
    ("example..txt", "No"),
    ("file.name.txt", "No"),
    ("file.txt.", "No"),
    ("...", "No"),

    # Invalid: Substring before dot (empty or doesn't start with Latin letter)
    (".txt", "No"),
    ("1example.dll", "No"),
    ("1file.txt", "No"),
    ("1.txt", "No"),
    ("123A.txt", "No"),
    ("_example.txt", "No"),
    ("!example.exe", "No"),
    (" file.txt", "No"),
    (" example.exe", "No"),

    # Invalid: Substring after dot (must be exactly 'txt', 'exe', or 'dll')
    ("example.jpg", "No"),
    ("example.pdf", "No"),
    ("example.png", "No"),
    ("example.py", "No"),
    ("example.t", "No"),
    ("example.txtx", "No"),
    ("example.txt1", "No"),
    ("example.ex", "No"),
    ("example.exee", "No"),
    ("example.dlls", "No"),
    ("example.", "No"),
    ("example.TXT", "No"),
    ("file. TXT", "No"),

    # Edge cases
    ("", "No"),
    (" ", "No"),
    (" .txt", "No"),
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected