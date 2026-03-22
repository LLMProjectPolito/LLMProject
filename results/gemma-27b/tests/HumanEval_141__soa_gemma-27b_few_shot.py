import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("MyFile.exe") == "Yes"
    assert file_name_check("Document1.dll") == "Yes"
    assert file_name_check("A.txt") == "Yes"
    assert file_name_check("file123.txt") == "Yes"

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == "No"
    assert file_name_check("myfileexe") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.backup") == "No"
    assert file_name_check("file.name.dll") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("2myfile.exe") == "No"

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("myfile.pdf") == "No"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("example1234.txt") == "No"
    assert file_name_check("file1234.exe") == "No"
    assert file_name_check("document1234.dll") == "No"

def test_invalid_file_name_special_characters():
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("my_file.exe") == "No"

def test_empty_file_name():
    assert file_name_check("") == "No"