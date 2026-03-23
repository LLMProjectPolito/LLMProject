import pytest
import math

def test_basic():
    assert file_name_check("example.txt") == 'Yes'

def test_edge_empty_filename():
    assert file_name_check("") == "No"

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == 'No'