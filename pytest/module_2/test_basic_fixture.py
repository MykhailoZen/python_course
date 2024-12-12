# Create a new test file named test_basic_fixture.py.
# Write a fixture named input_data that returns a dict with a predefined structure
# (a config with defined sections, for example).
# Write a test function that validates input data.

import pytest


@pytest.fixture
def input_data():
    return {
        'phone1': {
            'brand': 'Apple',
            'color': 'red',
            'capacity': 128
        },
        'phone2': {
            'brand': 'Samsung',
            'color': 'blue',
            'capacity': 256
        }}


def test_validate_input_data(input_data):
    assert input_data['phone1']['brand'] == 'Apple', f'The brand {input_data["phone1"]["brand"]} is not correct.'
    assert input_data['phone1']['color'] == 'red', f'The color {input_data["phone1"]["color"]} is not correct.'
    assert input_data['phone1']['capacity'] == 128, 'The capacity {input_data["phone1"]["capacity"]} is not correct.'
    assert input_data['phone2']['brand'] == 'Samsung', f'The brand {input_data["phone2"]["brand"]} is not correct.'
    assert input_data['phone2']['color'] == 'blue', f'The color {input_data["phone2"]["color"]} is not correct.'
    assert input_data['phone2']['capacity'] == 256, 'The capacity {input_data["phone2"]["capacity"]} is not correct.'
