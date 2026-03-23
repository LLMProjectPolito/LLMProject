import pytest
import math

def test_file_name_check_basic():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_many_digits():
    assert file_name_check("1234example.txt") == "No"

def test_file_name_check_too_many_digits():
    assert file_name_check("1234example.txt") == "No"