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


# this fixture is called by the test, but doesn't capture actual text from caplog and do nothing as the result.
# can't get for now how to make it work
@pytest.fixture
def cli_log_capture(caplog):
    with open('pytest.log.txt', 'a') as capture:
        capture.write(caplog.text)
