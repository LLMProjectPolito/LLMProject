import pytest
import math

def test_basic():
    assert file_name_check("example.txt") == "Yes"

def test_edge():
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("abc.exe") == "Yes"
    assert file_name_check("a1.dll") == "Yes"
    assert file_name_check("a123.txt") == "Yes"
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check(".txt") == "No"
    assert file_name_check("1.txt") == "No"
    assert file_name_check("a.tx") == "No"
    assert file_name_check("a.exe1") == "No"
    assert file_name_check("a.txt.") == "No"
    assert file_name_check("a..txt") == "No"
    assert file_name_check("a.txttxt") == "No"
    assert file_name_check("a.123") == "No"
    assert file_name_check("a1b.txt") == "Yes"
    assert file_name_check("A.txt") == "Yes"
    assert file_name_check("A123.dll") == "Yes"

def test_invalid_extension():
    assert file_name_check("example.pdf") == "No"