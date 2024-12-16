import os
from pathlib import Path

import pytest

@pytest.fixture
def input_data() -> dict:
    return {
        "name": "Bob",
        "age": 30,
        "sex": "Male",
    }

@pytest.fixture
def files_operations(tmp_path: Path):
    dir = tmp_path / "temp"
    dir.mkdir()
    input_file = dir / "temp_input.txt"
    output_file = dir / "temp_output.txt"
    yield input_file, output_file
    os.remove(input_file)
    os.remove(output_file)