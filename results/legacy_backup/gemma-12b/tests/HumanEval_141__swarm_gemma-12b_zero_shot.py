import pytest
import math

def test_file_name_check_leading_digit_and_too_many_digits():
    assert file_name_check("1234example.txt") == 'No'