
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
    if not file_name:
        return 'No'

    digit_count = 0
    dot_count = 0
    parts = file_name.split('.')

    if len(parts) != 2:
        return 'No'

    name_before_dot = parts[0]
    extension = parts[1]

    for char in name_before_dot:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if dot_count != 1:
        return 'No'

    if not name_before_dot:
        return 'No'

    if not name_before_dot[0].isalpha():
        return 'No'

    allowed_extensions = {'txt', 'exe', 'dll'}
    if extension not in allowed_extensions:
        return 'No'

    return 'Yes'


@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("example.exe", "Yes"),
        ("example.TXT", "Yes"),
        ("example.DLL", "Yes"),
        ("ex.txt", "Yes"),
        ("ex.exe", "Yes"),
        ("ex.dll", "Yes"),
        ("ex", "No"),
        (".", "No"),
        ("1.", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a1.txt", "No"),
        ("A1.exe", "No"),
        ("a.1txt", "No"),
        ("A.1exe", "No"),
        ("a.1dll", "No"),
        ("1a.txt", "No"),
        ("a.123txt", "No"),
        ("a.txt1", "No"),
        ("a.txt12", "No"),
        ("a.txt123", "No"),
        ("a.txt.bak", "No"),
        ("a.txt.exe.bak", "No"),
        ("a.txt.exe.dll", "No"),
        ("a.txt.exe.txt", "No"),
        ("a.txt.exe.1", "No"),
        ("a.txt.exe.12", "No"),
        ("a.txt.exe.123", "No"),
        ("a.txt.exe.txt1", "No"),
        ("a.txt.exe.txt12", "No"),
        ("a.txt.exe.txt123", "No"),
        ("a.txt.exe.txt.bak", "No"),
        ("a.txt.exe.txt.dll", "No"),
        ("a.txt.exe.txt.txt", "No"),
        ("a.txt.exe.txt.1", "No"),
        ("a.txt.exe.txt.12", "No"),
        ("a.txt.exe.txt.123", "No"),
        ("a.txt.exe.txt.txt1", "No"),
        ("a.txt.exe.txt.txt12", "No"),
        ("a.txt.exe.txt.txt123", "No"),
        ("a.txt.exe.txt.txt.bak", "No"),
        ("a.txt.exe.txt.txt.dll", "No"),
        ("a.txt.exe.txt.txt.txt", "No"),
        ("a.txt.exe.txt.txt.txt.1", "No"),
        ("a.txt.exe.txt.txt.txt.12", "No"),
        ("a.txt.exe.txt.txt.txt.txt", "No"),
        ("a.txt.exe.txt.txt.txt.txt.1", "No"),
        ("a.txt.exe.txt.txt.txt.txt.12", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.1", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.12", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.1", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.12", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.bak", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.1", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.12", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.123", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt1", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt12", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt123", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.bak", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.1", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.12", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.123", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt1", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt12", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt123", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt.bak", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt.txt", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt.1", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt.12", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.txt.txt.123", "No"),
        ("a.txt.exe.txt.txt.txt.txt.txt.txt.