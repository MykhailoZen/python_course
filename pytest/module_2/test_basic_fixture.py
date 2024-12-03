import pytest


@pytest.fixture
def input_data():
    return {
        "config": {
            "s_1": {"k_1": "v_1", "k_2": "v_2"},
            "s_2": {"k_3": "v_3", "k_4": "v_4"},
        }
    }


def test_input_data(input_data):
    assert "config" in input_data
    assert "s_1" in input_data["config"]
    assert "s_2" in input_data["config"]
    assert input_data["config"]["s_1"]["k_1"] == "v_1"
    assert input_data["config"]["s_1"]["k_2"] == "v_2"
    assert input_data["config"]["s_2"]["k_3"] == "v_3"
    assert input_data["config"]["s_2"]["k_4"] == "v_4"
