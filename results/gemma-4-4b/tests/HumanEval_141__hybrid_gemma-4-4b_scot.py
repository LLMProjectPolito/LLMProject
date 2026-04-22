
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
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    digit_count = 0
    dot_count = 0
    parts = file_name.split(".")

    if len(parts) != 2:
        return "No"

    before_dot = parts[0]
    after_dot = parts[1]

    for char in before_dot:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return "No"

    if len(parts) != 2:
        return "No"

    if dot_count != 1:
        return "No"

    if not before_dot:
        return "No"

    if not before_dot[0].isalpha():
        return "No"

    if after_dot not in ["txt", "exe", "dll"]:
        return "No"

    return "Yes"



class TestFileNameCheck(pytest.Generator):
    @pytest.mark.parametrize(
        "file_name, expected",
        [
            ("example.txt", "Yes"),
            ("1example.dll", "No"),
            ("example.exe", "Yes"),
            ("example.TXT", "Yes"),
            ("example.DLL", "Yes"),
            ("example.123", "No"),
            ("123example.txt", "No"),
            ("example.123.txt", "No"),
            (".txt", "No"),
            ("example", "No"),
            ("example.xyz", "No"),
            ("example.pdf", "No"),
            ("example.txt.exe", "No"),
            ("a.txt", "Yes"),
            ("A.exe", "Yes"),
            ("a1.txt", "No"),
            ("A1.exe", "No"),
            ("a.txt1", "No"),
            ("A.exe1", "No"),
            ("a.txt.exe", "No"),
            ("A.exe.txt", "No"),
            ("a.txt.dll", "No"),
            ("A.exe.dll", "No"),
            ("a.txt.pdf", "No"),
            ("A.exe.pdf", "No"),
            ("a.txt.123", "No"),
            ("A.exe.123", "No"),
            ("a.txt.exe.dll", "No"),
            ("A.exe.txt.dll", "No"),
            ("a.txt.exe.pdf", "No"),
            ("A.exe.txt.pdf", "No"),
            ("a.txt.exe.123", "No"),
            ("A.exe.txt.123", "No"),
            ("a.txt.exe.dll.pdf", "No"),
            ("A.exe.txt.dll.pdf", "No"),
            ("a.txt.exe.dll.123", "No"),
            ("A.exe.txt.dll.123", "No"),
            ("a.txt.exe.dll.txt", "No"),
            ("A.exe.txt.dll.txt", "No"),
            ("a.txt.exe.dll.exe", "No"),
            ("A.exe.txt.dll.exe", "No"),
            ("a.txt.exe.dll.dll", "No"),
            ("A.exe.txt.dll.dll", "No"),
        ],
    )
    def test_file_name_check(self, file_name, expected):
        assert file_name_check(file_name) == expected