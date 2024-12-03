import pytest
import tempfile
import os


@pytest.fixture
def input_data():
    return {
        "config": {
            "s_1": {"k_1": "v_1", "k_2": "v_2"},
            "s_2": {"k_3": "v_3", "k_4": "v_4"},
        }
    }


@pytest.fixture
def temp_files():
    input_file = tempfile.NamedTemporaryFile(delete=False)
    output_file = tempfile.NamedTemporaryFile(delete=False)
    yield input_file, output_file
    os.remove(input_file.name)
    os.remove(output_file.name)
