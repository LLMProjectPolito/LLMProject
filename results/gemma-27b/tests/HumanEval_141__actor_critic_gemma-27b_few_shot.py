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
    dot_count = file_name.count('.')
    if dot_count != 1:
        return 'No'

    parts = file_name.split('.')
    before_dot = parts[0]
    after_dot = parts[1]

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha():
        return 'No'

    digit_count = sum(c.isdigit() for c in before_dot)

    if digit_count > 3:
        return 'No'

    if after_dot.lower() not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

import pytest

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("example1.txt", "Yes"),
        ("123example.txt", "No"),
        ("example.TXT", "Yes"),  # Case-insensitive extension
        ("example.txT", "Yes"),  # Case-insensitive extension
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("example.pdf", "No"),
        ("123.txt", "No"),
        (".txt", "No"),
        ("", "No"),
        ("a.txt", "Yes"),
        ("A.txt", "Yes"),
        ("a1.txt", "Yes"),
        ("a123.txt", "No"),
        ("a.exe", "Yes"),
        ("a.dll", "Yes"),
        ("a.pdf", "No"),
        ("1a.txt", "No"),
        ("a1b.txt", "Yes"),
        ("a1b2c.txt", "Yes"),
        ("a1b2c3.txt", "No"),
        ("abc123def.txt", "Yes"),  # Multiple chars before first digit
        (".", "No"),  # Only a dot
        ("example.longextension", "No"),  # Longer extension
        ("example123.txt", "Yes"),  # Digit at the end
        ("example .txt", "No"),  # Whitespace in filename
    ],
)
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected