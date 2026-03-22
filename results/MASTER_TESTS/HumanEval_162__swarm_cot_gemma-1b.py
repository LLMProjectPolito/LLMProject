import pytest
import hashlib

def string_to_md5(text):
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def string_to_md5(text):
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def string_to_md5(text):
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_string_to_md5():
    assert string_to_md5("hello") == "b10a8db164e075416e5799bca0976ffb"
    assert string_to_md5("") == None
    assert string_to_md5("world") == "a65d8f8f8f8f8f8f8f8f8f8f8f8f8f8f"
    assert string_to_md5("123") == "a65d8f8f8f8f8f8f8f8f8f8f8f8f8f8f"
    assert string_to_md5("hello world") == "b10a8db164e075416e5799bca0976ffb"