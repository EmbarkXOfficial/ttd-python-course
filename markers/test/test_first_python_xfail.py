import sys

import pytest

from markers.app.FirstPython import multiply, divide, add


@pytest.mark.xfail
def test_add():
    print("yes executed")
    assert add(40, 20) == 30


@pytest.mark.xfail(reason="Should be skipped")
def test_multiply():
    assert multiply(10, 20) == 200


@pytest.mark.xfail(sys.version_info > (3, 7), reason="Python version not compatible")
def test_divide():
    assert divide(20, 10) == 2
