import pytest


@pytest.fixture()
def input_data():
    return {
        'module': 'Data Collector',
        'version': '1.13.22',
        'OS': 'Windows',
    }


@pytest.fixture
def temp_file_creation(tmp_path):
    input_file = tmp_path / 'input.txt'
    output_file = tmp_path / 'output.txt'
    yield input_file, output_file
