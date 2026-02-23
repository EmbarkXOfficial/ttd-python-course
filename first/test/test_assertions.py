from first.app.FirstPython import add


def test_add():
    if add(20, 30) == 40:
        print("Works")
    else:
        print("Failed")
