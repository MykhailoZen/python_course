import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()


def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0