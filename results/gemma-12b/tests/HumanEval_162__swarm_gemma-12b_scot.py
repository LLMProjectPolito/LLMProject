
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from hashlib import md5
import math

def test_unicode_string():
    text = "你好世界"  # Chinese characters
    expected_md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_md5

    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == md5_hash

    expected_md5 = md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_md5