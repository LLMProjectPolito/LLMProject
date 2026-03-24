
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

```python
import pytest
import math

def is_valid_code(code):
    """
    Checks if the given code is valid.
    """
    try:
        exec(code)
        return True
    except Exception:
        return False

def is_valid_file(file_name):
    """
    Checks if the given file name is valid.
    """
    if not file_name:
        return "No"
    if not file_name[0].isalpha():
        return "No"
    if not file_name[-1].lower() in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("test.py", "Yes"),
        ("hello.c", "Yes"),
        ("test.txt", "No"),
        ("no_file.exe", "No"),
        ("test.exe", "Yes"),
        ("test.dll", "Yes"),
        ("test.txt.py", "No"),
        ("hello.exe", "No"),
        ("test.dll.txt", "No"),
        ("test.exe.py", "No"),
        ("test.txt.exe", "No"),
        ("test.dll.txt.py", "No"),
        ("test.exe.txt", "No"),
        ("test.dll.txt.exe", "No"),
    ],
)
def test_is_valid_code(file_name, expected):
    """
    Tests if the given code is valid.
    """
    is_valid_code(file_name)
    assert expected == "Yes"

def test_is_valid_file(file_name):
    """
    Tests if the given file name is valid.
    """
    assert is_valid_file(file_name)
    assert "No" not in file_name
    assert "No" not in file_name[0]
    assert "No" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-1]
    assert "Yes" not in file_name
    assert "Yes" not in file_name[0]
    assert "Yes" not in file_name[-