import pytest


@pytest.fixture(autouse=True)
def for_all():
    print("for all called")
    return 100


@pytest.fixture
def a():
    print("Fixture a called")
    return 10


@pytest.fixture
def c(a):
    return 100 / a


@pytest.fixture
def b():
    print("Fixture b called")
    return 20


def test_multiply(a):
    print("Database related code : ", str(a))


def test_divide(a, b):
    print("Database related code : ", str(b / a))
