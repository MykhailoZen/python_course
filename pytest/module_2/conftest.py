import pytest

@pytest.fixture
def input_data() -> dict:
    return {
        "name": "Bob",
        "age": 30,
        "sex": "Male",
    }
