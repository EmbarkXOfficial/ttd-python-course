import sys

import pytest

from markers.app.FirstPython import multiply, divide, add


@pytest.mark.skip
def test_add():
    print("Add executed")
    assert add(10, 20) == 30


@pytest.mark.skip(reason="Just thought of skipping this test")
def test_multiply():
    assert multiply(10, 20) == 200


@pytest.mark.skipif(sys.version_info > (3, 7), reason="Python version not compatible")
def test_divide():
    assert divide(20, 10) == 2
