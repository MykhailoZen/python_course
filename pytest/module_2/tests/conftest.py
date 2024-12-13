"""
Create a conftest.py file in the tests directory
Move all your fixtures into the conftest.py file.
Execute all your tests, created so far, and verify that all fixtures work as expected
"""
import pytest
import tempfile
import os

from urllib3 import request

@pytest.fixture
def input_data():
    return {
        'wifi_config': {
            'AP_name': 'testWiFi',
            'AP_pass': '12345q'
        },
        'device': {
            'platform': 'dpd',
            'type': 'camera',
            'name': 'longfin'
        }
    }

#@pytest.fixture
#def input_file_data():
 #   return  "this is test text to deal with fixtures."

@pytest.fixture
def temp_file_handler(request):
    """Fixture to create and manage temporary files"""
    temp_files = []
    def create_temp_file():
        temp_file = tempfile.NamedTemporaryFile(mode='r+', delete=False)
        temp_files.append(temp_file)
        return temp_file

    yield create_temp_file

    keep_files = request.config.getoption("--keep-temp-files")
    for temp_file in temp_files:
        if not temp_file.closed:
            temp_file.close()

        if not keep_files and os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
            print(f"Deleted temporary file: {temp_file.name}")
        else:
            print(f"Kept temporary file: {temp_file.name}")


def pytest_addoption(parser):
    parser.addoption(
        "--keep-temp-files",
        action="store_true",
        default=False,
        help="Keep temporary files after test execution"
    )