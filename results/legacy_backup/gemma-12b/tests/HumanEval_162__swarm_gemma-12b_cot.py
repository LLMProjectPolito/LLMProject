import pytest
import hashlib
import math

def test_empty_string_returns_none():
    """Test that an empty string input returns None."""
    from your_module import string_to_md5  # Replace your_module
    assert string_to_md5("") is None