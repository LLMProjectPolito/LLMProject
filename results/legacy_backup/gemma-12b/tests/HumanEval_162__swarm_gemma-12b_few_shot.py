import pytest
import math

def test_string_to_md5_non_string_input():
    assert string_to_md5(123) is None