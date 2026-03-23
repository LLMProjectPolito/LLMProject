import pytest
import hashlib

def test_string_to_md5_empty():
    assert string_to_md5("") is None