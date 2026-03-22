import pytest

def test_strongest_extension():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('class_name', ['extension1', 'extension2']) == 'class_name.extension1'

def test_strongest_extension_tied_strength():
    assert Strongest_Extension('class_name', ['AA', 'BB']) == 'class_name.AA'
    assert Strongest_Extension('class_name', ['aa', 'bb']) == 'class_name.aa'

def test_strongest_extension_empty_list():
    with pytest.raises(IndexError):
        Strongest_Extension('class_name', [])

def test_strongest_extension_single_extension():
    assert Strongest_Extension('class_name', ['extension']) == 'class_name.extension'

def test_strongest_extension_no_uppercase():
    assert Strongest_Extension('class_name', ['abc', 'def']) == 'class_name.abc'

def test_strongest_extension_no_lowercase():
    assert Strongest_Extension('class_name', ['ABC', 'DEF']) == 'class_name.ABC'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('class_name', ['AbC', 'DeF']) == 'class_name.AbC'