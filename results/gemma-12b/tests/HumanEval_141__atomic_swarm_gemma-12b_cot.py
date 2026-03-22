import pytest
import math

def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"

def test_edge_empty_filename():
    assert file_name_check("") == "No"

def test_edge_no_dot():
    assert file_name_check("example") == "No"

def test_edge_multiple_dots():
    assert file_name_check("example.txt.exe") == "No"

def test_edge_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_edge_invalid_extension():
    assert file_name_check("example.pdf") == "No"

def test_edge_too_many_digits():
    assert file_name_check("1234example.txt") == "No"

def test_edge_filename_starts_with_digit():
    assert file_name_check("1example.txt") == "No"

def test_edge_extension_case_sensitive():
    assert file_name_check("example.TXT") == "No"

def test_edge_extension_with_space():
    assert file_name_check("example.txt ") == "No"

import pytest

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == "No"

def test_file_name_check_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_file_name_check_no_dot():
    assert file_name_check("example") == "No"

def test_file_name_check_multiple_dots():
    assert file_name_check("example.txt.pdf") == "No"

def test_file_name_check_too_many_digits():
    assert file_name_check("1234example.txt") == "No"

def test_file_name_check_digit_start():
    assert file_name_check("123.txt") == "No"

def test_file_name_check_non_latin_start():
    assert file_name_check("éxample.txt") == "No"

def test_file_name_check_empty_string():
    assert file_name_check("") == "No"