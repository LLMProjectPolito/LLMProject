import pytest
import math

def test_file_name_check_empty_before_dot():
    assert file_name_check(".txt") == 'No'