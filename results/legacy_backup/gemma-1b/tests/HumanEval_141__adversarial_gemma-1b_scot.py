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
    if not isinstance(file_name, str):
        return "No"

    if len(file_name) > 3:
        return "No"

    if not file_name.startswith('.'):
        return "No"

    if not file_name.startswith('a' <= file_name[1:].lower() <= 'z'):
        return "No"

    allowed_extensions = ['txt', 'exe', 'dll']
    if not file_name[1:].lower() in allowed_extensions:
        return "No"

    return "Yes"