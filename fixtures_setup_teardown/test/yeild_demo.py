import pytest


@pytest.fixture
def a():
    print("Database initialization : Fixture a called")
    yield 10
    print("a : Database connection closed")


@pytest.fixture
def b():
    print("Database initialization : Fixture b called")
    yield 20
    print("b : Database connection closed")


def test_multiply(a):
    print("Database related code : ", str(a))


def test_divide(a, b):
    print("Database related code : ", str(b / a))
