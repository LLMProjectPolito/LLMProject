
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

    if len(parts) != 2:
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


def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("test.exe") == "Yes"
    assert file_name_check("data.dll") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.exe") == "Yes"
    assert file_name_check("file123.txt") == "Yes"
    assert file_name_check("file_name.txt") == "Yes"

def test_file_name_check_invalid_digits():
    assert file_name_check("1234.txt") == "No"
    assert file_name_check("file1234.txt") == "No"

def test_file_name_check_invalid_dot_count():
    assert file_name_check("example") == "No"
    assert file_name_check("example.txt.bak") == "No"

def test_file_name_check_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_file_name_check_invalid_start_char():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("!example.txt") == "No"

def test_file_name_check_invalid_extension():
    assert file_name_check("example.java") == "No"
    assert file_name_check("example.pdf") == "No"

def test_file_name_check_empty_string():
    assert file_name_check("") == "No"