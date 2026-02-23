from unittest import mock

import pytest

from mocking.src import Service


@mock.patch("mocking.src.Service.check_availability")
def test_first_mock(first_mock):
    first_mock.return_value = False
    print(Service.is_available())


@mock.patch("mocking.src.Service.get_password")
@pytest.mark.parametrize("username,password",
                         [
                             ("aaaa", "123"),
                             ("bbbb", "456"),
                             ("cccc", "789")
                         ]
                         )
def test_first_mock_parameterized(mock, username, password):
    mock.return_value = "123"
    print(Service.validate_user(username, password))
