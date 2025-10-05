import pytest
from ascii_calculator.ascii_calculator import char_to_ascii, ascii_to_char

def test_char_to_ascii_single():
    char_to_ascii('A') == [65]
    char_to_ascii('a') == [97]

def test_char_to_ascii_multiple():
    char_to_ascii('abc') == [97, 98, 99]
    char_to_ascii('Hello') == [72, 101, 108, 108, 111]

def test_ascii_to_char_single():
    ascii_to_char([65]) == 'A'
    ascii_to_char([97]) == 'a'

def test_ascii_to_char_multiple():
    ascii_to_char([97, 98, 99]) == 'abc'
    ascii_to_char([72, 101, 108, 108, 111]) == 'Hello'

def test_char_to_ascii_invalid():
    with pytest.raises(ValueError):
        char_to_ascii(123)

def test_ascii_to_char_invalid():
    with pytest.raises(ValueError):
        ascii_to_char(128)

def test_defaults():
    char_to_ascii() == [97]
    ascii_to_char() == 'a'

