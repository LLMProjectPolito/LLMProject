import pytest
from hashlib import md5

def test_string_to_md5_with_unicode_characters():
    """Test with a string containing unicode characters to ensure proper hashing."""
    text = "你好世界"  # Chinese characters
    expected_md5 = md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_md5