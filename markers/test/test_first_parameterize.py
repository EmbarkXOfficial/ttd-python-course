import pytest

from markers.app.FirstPython import add


@pytest.mark.parametrize("output, a, b",
                         [
                             (30, 10, 20),
                             (300, 100, 200),
                             (3000, 1000, 2000)
                         ],
                         ids=["first", "second", "third"]
                         )
def test_add(output, a, b):
    assert add(a, b) == output
    # assert add(10, 20) == 30
    # assert add(100, 200) == 300
    # assert add(1000, 2000) == 3000
