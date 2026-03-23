import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("MyFile.exe") == "Yes"
    assert file_name_check("AnotherFile.dll") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.exe") == "Yes"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("123example.txt") == "No"
    assert file_name_check("ex456ample.exe") == "No"
    assert file_name_check("file789.dll") == "No"
    assert file_name_check("1234example.txt") == "No"

def test_invalid_file_name_wrong_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("MyFile.jpg") == "No"
    assert file_name_check("AnotherFile.png") == "No"

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

def test_invalid_file_name_starts_with_special_character():
    assert file_name_check("!example.txt") == "No"
    assert file_name_check("@MyFile.exe") == "No"
    assert file_name_check("#AnotherFile.dll") == "No"

def test_edge_cases():
    assert file_name_check("a1.txt") == "Yes"
    assert file_name_check("A1.exe") == "Yes"
    assert file_name_check("example1.txt") == "Yes"
    assert file_name_check("example12.exe") == "Yes"
    assert file_name_check("example123.dll") == "Yes"
    assert file_name_check("example1234.txt") == "No"
    assert file_name_check("a.TXT") == "No"
    assert file_name_check("a.ExE") == "No"
    assert file_name_check("a.dLl") == "No"