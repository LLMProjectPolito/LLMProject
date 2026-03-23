import pytest
import math

def test_string_to_md5_unicode_characters():
    """Tests handling of Unicode characters in the input string."""
    assert string_to_md5("你好世界") == "59529499999999999999999999999999"