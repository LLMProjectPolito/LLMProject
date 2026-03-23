import pytest
import math

import hashlib

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

import hashlib

def test_string_to_md5_empty():
    assert string_to_md5('') is None

import hashlib

def test_string_to_md5_empty():
    assert string_to_md5('') is None