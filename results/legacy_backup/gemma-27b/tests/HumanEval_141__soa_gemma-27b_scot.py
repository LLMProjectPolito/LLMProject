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
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    before_dot = parts[0]
    after_dot = parts[1]

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha():
        return 'No'

    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# STEP 2: PLAN - List test functions names and scenarios.
# Test functions:
# - test_valid_file_names: Tests valid file names.
# - test_invalid_digit_count: Tests file names with more than three digits.
# - test_invalid_dot_count: Tests file names with incorrect number of dots.
# - test_invalid_before_dot: Tests file names with empty or non-alphabetic substring before the dot.
# - test_invalid_after_dot: Tests file names with invalid substring after the dot.
# - test_edge_cases: Tests edge cases like empty string, dot only, etc.

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("myFile.exe", "Yes"),
        ("document1.dll", "Yes"),
        ("a123.txt", "Yes"),
        ("A123.exe", "Yes"),
        ("file.txt", "Yes"),
        ("file1.txt", "Yes"),
        ("file12.txt", "Yes"),
        ("file123.txt", "Yes"),
    ],
)
def test_valid_file_names(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("1234example.txt", "No"),
        ("example1234.txt", "No"),
        ("examp1e1234.txt", "No"),
        ("1234.txt", "No"),
    ],
)
def test_invalid_digit_count(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("exampletxt", "No"),
        ("example.txt.exe", "No"),
        (".txt", "No"),
        ("example", "No"),
    ],
)
def test_invalid_dot_count(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("1example.txt", "No"),
        ("example.txt", "Yes"),
        ("Example.txt", "Yes"),
        ("", "No"),
        ("..txt", "No"),
        ("example..txt", "No"),
    ],
)
def test_invalid_before_dot(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.doc", "No"),
        ("example.pdf", "No"),
        ("example.jpg", "No"),
        ("example.something", "No"),
    ],
)
def test_invalid_after_dot(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("", "No"),
        (".", "No"),
        ("example.", "No"),
        (".example", "No"),
    ],
)
def test_edge_cases(file_name, expected):
    assert file_name_check(file_name) == expected