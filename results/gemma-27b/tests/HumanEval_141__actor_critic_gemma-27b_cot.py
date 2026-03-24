
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

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("MyFile.exe") == "Yes"
    assert file_name_check("AnotherFile.dll") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.exe") == "Yes"
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("example1.txt") == "Yes"
    assert file_name_check("a1.txt") == "Yes"
    assert file_name_check("A1.exe") == "Yes"
    assert file_name_check("example12.dll") == "Yes"
    assert file_name_check("example123.exe") == "Yes"
    assert file_name_check("abc.txt") == "Yes"
    assert file_name_check("ABC.exe") == "Yes"
    assert file_name_check("aBc.dll") == "Yes"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("ex4567ample.dll") == "No"
    assert file_name_check("12345file.exe") == "No"

def test_invalid_file_name_wrong_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("file.jpg") == "No"
    assert file_name_check("document.png") == "No"

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == "No"
    assert file_name_check("fileexe") == "No"
    assert file_name_check("documentdll") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.backup") == "No"
    assert file_name_check("file.exe.old") == "No"
    assert file_name_check("document.dll.tmp") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("2file.exe") == "No"
    assert file_name_check("3document.dll") == "No"

def test_invalid_file_name_starts_with_special_character():
    assert file_name_check("_example.txt") == "No"
    assert file_name_check("!file.exe") == "No"
    assert file_name_check("$document.dll") == "No"

def test_empty_string():
    assert file_name_check("") == "No"

def test_long_filename():
    long_name = "a" * 200 + ".txt"
    assert file_name_check(long_name) == "No"

def test_filename_with_only_dot():
    assert file_name_check(".") == "No"

def test_filename_with_spaces_at_beginning():
    assert file_name_check(" example.txt") == "No"

def test_filename_with_spaces_at_end():
    assert file_name_check("example.txt ") == "No"

def test_filename_with_special_characters_within_name():
    assert file_name_check("example@file.txt") == "No"
    assert file_name_check("example#file.exe") == "No"
    assert file_name_check("example%file.dll") == "No"
    assert file_name_check("example^file.txt") == "No"
    assert file_name_check("example&file.exe") == "No"
    assert file_name_check("example*file.dll") == "No"
    assert file_name_check("example(file.txt") == "No"
    assert file_name_check("example)file.exe") == "No"
    assert file_name_check("example+file.dll") == "No"
    assert file_name_check("example=file.txt") == "No"
    assert file_name_check("example[file.exe") == "No"
    assert file_name_check("example]file.dll") == "No"
    assert file_name_check("example{file.txt") == "No"
    assert file_name_check("example}file.exe") == "No"
    assert file_name_check("example|file.dll") == "No"
    assert file_name_check("example;file.txt") == "No"
    assert file_name_check("example:file.exe") == "No"
    assert file_name_check("example'file.dll") == "No"
    assert file_name_check('example"file.txt') == "No"
    assert file_name_check("example<file.exe") == "No"
    assert file_name_check("example>file.dll") == "No"
    assert file_name_check("example,file.txt") == "No"
    assert file_name_check("example?file.exe") == "No"
    assert file_name_check("example/file.dll") == "No"
    assert file_name_check("example\\file.txt") == "No"

def test_disallowed_characters():
    assert file_name_check("example-file.txt") == "No"
    assert file_name_check("example_file.txt") == "No"
    assert file_name_check("example file.txt") == "No"