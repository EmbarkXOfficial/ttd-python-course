import pytest


# pytest.raises()

def test_exception_demo():
    with pytest.raises(ZeroDivisionError):
        print(100 / 0)


def test_exception_demo_wrapper():
    with pytest.raises(ZeroDivisionError, match=r".* by .*") as expinfo:
        print(100 / 0)
    print(type(expinfo))
    print(expinfo.type)
    print(expinfo.value)
    print(expinfo.traceback)
