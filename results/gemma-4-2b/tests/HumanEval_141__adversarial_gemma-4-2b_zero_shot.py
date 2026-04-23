
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
    digits = 0
    dot_count = 0
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    prefix = parts[0]
    suffix = parts[1]

    if not prefix:
        return 'No'

    for char in prefix:
        if '0' <= char <= '9':
            digits += 1

    if digits > 3:
        return 'No'

    if dot_count != 1:
        return 'No'

    if not suffix in ['txt', 'exe', 'dll']:
        return 'No'

    first_char = prefix[0]
    if not ('a' <= first_char <= 'z' or 'A' <= first_char <= 'Z'):
        return 'No'

    return 'Yes'


@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("example1.txt", "No"),
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("example.txt", "Yes"),
        ("example.a", "No"),
        ("example..txt", "No"),
        ("example", "No"),
        ("example.xyz", "No"),
        ("example.123", "No"),
        ("example.abc", "Yes"),
        ("example.ABC", "Yes"),
        ("example.123.txt", "No"),
        ("example.a.txt", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "No"),
        ("example.txt.exe", "No"),
        ("example.txt.dll", "