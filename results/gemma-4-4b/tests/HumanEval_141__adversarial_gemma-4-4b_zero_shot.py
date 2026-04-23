
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
    parts = file_name.split('.')

    if len(parts) != 2:
        return 'No'

    before_dot = parts[0]
    after_dot = parts[1]

    for char in before_dot:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if dot_count != 1:
        return 'No'

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha():
        return 'No'

    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("example.exe", "Yes"),
        ("example.TXT", "Yes"),
        ("example1.txt", "No"),
        ("examp.txt", "Yes"),
        ("example.123", "No"),
        ("examp.123.txt", "No"),
        ("examp.txt.txt", "No"),
        ("examp", "No"),
        ("example.", "No"),
        (".txt", "No"),
        ("example.xyz", "No"),
        ("example.XYZ", "Yes"),
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
        ("a.txt.xyz", "No"),
        ("A.exe.XYZ", "No"),
        ("123.txt", "No"),
        ("abc.txt", "Yes"),
        ("a123.txt", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.xyz", "No"),
        ("a.txt.ABC", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("a.txt.", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.