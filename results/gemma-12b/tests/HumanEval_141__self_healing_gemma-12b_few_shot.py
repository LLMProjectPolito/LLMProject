import re

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
        return "No"

    if file_name.count('.') != 1:
        return "No"

    parts = file_name.split('.')
    if len(parts[0]) == 0:
        return "No"

    if not re.match(r'^[a-zA-Z]', parts[0]):
        return "No"

    if not parts[1] in ['txt', 'exe', 'dll']:
        return "No"

    if re.search(r'\d{4,}', file_name):
        return "No"
    
    digits = re.findall(r'\d', file_name)
    if len(digits) > 3:
        return "No"

    return "Yes"

def test_valid_filename():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("my_file.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("longname.txt") == "Yes"

def test_invalid_filename_too_many_digits():
    assert file_name_check("123example.txt") == "No"
    assert file_name_check("1234example.txt") == "No"

def test_invalid_filename_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_filename_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_invalid_filename_non_letter_start():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("!example.txt") == "No"
    assert file_name_check("_example.txt") == "No"

def test_invalid_filename_wrong_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.zip") == "No"

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.txt.bak") == "No"

def test_invalid_filename_empty_string():
    assert file_name_check("") == "No"