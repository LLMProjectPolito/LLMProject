import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("MyFile.exe") == "Yes"
    assert file_name_check("AnotherFile.dll") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.exe") == "Yes"
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("file123.dll") == "Yes"
    assert file_name_check("fileABC.exe") == "Yes"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("example1234.dll") == "No"
    assert file_name_check("1234.exe") == "No"

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == "No"
    assert file_name_check("MyFileexe") == "No"
    assert file_name_check("AnotherFiledll") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.txt") == "No"
    assert file_name_check("My.File.exe") == "No"
    assert file_name_check("Another.File.dll") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("2MyFile.exe") == "No"
    assert file_name_check("3AnotherFile.dll") == "No"

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("MyFile.jpg") == "No"
    assert file_name_check("AnotherFile.png") == "No"

def test_invalid_file_name_starts_with_special_char():
    assert file_name_check("_example.txt") == "No"
    assert file_name_check("!MyFile.exe") == "No"
    assert file_name_check("@AnotherFile.dll") == "No"

def test_invalid_file_name_empty_string():
    assert file_name_check("") == "No"

def test_invalid_file_name_extension_uppercase():
    assert file_name_check("example.TXT") == "No"
    assert file_name_check("MyFile.EXE") == "No"
    assert file_name_check("AnotherFile.DLL") == "No"