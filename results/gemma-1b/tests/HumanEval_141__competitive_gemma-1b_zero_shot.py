
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

def test_file_name_check():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.txt.bak") == "No"
    assert file_name_check("example.txt.1") == "No"
    assert file_name_check("example.txt.a") == "No"
    assert file_name_check("example.txt.1a") == "No"
    assert file_name_check("example.txt.12") == "No"
    assert file_name_check("example.txt.123") == "No"
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("example.txt.1") == "Yes"
    assert file_name_check("example.txt.a") == "Yes"
    assert file_name_check("example.txt.1A") == "Yes"
    assert file_name_check("example.txt.123") == "Yes"
    assert file_name_check("example.txt.1234") == "No"
    assert file_name_check("example.txt.12345") == "No"
    assert file_name_check("example.txt.123456") == "No"
    assert file_name_check("example.txt.1234567") == "No"
    assert file_name_check("example.txt.12345678") == "No"
    assert file_name_check("example.txt.123456789") == "No"
    assert file_name_check("example.txt.1234567890") == "No"
    assert file_name_check("example.txt.12345678901") == "No"
    assert file_name_check("example.txt.123456789012") == "No"
    assert file_name_check("example.txt.1234567890123") == "No"
    assert file_name_check("example.txt.12345678901234") == "No"
    assert file_name_check("example.txt.123456789012345") == "No"
    assert file_name_check("example.txt.1234567890123456") == "No"
    assert file_name_check("example.txt.12345678901234567") == "No"
    assert file_name_check("example.txt.123456789012345678") == "No"
    assert file_name_check("example.txt.1234567890123456789") == "No"
    assert file_name_check("example.txt.12345678901234567890") == "No"
    assert file_name_check("example.txt.123456789012345678901") == "No"
    assert file_name_check("example.txt.1234567890123456789012") == "No"
    assert file_name_check("example.txt.12345678901234567890123") == "No"
    assert file_name_check("example.txt.123456789012345678901234") == "No"
    assert file_name_check("example.txt.1234567890123456789012345") == "No"
    assert file_name_check("example.txt.12345678901234567890123456") == "No"
    print("All tests passed")