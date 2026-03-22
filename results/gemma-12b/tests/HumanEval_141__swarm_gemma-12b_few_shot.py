import pytest
import math

def test_file_name_check_leading_digit():
    assert file_name_check("123.txt") == 'No'