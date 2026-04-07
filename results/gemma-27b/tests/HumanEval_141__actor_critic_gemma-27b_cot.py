
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
    ("example.txt", "Yes"),
    ("MyFile.exe", "Yes"),
    ("AnotherFile.dll", "Yes"),
    ("a.txt", "Yes"),
    ("A.exe", "Yes"),
    ("a1.txt", "Yes"),
    ("A1.exe", "Yes"),
    ("example1.txt", "Yes"),
    ("example12.dll", "Yes"),
    ("example123.exe", "Yes"),
    ("123example.txt", "No"),
    ("ex456ample.dll", "No"),
    ("1234file.exe", "No"),
    ("example.pdf", "No"),
    ("file.jpg", "No"),
    ("document.png", "No"),
    ("exampletxt", "No"),
    ("fileexe", "No"),
    ("documentdll", "No"),
    ("example.txt.backup", "No"),
    ("file..exe", "No"),
    ("document.version.dll", "No"),
    (".txt", "No"),
    (".exe", "No"),
    (".dll", "No"),
    ("1example.txt", "No"),
    ("2file.exe", "No"),
    ("3document.dll", "No"),
    ("_example.txt", "No"),
    ("!file.exe", "No"),
    ("$document.dll", "No"),
    ("", "No"),
    ("a.TXT", "Yes"),
    ("a.ExE", "Yes"),
    ("a.dLl", "Yes"),
    ("a.txT", "Yes"),
    ("a.exE", "Yes"),
    ("a.dLl", "Yes"),
    ("example with spaces.txt", "No"),
    ("example/with/slashes.exe", "No"),
    ("example:with:colons.dll", "No"),
    "verylongfilenameverylongfilenameverylongfilename.txt", "No",
    ("valid.txt ", "No"),
    (" valid.txt", "No"),
    ("a1b2c3d4.txt", "No"),
    ("a.tx", "No"),
    ("a.t", "No"),
    ("a.", "No"),
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected