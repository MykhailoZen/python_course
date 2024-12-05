import pytest

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

@pytest.mark.parametrize('input_str, expected', [
    # Basic palindromes
    ('radar', True),
    ('level', True),
    ('deed', True),
    ('hello', False),

    # Empty string and single character
    ('', True),
    ('a', True),

    # Case sensitivity
    ('Radar', True),
    ('RaDaR', True),

    # Spaces and special characters
    ('A man a plan a canal Panama', True),
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
Task: Run all tests from the tests folder.
Answer: pytest test_string_operations.py

Task: Run only the multiplication test from the test_math.py file using the test name filtering option.
Answer: pytest -v -m palindrome test_string_operations.py

"""