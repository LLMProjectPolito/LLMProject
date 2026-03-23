import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("my_program.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.exe") == "Yes"
    assert file_name_check("file123.txt") == "Yes"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("1234.txt") == "No"

def test_invalid_file_name_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check(".txt") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_invalid_file_name_non_letter_start():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("_example.txt") == "No"
    assert file_name_check(" example.txt") == "No"

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.") == "No"

def test_invalid_file_name_empty_extension():
    assert file_name_check("example.") == "No"

def test_file_name_with_digits_and_letters():
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("1file.txt") == "No"
    assert file_name_check("file12.exe") == "Yes"
    assert file_name_check("1file12.exe") == "No"

def test_file_name_with_special_characters():
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("example#.dll") == "No"

def test_empty_file_name():
    assert file_name_check("") == "No"