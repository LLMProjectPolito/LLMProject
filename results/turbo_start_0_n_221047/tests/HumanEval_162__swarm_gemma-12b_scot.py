import pytest
import hashlib

def test_unicode_string():
    text = "你好世界"  # Chinese characters
    expected_md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_md5