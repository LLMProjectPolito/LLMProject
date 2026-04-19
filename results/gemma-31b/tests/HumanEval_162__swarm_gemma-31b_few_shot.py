
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import math

@pytest.mark.parametrize("input_str, expected", [
    ('你好', '7c72092058480f3465f404546671263c'),
    ('🚀', '83408a4243042382488772a2f8357f4e'),
])
def test_string_to_md5_unicode(input_str, expected):
    assert string_to_md5(input_str) == expected

def test_string_to_md5_empty():
    assert string_to_md5('') is None