"""
Kayak, Radar, Noon
"""
import pytest


def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False

@pytest.mark.palindrome
def test_palindrome_positive():
    assert is_palindrome("RaDar")


def test_palindrome_negative():
    assert is_palindrome("pYthoN") == False


def test_palindrome_empty():
    assert is_palindrome("")


def test_palindrome_int_input():
    with pytest.raises(AttributeError):
        assert is_palindrome(1234)
