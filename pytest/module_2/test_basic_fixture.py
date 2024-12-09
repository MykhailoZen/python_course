import pytest


def get_config_values(config_file):
    return list(config_file.items())


def test_input_validation(input_data):
    assert get_config_values(input_data) == [('module', 'Data Collector'), ('version', '1.13.22'), ('OS', 'Linux')]
# 'OS' is changed to 'Linux' intentionally to make test fail to introduce rerun -> pytest --reruns 3 --reruns-delay 3


@pytest.mark.xfail(reason='Update is not rolled out yet')
def test_version_after_update(input_data):
    assert [x[1] for x in get_config_values(input_data) if x[0] == 'version'][0] == '1.14.0'
