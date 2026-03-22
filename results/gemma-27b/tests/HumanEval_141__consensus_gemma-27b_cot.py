import pytest

def test_valid_file_names():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("document1.dll") == 'Yes'
    assert file_name_check("A.txt") == 'Yes'
    assert file_name_check("file123.txt") == 'Yes'
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.exe") == "Yes"
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("file123.dll") == "Yes"
    assert file_name_check("ExAmPlE.txt") == "Yes"
    assert file_name_check("MyFiLe.exe") == "Yes"
    assert file_name_check("AnOtHeRfIlE.dll") == "Yes"
    assert file_name_check("file12.txt") == "Yes"
    assert file_name_check("file123.exe") == "Yes"

def test_invalid_file_names_digit_count():
    assert file_name_check("1234example.txt") == 'No'
    assert file_name_check("example1234.exe") == 'No'
    assert file_name_check("1234.dll") == "No"
    assert file_name_check("file1234.txt") == "No"
    assert file_name_check("file1234.exe") == "No"
    assert file_name_check("file1234.dll") == "No"

def test_invalid_file_names_dot_count():
    assert file_name_check("example.txt.txt") == 'No'
    assert file_name_check("exampletxt") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("MyFile.exe.dll") == "No"
    assert file_name_check("AnotherFile..dll") == "No"

def test_invalid_file_names_starts_with_digit():
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("2MyFile.exe") == 'No'
    assert file_name_check("3AnotherFile.dll") == "No"

def test_invalid_file_names_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_file_names_invalid_extension():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("file.jpg") == 'No'
    assert file_name_check("MyFile.jpg") == "No"
    assert file_name_check("AnotherFile.png") == "No"

def test_edge_cases():
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("A.exe") == 'Yes'
    assert file_name_check("abc.dll") == 'Yes'
    assert file_name_check("example1.txt") == 'Yes'
    assert file_name_check("example12.exe") == 'Yes'
    assert file_name_check("example123.dll") == 'Yes'
    assert file_name_check("example.TXT") == 'No'
    assert file_name_check("example.ExE") == 'No'
    assert file_name_check("example.DlL") == 'No'

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == "No"
    assert file_name_check("MyFileexe") == "No"
    assert file_name_check("AnotherFiledll") == "No"

def test_invalid_file_name_starts_with_special_character():
    assert file_name_check("!example.txt") == "No"
    assert file_name_check("@MyFile.exe") == "No"
    assert file_name_check("#AnotherFile.dll") == "No"

def test_invalid_file_name_empty_string():
    assert file_name_check("") == "No"