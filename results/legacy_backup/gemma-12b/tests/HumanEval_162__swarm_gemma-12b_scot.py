import pytest
import hashlib

def test_unicode_string():
    text = "你好世界"  # A Unicode string (Chinese for "Hello world")
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert md5_hash == 'd2a8c894996969999999999999999999'