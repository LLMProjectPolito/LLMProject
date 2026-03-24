
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
from your_module import file_name_check  # Replace your_module

ALLOWED_EXTENSIONS = ["txt", "exe", "dll"]
MAX_DIGITS = 3


def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("my_program.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.txt") == "Yes"
    assert file_name_check("file123.txt") == "Yes"
    assert file_name_check("abc123.txt") == "Yes"
    assert file_name_check("a123.txt") == "Yes"


@pytest.mark.parametrize("num_digits", [0, 1, 2, 3, 4, 5])
def test_invalid_file_name_too_many_digits(num_digits):
    if num_digits <= MAX_DIGITS:
        assert file_name_check(f"a{"1" * num_digits}.txt") == "Yes"
    else:
        assert file_name_check(f"a{num_digits}{"1" * (num_digits - MAX_DIGITS)}.txt") == "No"


def test_invalid_file_name_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"
    assert file_name_check("123") == "No"


def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check(".txt") == "No"
    assert file_name_check("example..txt") == "No"


def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"


def test_invalid_file_name_not_letter_before_dot():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("example#.txt") == "No"
    assert file_name_check("example$.txt") == "No"


def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.xyz") == "No"
    assert file_name_check("example.") == "No"


def test_invalid_file_name_empty_extension():
    assert file_name_check("example.") == "No"


def test_edge_cases_valid():
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("abc.txt") == "Yes"


def test_edge_cases_invalid():
    assert file_name_check("") == "No"
    assert file_name_check(".") == "No"
    assert file_name_check("a.txt ") == "No"
    assert file_name_check(" a.txt") == "No"
    assert file_name_check("a.txt\t") == "No"
    assert file_name_check("a.txt\n") == "No"
    assert file_name_check("example .txt") == "No"


def test_long_filename():
    assert file_name_check("a" * 100 + ".txt") == "Yes"  # Test a long but valid filename


def test_special_characters():
    assert file_name_check("example!@#$.txt") == "No"
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("example!.exe") == "No"
    assert file_name_check("example!.dll") == "No"
    assert file_name_check("a!.txt") == "No"
    assert file_name_check("a!1.txt") == "Yes"
    assert file_name_check("a!12.txt") == "Yes"
    assert file_name_check("a!123.txt") == "Yes"
    assert file_name_check("a!1234.txt") == "No"