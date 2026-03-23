import pytest
import math

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5("") is None

import hashlib

def test_string_to_md5_non_string_input():
    assert string_to_md5(123) is None