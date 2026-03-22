import pytest

def test_strongest_extension_empty_extensions():
    """Test with empty list of extensions"""
    assert Strongest_Extension('my_class', []) == 'my_class'

def test_strongest_extension_single_extension():
    """Test with a single extension"""
    assert Strongest_Extension('my_class', ['AA']) == 'my_class.AA'

def test_strongest_extension_multiple_extensions_different_strengths():
    """Test with multiple extensions having different strengths"""
    assert Strongest_Extension('my_class', ['AA', 'be', 'cC']) == 'my_class.cC'
    assert Strongest_Extension('my_class', ['AA', 'be', 'Bb']) == 'my_class.AA'

def test_strongest_extension_multiple_extensions_same_strength():
    """Test with multiple extensions having the same strength"""
    assert Strongest_Extension('my_class', ['AA', 'aA']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['aA', 'AA']) == 'my_class.AA'

def test_strongest_extension_empty_extensions():
    """Test with empty list of extensions"""
    with pytest.raises(IndexError):
        Strongest_Extension('my_class', [])

def test_strongest_extension_class_name_with_no_letters():
    """Test with class name having no letters"""
    with pytest.raises(TypeError):
        Strongest_Extension('', ['AA'])

def test_strongest_extension_class_name_with_lowercase_letters():
    """Test with class name having lowercase letters"""
    assert Strongest_Extension('my_class', ['AA']) == 'my_class.AA'

def test_strongest_extension_class_name_with_uppercase_letters():
    """Test with class name having uppercase letters"""
    assert Strongest_Extension('MyClass', ['AA']) == 'MyClass.AA'

def test_strongest_extension_class_name_with_only_uppercase_letters():
    """Test with class name having only uppercase letters"""
    assert Strongest_Extension('MYCLASS', ['AA']) == 'MYCLASS.AA'

def test_strongest_extension_class_name_with_only_lowercase_letters():
    """Test with class name having only lowercase letters"""
    assert Strongest_Extension('myclass', ['aa']) == 'myclass.aa'

def test_strongest_extension_class_name_with_mixed_case():
    """Test with class name having mixed case"""
    assert Strongest_Extension('MyClAsS', ['AA']) == 'MyClAsS.AA'

def test_strongest_extension_class_name_with_special_characters():
    """Test with class name having special characters"""
    assert Strongest_Extension('_my_class!', ['AA', 'Be', 'CC']) == '_my_class!.AA'

def test_strongest_extension_class_name_with_numbers():
    """Test with class name having numbers"""
    assert Strongest_Extension('my_class123', ['AA', 'Be', 'CC']) == 'my_class123.AA'

def test_strongest_extension_class_name_with_dots():
    """Test with class name having dots"""
    assert Strongest_Extension('my.class', ['AA', 'Be', 'CC']) == 'my.class.AA'

def test_strongest_extension_extension_with_uppercase_letters():
    """Test with extension having uppercase letters"""
    assert Strongest_Extension('my_class', ['SErViNgSlIcEs', 'Be', 'CC']) == 'my_class.SErViNgSlIcEs'

def test_strongest_extension_extension_with_lowercase_letters():
    """Test with extension having lowercase letters"""
    assert Strongest_Extension('my_class', ['seRviNgSlIcEs', 'Be', 'CC']) == 'my_class.Be'

def test_strongest_extension_extension_with_special_characters():
    """Test with extension having special characters"""
    assert Strongest_Extension('my_class', ['SErViNgSlIcEs!', 'Be', 'CC']) == 'my_class.SErViNgSlIcEs'

def test_strongest_extension_extension_with_numbers():
    """Test with extension having numbers"""
    assert Strongest_Extension('my_class', ['SErViNgSlIcEs1', 'Be', 'CC']) == 'my_class.SErViNgSlIcEs'

def test_strongest_extension_extension_with_dots():
    """Test with extension having dots"""
    assert Strongest_Extension('my_class', ['SErViNg.Sli.CEs', 'Be', 'CC']) == 'my_class.SErViNg.Sli.CEs'

def test_strongest_extension_multiple_extensions():
    """Test with multiple extensions"""
    assert Strongest_Extension('my_class', ['AA', 'be', 'AA', 'cc']) == 'my_class.AA'

def test_strongest_extension_extensions_same_class():
    """Test with extensions having different strengths but same class"""
    assert Strongest_Extension('my_class', ['SErviNGSliCes', 'cheese', 'StuFfed']) == 'my_class.SErviNGSliCes'