import pytest


def palindrome_checker(phrase):
    return ''.join(phrase.lower().split(' '))[::-1] == ''.join(phrase.lower().split(' '))


@pytest.mark.palindrome
@pytest.mark.parametrize('phrase', [
    'abba',
    'Do geese see God',
    '1441'
])
def test_palindrome(phrase):
    assert palindrome_checker(phrase)


@pytest.mark.P0
@pytest.mark.parametrize('phrase', [
    'barry',
    'abba!',
    'In God we trust'
])
def test_not_palindrome(phrase):
    assert not palindrome_checker(phrase)

# run only the tests from the test_string_operations.py -> pytest <path_to_file>/test_string_operations.py
# use marker filtering to run only the palindrome -> -> pytest <path_to_file>/test_string_operations.py -m 'palindrome'
