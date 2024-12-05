import pytest

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

@pytest.mark.parametrize('input_str, expected', [
    # Basic palindromes
    ('radar', True),
    ('level', True),
    ('deed', True),
    pytest.param('hello', False, marks=pytest.mark.p0),

    # Empty string and single character
    ('', True),
    ('a', True),

    # Case sensitivity
    ('Radar', True),
    ('RaDaR', True),

    # Spaces and special characters
    pytest.param('A man a plan a canal Panama', True, marks=pytest.mark.p0),
    ('race a car', False),
    ('Was it a car or a cat I saw?', True),

    # Numbers and mixed content
    ('12321', True),
    ('12345', False),
    ('A1b22b1a', True),

])
@pytest.mark.palindrome
def test_is_palindrome(input_str, expected):
    assert is_palindrome(input_str) == expected

"""
pytest test_string_operations.py

Answer: pytest -v -m palindrome test_string_operations.py

"""