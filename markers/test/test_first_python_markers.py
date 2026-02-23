import pytest

from markers.app.FirstPython import multiply, divide, add


@pytest.mark.md
def test_add():
    assert add(10, 20) == 30


@pytest.mark.md
def test_multiply():
    assert multiply(10, 20) == 200


@pytest.mark.div
def test_divide():
    assert divide(20, 10) == 2
